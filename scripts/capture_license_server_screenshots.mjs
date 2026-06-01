#!/usr/bin/env node

import { spawn } from "node:child_process";
import { existsSync } from "node:fs";
import fs from "node:fs/promises";
import net from "node:net";
import path from "node:path";
import { fileURLToPath } from "node:url";
import { chromium } from "playwright";

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
const repoRoot = path.resolve(__dirname, "..");

const DEFAULT_REPO_URL = "https://github.com/sebleedelisle/liberation-license-server";
const DEFAULT_BRANCH = "main";
const DEFAULT_CLONE_DIR = path.join(repoRoot, ".screenshot-work", "license-server");
const MONGO_IMAGE = process.env.LICENSE_SERVER_MONGO_IMAGE || "mongo:7";
const MONGO_DRIVER = process.env.LICENSE_SERVER_MONGO_DRIVER || "auto";
const RELEASE_METADATA_URL =
    process.env.LICENSE_SERVER_RELEASE_METADATA_URL || "https://liberationlaser.com/changelog";
const PASSWORD = "liberation-docs";
const DOCUMENTATION_COUNTRY_CODE = "GB";
const DOCUMENTATION_CURRENCY = "GBP";
const PRODUCT_PRICES = {
    "LBN-HOBBY-2-MONTHLY": { USD: 15, GBP: 10, EUR: 15 },
    "LBN-HOBBY-4-MONTHLY": { USD: 25, GBP: 20, EUR: 25 },
    "LBN-PRO-8-MONTHLY": { USD: 50, GBP: 40, EUR: 45 },
    "LBN-PRO-UNLIMITED-MONTHLY": { USD: 100, GBP: 80, EUR: 95 },
};

const repoUrl = process.env.LICENSE_SERVER_REPO_URL || DEFAULT_REPO_URL;
const branch = process.env.LICENSE_SERVER_REPO_BRANCH || DEFAULT_BRANCH;
const cloneDir = process.env.LICENSE_SERVER_CLONE_DIR || DEFAULT_CLONE_DIR;
const assetDirs = ["en-GB/.gitbook/assets"].map((dir) =>
    path.join(repoRoot, dir)
);
const primaryAssetDir = assetDirs[0];
const DEFAULT_VIEWPORT = { width: 1340, height: 1100 };
const DEFAULT_CONTEXT_PADDING = 64;
const DEFAULT_IMAGE_BORDER = 8;

function step(message) {
    console.log(`\n[license screenshots] ${message}`);
}

function redact(value) {
    const token = process.env.GITHUB_TOKEN || process.env.GH_TOKEN;
    return token ? String(value).replaceAll(token, "<github-token>") : String(value);
}

function repoUrlWithToken(url) {
    const token = process.env.GITHUB_TOKEN || process.env.GH_TOKEN;
    if (!token || !url.startsWith("https://github.com/")) {
        return url;
    }

    const parsed = new URL(url);
    if (parsed.username || parsed.password) {
        return url;
    }
    parsed.username = "x-access-token";
    parsed.password = token;
    return parsed.toString();
}

function run(command, args, options = {}) {
    const {
        cwd = repoRoot,
        env = process.env,
        stdio = "inherit",
        okStatuses = [0],
    } = options;

    return new Promise((resolve, reject) => {
        const child = spawn(command, args, {
            cwd,
            env,
            stdio,
            shell: false,
        });

        let stdout = "";
        let stderr = "";

        if (stdio === "pipe") {
            child.stdout?.on("data", (chunk) => {
                stdout += chunk.toString();
            });
            child.stderr?.on("data", (chunk) => {
                stderr += chunk.toString();
            });
        }

        child.on("error", reject);
        child.on("close", (status) => {
            if (okStatuses.includes(status)) {
                resolve({ stdout, stderr, status });
                return;
            }

            const display = [command, ...args].map(redact).join(" ");
            reject(
                new Error(
                    `Command failed (${status}): ${display}\n${redact(stderr || stdout)}`
                )
            );
        });
    });
}

async function pathExists(filePath) {
    try {
        await fs.access(filePath);
        return true;
    } catch {
        return false;
    }
}

async function findFreePort() {
    return new Promise((resolve, reject) => {
        const server = net.createServer();
        server.unref();
        server.on("error", reject);
        server.listen(0, "127.0.0.1", () => {
            const address = server.address();
            server.close(() => resolve(address.port));
        });
    });
}

async function waitForTcp(port, timeoutMs = 30000) {
    const deadline = Date.now() + timeoutMs;
    while (Date.now() < deadline) {
        const connected = await new Promise((resolve) => {
            const socket = net.connect({ host: "127.0.0.1", port });
            socket.once("connect", () => {
                socket.destroy();
                resolve(true);
            });
            socket.once("error", () => resolve(false));
            socket.setTimeout(1000, () => {
                socket.destroy();
                resolve(false);
            });
        });

        if (connected) {
            return;
        }
        await new Promise((resolve) => setTimeout(resolve, 500));
    }
    throw new Error(`Timed out waiting for TCP port ${port}`);
}

async function waitForHttp(url, serverProcess, getLogs, timeoutMs = 60000) {
    const deadline = Date.now() + timeoutMs;
    while (Date.now() < deadline) {
        if (serverProcess.exitCode !== null) {
            throw new Error(`Licence server exited early.\n${getLogs()}`);
        }

        try {
            const response = await fetch(url, { redirect: "manual" });
            if (response.status >= 200 && response.status < 500) {
                return;
            }
        } catch {
            // Keep polling until the server is ready.
        }
        await new Promise((resolve) => setTimeout(resolve, 750));
    }
    throw new Error(`Timed out waiting for ${url}\n${getLogs()}`);
}

async function stopProcess(child) {
    if (!child || child.exitCode !== null) {
        return;
    }

    child.kill("SIGTERM");
    const exited = await new Promise((resolve) => {
        const timer = setTimeout(() => resolve(false), 5000);
        child.once("exit", () => {
            clearTimeout(timer);
            resolve(true);
        });
    });

    if (!exited && child.exitCode === null) {
        child.kill("SIGKILL");
    }
}

async function prepareClone() {
    const parentDir = path.dirname(cloneDir);
    await fs.mkdir(parentDir, { recursive: true });

    const authenticatedUrl = repoUrlWithToken(repoUrl);
    const gitDir = path.join(cloneDir, ".git");

    if (!existsSync(gitDir)) {
        await fs.rm(cloneDir, { recursive: true, force: true });
        step(`Cloning ${repoUrl} (${branch})`);
        await run("git", [
            "clone",
            "--depth",
            "1",
            "--branch",
            branch,
            authenticatedUrl,
            cloneDir,
        ]);
        await run("git", ["remote", "set-url", "origin", repoUrl], {
            cwd: cloneDir,
            stdio: "pipe",
        });
        return;
    }

    step(`Updating clone in ${path.relative(repoRoot, cloneDir)}`);
    await run("git", ["fetch", "--depth", "1", authenticatedUrl, branch], {
        cwd: cloneDir,
    });
    await run("git", ["checkout", "-B", branch, "FETCH_HEAD"], {
        cwd: cloneDir,
    });
    await run("git", ["remote", "set-url", "origin", repoUrl], {
        cwd: cloneDir,
        stdio: "pipe",
    });
}

async function installServerDependencies() {
    if (process.env.LICENSE_SERVER_SKIP_INSTALL === "1") {
        step("Skipping licence server npm install");
        return;
    }

    const hasPackageLock = await pathExists(path.join(cloneDir, "package-lock.json"));
    step(hasPackageLock ? "Installing licence server dependencies with npm ci" : "Installing licence server dependencies with npm install");
    await run("npm", [hasPackageLock ? "ci" : "install"], { cwd: cloneDir });
}

async function startMemoryMongo() {
    step("Starting in-memory MongoDB");
    const { MongoMemoryServer } = await import("mongodb-memory-server");
    const server = await MongoMemoryServer.create({
        instance: {
            dbName: "liberation_docs_screenshots",
            ip: "127.0.0.1",
        },
    });

    return {
        driver: "memory",
        databaseUrl: server.getUri("liberation_docs_screenshots"),
        server,
    };
}

async function startDockerMongo() {
    await run("docker", ["--version"], { stdio: "pipe" });

    const mongoPort = await findFreePort();
    const containerName = `liberation-docs-mongo-${process.pid}`;
    step(`Starting MongoDB ${MONGO_IMAGE} on port ${mongoPort}`);

    const result = await run(
        "docker",
        [
            "run",
            "--rm",
            "-d",
            "--name",
            containerName,
            "-p",
            `127.0.0.1:${mongoPort}:27017`,
            MONGO_IMAGE,
        ],
        { stdio: "pipe" }
    );

    await waitForTcp(mongoPort, 45000);

    return {
        driver: "docker",
        mongoPort,
        containerName,
        databaseUrl: `mongodb://127.0.0.1:${mongoPort}/liberation_docs_screenshots`,
        containerId: result.stdout.trim(),
    };
}

async function startMongo() {
    if (process.env.LICENSE_SERVER_DATABASE_URL) {
        step("Using MongoDB from LICENSE_SERVER_DATABASE_URL");
        return {
            driver: "external",
            databaseUrl: process.env.LICENSE_SERVER_DATABASE_URL,
        };
    }

    if (MONGO_DRIVER === "memory" || MONGO_DRIVER === "auto") {
        try {
            return await startMemoryMongo();
        } catch (error) {
            if (MONGO_DRIVER === "memory") {
                throw error;
            }
            console.warn(`[license screenshots] In-memory MongoDB failed, trying Docker: ${error.message}`);
        }
    }

    if (MONGO_DRIVER === "docker" || MONGO_DRIVER === "auto") {
        return await startDockerMongo();
    }

    throw new Error(
        `Unknown LICENSE_SERVER_MONGO_DRIVER "${MONGO_DRIVER}". Use "auto", "memory", or "docker".`
    );
}

async function stopMongo(mongo) {
    if (!mongo) {
        return;
    }

    if (mongo.driver === "memory") {
        step("Stopping in-memory MongoDB");
        await mongo.server.stop();
        return;
    }

    if (mongo.driver !== "docker") {
        return;
    }

    step("Stopping MongoDB Docker container");
    await run("docker", ["stop", mongo.containerName], {
        stdio: "pipe",
        okStatuses: [0, 1],
    });
}

function parseReleaseMetadata(html) {
    const match = html.match(
        /Version\s*:\s*([0-9.]+)(?:\s*Build\s*([0-9]+))?[\s\S]*?Build date\s*:\s*([^<\n]+)/i
    );
    if (!match) {
        throw new Error(`Could not parse release metadata from ${RELEASE_METADATA_URL}`);
    }

    const releaseDate = new Date(`${match[3].trim()} UTC`);
    if (Number.isNaN(releaseDate.getTime())) {
        throw new Error(`Could not parse release date "${match[3].trim()}"`);
    }

    return {
        version: match[1],
        build: match[2] ? Number(match[2]) : null,
        releaseDate: releaseDate.toISOString(),
    };
}

async function fetchReleaseMetadata() {
    step(`Fetching release metadata from ${RELEASE_METADATA_URL}`);
    const response = await fetch(RELEASE_METADATA_URL);
    if (!response.ok) {
        throw new Error(`Could not fetch release metadata: ${response.status} ${response.statusText}`);
    }

    const metadata = parseReleaseMetadata(await response.text());
    const buildText = metadata.build === null ? "" : ` Build ${metadata.build}`;
    step(`Using Liberation ${metadata.version}${buildText}`);
    return metadata;
}

function seedScriptSource(releaseMetadata) {
    const releaseMetadataJson = JSON.stringify(releaseMetadata);
    const productPricesJson = JSON.stringify(PRODUCT_PRICES);
    return `
import fs from 'node:fs/promises';
import mongoose from 'mongoose';
import bcrypt from 'bcryptjs';
import Product from './models/Product.js';
import User from './models/User.js';
import Machine from './models/Machine.js';
import Download from './models/Download.js';

const outputPath = process.argv[2];
const password = '${PASSWORD}';
const passwordHash = await bcrypt.hash(password, 10);
const releaseMetadata = ${releaseMetadataJson};
const productPrices = ${productPricesJson};
const releaseDate = new Date(releaseMetadata.releaseDate);

function monthDate(base, monthOffset) {
    return new Date(Date.UTC(base.getUTCFullYear(), base.getUTCMonth() + monthOffset, 6, 10, 0, 0));
}

const now = new Date();
let expiryDate = monthDate(now, 1);
if (expiryDate.getTime() <= now.getTime() + 7 * 24 * 60 * 60 * 1000) {
    expiryDate = monthDate(now, 2);
}

const startDate = monthDate(expiryDate, -2);
const lastRenewalDate = monthDate(expiryDate, -1);

function productData(productCode, tierName, planName, seats, lasers, dmx) {
    return {
        productCode,
        appId: 'LBN01',
        appName: 'Liberation',
        tierName,
        planName,
        price: productPrices[productCode],
        subscriptionPeriod: 'month',
        subscriptionQuantity: 1,
        gracePeriodDays: 7,
        numberOfSeats: seats,
        numLasers: lasers,
        numDmx: dmx,
        paymentData: {
            paddle: {
                paddlePlanId: 'docs-' + productCode.toLowerCase(),
            },
        },
        visible: true,
    };
}

function paddlePayment(email, suffix) {
    return {
        paddle: {
            paddleSubscriptionId: 'docs-' + suffix,
            paddleUserId: 'docs-user-' + suffix,
            paddleEmail: email,
        },
    };
}

function licence({ product, email, suffix, state = 1, machines = [] }) {
    return {
        product: product._id,
        startDate,
        lastRenewalDate,
        expiryDate,
        subscriptionState: state,
        paymentData: paddlePayment(email, suffix),
        currency: '${DOCUMENTATION_CURRENCY}',
        machines: machines.map((machine) => machine._id),
        scheduledChanges: [],
        useCount: 42,
        lastUseDate: lastRenewalDate,
    };
}

await mongoose.connect(process.env.DATABASE_URL);
await mongoose.connection.dropDatabase();

const products = await Product.create([
    productData('LBN-HOBBY-2-MONTHLY', 'Hobby 2', 'Hobby 2', 1, 2, 0),
    productData('LBN-HOBBY-4-MONTHLY', 'Hobby 4', 'Hobby 4', 1, 4, 4),
    productData('LBN-PRO-8-MONTHLY', 'Pro 8', 'Pro 8', 2, 8, 8),
    productData('LBN-PRO-UNLIMITED-MONTHLY', 'Pro Unlimited', 'Pro Unlimited', 3, 10000, 10000),
]);

const byCode = Object.fromEntries(products.map((product) => [product.productCode, product]));

const normalMachine = await Machine.create({
    machineId: 'MACDOC000001ABCDEF123456',
    machineIdHash: 'docs-mac-hash',
    machineIdOriginal: 'Docs MacBook Pro',
    platform: 'Mac',
    valid: true,
    lastAccessTimeByProduct: [
        {
            productCode: 'LBN01',
            version: releaseMetadata.version,
            lastAccessDate: lastRenewalDate,
        },
    ],
});

await Download.create([
    {
        appCode: 'LBN01',
        version: releaseMetadata.version,
        build: releaseMetadata.build,
        platform: 'mac',
        type: 'release',
        accessLevel: 'public',
        status: 'published',
        url: 'https://example.com/Liberation-' + releaseMetadata.version + '.dmg',
        isPublic: true,
        releaseDate,
    },
    {
        appCode: 'LBN01',
        version: releaseMetadata.version,
        build: releaseMetadata.build,
        platform: 'windows',
        type: 'release',
        accessLevel: 'public',
        status: 'published',
        url: 'https://example.com/Liberation-Setup-' + releaseMetadata.version + '.exe',
        isPublic: true,
        releaseDate,
    },
]);

const normalEmail = 'docs.normal@example.com';
const normalUser = new User({
    name: 'Docs Normal User',
    firstName: 'Docs',
    email: normalEmail,
    password: passwordHash,
    address: { countryCode: '${DOCUMENTATION_COUNTRY_CODE}' },
    emailConfirmed: true,
    downloadAccessLevel: 'public',
    licenses: [
        licence({
            product: byCode['LBN-HOBBY-4-MONTHLY'],
            email: normalEmail,
            suffix: 'normal-active',
            state: 1,
            machines: [normalMachine],
        }),
    ],
});
await normalUser.save();

const cancelledEmail = 'docs.cancelled@example.com';
const cancelledUser = new User({
    name: 'Docs Cancelled User',
    firstName: 'Docs',
    email: cancelledEmail,
    password: passwordHash,
    address: { countryCode: '${DOCUMENTATION_COUNTRY_CODE}' },
    emailConfirmed: true,
    downloadAccessLevel: 'public',
    licenses: [
        licence({
            product: byCode['LBN-HOBBY-4-MONTHLY'],
            email: cancelledEmail,
            suffix: 'cancelled-auto-renew-off',
            state: 2,
            machines: [],
        }),
    ],
});
await cancelledUser.save();

await fs.writeFile(
    outputPath,
    JSON.stringify(
        {
            password,
            users: {
                normal: {
                    email: normalEmail,
                    activeLicenceId: normalUser.licenses[0]._id.toString(),
                },
                cancelled: {
                    email: cancelledEmail,
                    autoRenewOffLicenceId: cancelledUser.licenses[0]._id.toString(),
                },
            },
            release: releaseMetadata,
            dates: {
                startDate,
                lastRenewalDate,
                expiryDate,
            },
        },
        null,
        2
    )
);

await mongoose.disconnect();
`;
}

async function seedDatabase(databaseUrl, releaseMetadata) {
    const seedFile = path.join(cloneDir, ".docs-screenshot-seed.mjs");
    const outputFile = path.join(cloneDir, ".docs-screenshot-seed-output.json");

    await fs.writeFile(seedFile, seedScriptSource(releaseMetadata), "utf8");
    step("Seeding screenshot data");
    await run("node", [seedFile, outputFile], {
        cwd: cloneDir,
        env: {
            ...process.env,
            DATABASE_URL: databaseUrl,
            NODE_ENV: "production",
            DISCOURSE_URL: "",
            DISCOURSE_API_KEY: "",
            DISCOURSE_SSO_SECRET: "",
        },
    });

    const data = JSON.parse(await fs.readFile(outputFile, "utf8"));
    await fs.rm(seedFile, { force: true });
    await fs.rm(outputFile, { force: true });
    return data;
}

async function startLicenseServer(databaseUrl) {
    const serverPort = await findFreePort();
    const baseUrl = `http://127.0.0.1:${serverPort}`;

    const env = {
        ...process.env,
        NODE_ENV: "production",
        PORT: String(serverPort),
        DATABASE_URL: databaseUrl,
        SESSION_SECRET: "docs-screenshot-session-secret",
        JWT_SECRET: "docs-screenshot-jwt-secret",
        WEBSITE_URL: baseUrl,
        EMAIL_DIRECT_URL: baseUrl,
        WEBSITE_DOMAIN: `127.0.0.1:${serverPort}`,
        USE_HTTPS: "no",
        RUN_UPDATES: "no",
        NO_RESTART_EMAIL: "1",
        TRUST_PROXY: "loopback",
        POSTMARK_API_TOKEN: "POSTMARK_API_TEST",
        PADDLE_VENDOR_ID: "123",
        PADDLE_AUTH_CODE: "docs-auth-code",
        PADDLE_PUBLIC_KEY: "docs-public-key",
        PADDLE_USE_SANDBOX: "true",
        SUPPORT_EMAIL: "support@example.com",
        ADMIN_EMAIL: "admin@example.com",
        DISCOURSE_URL: "",
        DISCOURSE_API_KEY: "",
        DISCOURSE_SSO_SECRET: "",
    };

    step(`Starting licence server on ${baseUrl}`);
    const child = spawn("npm", ["start"], {
        cwd: cloneDir,
        env,
        stdio: ["ignore", "pipe", "pipe"],
        shell: false,
    });

    let logs = "";
    const collect = (chunk) => {
        logs += chunk.toString();
        if (logs.length > 20000) {
            logs = logs.slice(-20000);
        }
    };
    child.stdout.on("data", collect);
    child.stderr.on("data", collect);

    await waitForHttp(`${baseUrl}/login`, child, () => logs, 60000);
    return { child, baseUrl };
}

function screenshotTargets(seedData) {
    const normal = seedData.users.normal;
    const cancelled = seedData.users.cancelled;

    return [
        {
            file: "account-download-page.png",
            aliases: ["windows-download-page.png"],
            user: "normal",
            path: "/account/download",
            selector: "body",
            maxHeight: 879,
            viewport: { width: 1340, height: 879 },
            contextPadding: 0,
            includeEmbeddedMedia: true,
            embeddedMediaCount: 2,
        },
        {
            file: "windows-install-download-page.png",
            user: "normal",
            path: "/account/download",
            selector: "body",
            maxHeight: 725,
            viewport: { width: 1340, height: 725 },
            contextPadding: 0,
            includeEmbeddedMedia: true,
            embeddedMediaCount: 2,
        },
        {
            file: "account-your-licences.png",
            user: "normal",
            path: "/account/my-products",
            selector: "main",
            maxHeight: 475,
        },
        {
            file: "account-active-licence.png",
            user: "normal",
            path: `/account/my-products/product?license=${normal.activeLicenceId}`,
            selector: "main",
            maxHeight: 560,
        },
        {
            file: "account-cancel-auto-renew.png",
            user: "normal",
            path: `/account/my-products/cancel?license=${normal.activeLicenceId}`,
            selector: ".narrow-form",
            maxHeight: 1220,
            viewport: { width: 1340, height: 1320 },
        },
        {
            file: "account-auto-renew-off.png",
            user: "cancelled",
            path: `/account/my-products/product?license=${cancelled.autoRenewOffLicenceId}`,
            selector: "main",
            maxHeight: 560,
        },
        {
            file: "account-change-licence-plan.png",
            user: "normal",
            path: `/account/my-products/change-plan?license=${normal.activeLicenceId}`,
            selector: "body",
            maxHeight: 760,
            viewport: { width: 1340, height: 760 },
            contextPadding: 0,
        },
    ];
}

async function loginContext(context, baseUrl, user, password) {
    const response = await context.request.post(`${baseUrl}/entry`, {
        form: {
            email: user.email,
            password,
            redirect: "/account/my-products",
        },
        headers: {
            // The screenshot server runs in production mode over local HTTP. This
            // lets express-session emit the secure cookie so we can copy the
            // signed session into the browser context for local rendering.
            "X-Forwarded-Proto": "https",
        },
        maxRedirects: 0,
    });
    const loginLocation = response.headers().location || "";

    if (![302, 303].includes(response.status())) {
        const body = await response.text().catch(() => "");
        throw new Error(`Login failed for ${user.email}: ${response.status()} ${body.slice(0, 200)}`);
    }

    const sessionCookie = response
        .headersArray()
        .find((header) => header.name.toLowerCase() === "set-cookie" && header.value.startsWith("connect.sid="));

    if (sessionCookie) {
        const [nameValue] = sessionCookie.value.split(";");
        const separator = nameValue.indexOf("=");
        if (separator > 0) {
            const rawValue = nameValue.slice(separator + 1);
            const value = decodeURIComponent(rawValue);
            await context.addCookies([
                {
                    name: nameValue.slice(0, separator),
                    value,
                    url: baseUrl,
                    httpOnly: true,
                    sameSite: "Lax",
                },
            ]);
        }
    }

    const authCheckPage = await context.newPage();
    const authCheckResponse = await authCheckPage.goto(`${baseUrl}/account/my-products`, {
        waitUntil: "domcontentloaded",
    });
    const authCheckUrl = authCheckPage.url();
    await authCheckPage.close();

    if (!authCheckResponse?.ok() || new URL(authCheckUrl).pathname === "/login") {
        const cookieSummary = (await context.cookies(baseUrl))
            .map((cookie) => `${cookie.name} domain=${cookie.domain} path=${cookie.path} secure=${cookie.secure}`)
            .join(", ");
        throw new Error(
            `Login did not authenticate ${user.email}: login redirected to ${loginLocation || "(none)"}, auth check landed on ${authCheckResponse?.status() || "no response"} ${authCheckUrl}; cookies: ${cookieSummary || "none"}`
        );
    }
}

async function prepareContext(browser, baseUrl, user, password) {
    const context = await browser.newContext({
        baseURL: baseUrl,
        viewport: DEFAULT_VIEWPORT,
        deviceScaleFactor: 1,
    });

    await context.route("**/*", (route) => {
        const url = route.request().url();
        if (url.includes("usefathom.com")) {
            route.abort();
            return;
        }
        route.continue();
    });

    await loginContext(context, baseUrl, user, password);
    return context;
}

async function addImageBorder(page, imagePath, borderWidth = DEFAULT_IMAGE_BORDER) {
    if (!borderWidth) {
        return;
    }

    const image = await fs.readFile(imagePath);
    const borderedImage = await page.evaluate(
        async ({ imageBase64, borderWidth }) => {
            const image = await new Promise((resolve, reject) => {
                const element = new Image();
                element.onload = () => resolve(element);
                element.onerror = reject;
                element.src = `data:image/png;base64,${imageBase64}`;
            });

            const canvas = document.createElement("canvas");
            canvas.width = image.naturalWidth + borderWidth * 2;
            canvas.height = image.naturalHeight + borderWidth * 2;

            const context = canvas.getContext("2d");
            context.fillStyle = "#000";
            context.fillRect(0, 0, canvas.width, canvas.height);
            context.drawImage(image, borderWidth, borderWidth);

            return canvas.toDataURL("image/png").split(",")[1];
        },
        {
            imageBase64: image.toString("base64"),
            borderWidth,
        }
    );

    await fs.writeFile(imagePath, Buffer.from(borderedImage, "base64"));
}

async function captureTarget(page, baseUrl, target, outputPath) {
    if (target.viewport) {
        await page.setViewportSize(target.viewport);
    }

    await page.goto(`${baseUrl}${target.path}`, { waitUntil: "domcontentloaded" });
    await page.waitForLoadState("load", { timeout: 10000 }).catch(() => {});
    if (target.includeEmbeddedMedia) {
        await page
            .waitForFunction((count) => {
                return document.querySelectorAll('iframe[src*="youtube"], iframe[src*="youtu"]').length >= count;
            }, target.embeddedMediaCount ?? 1, {
                timeout: 5000,
            })
            .catch(() => {});
        await page.waitForTimeout(1500);
    }
    await page.evaluate(() => document.fonts?.ready).catch(() => {});

    const locator = page.locator(target.selector).first();
    await locator.waitFor({ state: "visible", timeout: 10000 });

    const box = await locator.boundingBox();
    if (!box) {
        throw new Error(`Could not find screenshot selector ${target.selector} for ${target.path}`);
    }

    const viewport = page.viewportSize() || DEFAULT_VIEWPORT;
    const contextPadding =
        target.contextPadding ?? (target.selector === "body" ? 0 : DEFAULT_CONTEXT_PADDING);
    const x = Math.max(0, Math.floor(box.x - contextPadding));
    const y = Math.max(0, Math.floor(box.y - contextPadding));
    const width = Math.min(viewport.width - x, Math.ceil(box.width + contextPadding * 2));
    const requestedHeight = Math.ceil(box.height + contextPadding * 2);
    const height = Math.min(
        viewport.height - y,
        target.maxHeight || requestedHeight,
        requestedHeight
    );

    await page.screenshot({
        path: outputPath,
        clip: { x, y, width, height },
        animations: "disabled",
    });
    await addImageBorder(page, outputPath, target.borderWidth ?? DEFAULT_IMAGE_BORDER);
}

async function captureScreenshots(baseUrl, seedData) {
    await fs.mkdir(primaryAssetDir, { recursive: true });

    const browser = await chromium.launch();
    const contexts = new Map();

    try {
        for (const [name, user] of Object.entries(seedData.users)) {
            contexts.set(
                name,
                await prepareContext(browser, baseUrl, user, seedData.password)
            );
        }

        for (const target of screenshotTargets(seedData)) {
            const context = contexts.get(target.user);
            const page = await context.newPage();
            const outputPath = path.join(primaryAssetDir, target.file);
            step(`Capturing ${target.file}`);
            await captureTarget(page, baseUrl, target, outputPath);
            for (const alias of target.aliases ?? []) {
                await fs.copyFile(outputPath, path.join(primaryAssetDir, alias));
            }
            await page.close();
        }
    } finally {
        for (const context of contexts.values()) {
            await context.close().catch(() => {});
        }
        await browser.close().catch(() => {});
    }
}

async function mirrorAssets() {
    const generatedFiles = screenshotTargets({
        users: {
            normal: { activeLicenceId: "x" },
            cancelled: { autoRenewOffLicenceId: "x" },
        },
    }).flatMap((target) => [target.file, ...(target.aliases ?? [])]);

    for (const dir of assetDirs) {
        await fs.mkdir(dir, { recursive: true });
        if (dir === primaryAssetDir) {
            continue;
        }
        for (const file of generatedFiles) {
            await fs.copyFile(path.join(primaryAssetDir, file), path.join(dir, file));
        }
    }
}

async function main() {
    let mongo = null;
    let server = null;

    try {
        await prepareClone();
        await installServerDependencies();
        const releaseMetadata = await fetchReleaseMetadata();
        mongo = await startMongo();
        const seedData = await seedDatabase(mongo.databaseUrl, releaseMetadata);
        server = await startLicenseServer(mongo.databaseUrl);
        await captureScreenshots(server.baseUrl, seedData);
        await mirrorAssets();
        step("Screenshots captured successfully");
    } finally {
        await stopProcess(server?.child);
        await stopMongo(mongo);
    }
}

main().catch((error) => {
    console.error(error.message);
    process.exitCode = 1;
});
