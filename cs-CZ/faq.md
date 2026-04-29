---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/faq
---

# ✅ Časté dotazy

## Hardware

#### **Funguje Liberation na Windows?**

Ano – Liberation plně podporuje **Windows 10 a 11 (64bit)** a nabízí přesně stejné funkce jako verze pro Mac. Každé vydání vychází současně pro obě platformy.

#### **Funguje Liberation na Macu?**

Ano – Liberation plně podporuje **Mac (macOS 12 Monterey a novější)** a má stejnou sadu funkcí jako verze pro Windows. Všechny aktualizace vycházejí společně.

#### **Jaké jsou minimální požadavky na počítač?**

Záleží na tom, kolik laserů chcete ovládat. Pokud používáte jen několik laserů, vystačíte si i s méně výkonným počítačem. Jakýkoli Mac s Apple Silicon běží velmi dobře a měl by zvládnout ovládat až 100 laserů. Pokud připravujete složité show, kde je důležitá maximální spolehlivost, doporučujeme nejvýkonnější počítač, který si můžete dovolit.

#### **Kolik laserů mohu pomocí Liberation ovládat?**

Liberation dokáže spustit mnoho laserů z jednoho počítače. Byl testován s více než 100 laser controllers, takže odpověď závisí na:

* procesoru vašeho počítače
* rychlosti sítě
* typu vašeho předplatného

#### **Které MIDI kontroléry mohu použít?**

Liberation byl navržen a optimalizován pro oblíbený MIDI kontrolér APC40 Mk2. Funguje také s APC40 Mk1. Viz [Živé ovládání pomocí APC40](midi-control/live-control-with-the-apc40.md)

Postupně přidáváme další MIDI kontroléry a aktuálně podporujeme také APC Mini Mk2 a MIDI Fighter Twister.

K dispozici je také systém MIDI Send/Receive, který nabízí další možnosti ovládání přes MIDI. Viz [MIDI Send/Receive](midi-control/midi-send-receive.md)

Další informace najdete v části [Ovládání přes MIDI](midi-control/).

#### **Mohu použít libovolný MIDI kontrolér?**

Momentálně pracujeme na konfigurovatelném MIDI systému, který to v budoucnu umožní. Někteří uživatelé mezitím úspěšně používají MIDI převodník, který dokáže převést libovolné MIDI zprávy pro systém MIDI Send/Receive, ale jde o pracnější a pokročilý postup. Rady k tomuto nastavení hledejte na [fóru](https://forum.liberationlaser.com), ale realisticky je nejlepší volbou APC40.

## Laser controllers

#### **Které laser controllers jsou kompatibilní s Liberation?**

* [Ether Dream (doporučeno)](https://ether-dream.com)
* [Helios DAC](https://bitlasers.com/helios-laser-dac/)
* [Mercury od X-Laser](https://x-laser.com/pages/mercury-laser-control-system) (možná budete muset aktualizovat firmware)
* LaserCube USB (a LaserDock)
* síťový protokol LaserCube (s kabelovým připojením)
* AVB používané lasery [LASollinger](https://laseranimation.com/en/) (aktuálně pouze macOS, ve fázi testování)

Další informace najdete v části [Kompatibilní lasery a controllers (DAC)](hardware/compatible-lasers-and-controllers-dacs.md)

#### **Proč nepodporujete laser controller \[jiné značky]?**

Aby se podpořila lepší interoperabilita mezi softwarem a hardwarem, Liberation bude podporovat pouze DAC zařízení, která mají zveřejněný komunikační protokol. Věřím, že je to pro laserový obor nejlepší cesta vpřed.

#### **Jak poznám, zda lze můj laser použít s Liberation?**

Pokud má váš laser některou z následujících možností, můžete ho s Liberation použít:

* Externí **ILDA vstup** – 25pinový D konektor používaný s kompatibilním externím controller.
* Interně nainstalovaný **Ether Dream**.
* Libovolný **LaserCube** (funguje s USB i Wi-Fi LaserCube).
* **Jednotku X-Laser s vestavěným systémem Mercury** (v režimu Ether Dream).
* **Projektor LaserAnimation Sollinger s vestavěným AVB** (pouze macOS, vyžaduje síťová zařízení kompatibilní s AVB, aktuálně ve fázi testování).

Další informace najdete v části [Kompatibilní lasery a controllers (DAC)](hardware/compatible-lasers-and-controllers-dacs.md)

#### **Mohu používat Liberation se svým LaserCube?**

Ano, Liberation funguje přímo s jakýmkoli LaserCube. Viz [LaserCube](hardware/lasercube.md)

## Licence

#### **Kolik stojí licence?**

Aktuální ceny najdete na stránce [obchodu](https://liberationlaser.com/shop).

#### **Jaká jsou omezení jednotlivých licenčních úrovní?**

Aktuální možnosti licencí najdete na stránce [obchodu](https://liberationlaser.com/shop).

Upozorňujeme, že na **každé** úrovni, včetně bezplatné, můžete nastavovat, zobrazovat náhledy a navrhovat show s libovolným počtem laserů. Neexistují žádná další omezení kromě počtu laserů, které mohou být ve stavu _armed_. Všechny ostatní funkce Liberation jsou dostupné všem.

#### **Mohu přejít na vyšší úroveň?**

Na vyšší úroveň můžete přejít kdykoli. Za zbývající dobu aktuální licence dostanete částečnou refundaci a nový plán začne platit okamžitě. Viz [Upgrade nebo downgrade licence](installation/upgrade-downgrade-your-license.md)

#### **Mohu přejít na nižší licenci?**

Na nižší úroveň můžete přejít kdykoli, ale změna se projeví až na konci aktuálního licenčního období. Viz [Upgrade nebo downgrade licence](installation/upgrade-downgrade-your-license.md)

#### **Jak autorizuji počítač svou licencí?**

Po zakoupení licence můžete počítač autorizovat přímo v softwaru Liberation. Na obrazovce _About_ uvidíte tlačítko _Authorise_, které vás vyzve k přihlášení na web. Postupujte podle pokynů na obrazovce a dokončete proces autorizace. Viz [Autorizace a zrušení autorizace](installation/authorising-and-de-authorising.md)

#### **Jak často musím počítač připojit k internetu?**

Při každém obnovení licence je potřeba připojit Liberation k internetu, aby se aktualizovala interní licence. U měsíční opakované platby se budete muset připojit každý měsíc.

#### **Co se stane, když po obnovení nemohu počítač připojit k internetu?**

Liberation vám po obnovení licence poskytne 7denní ochrannou lhůtu na připojení k internetu a aktualizaci interní licence. Po uplynutí této doby se Liberation vrátí do režimu _Free_.

#### **Co se stane, když mi vyprší platnost platební karty?**

Od našeho poskytovatele plateb obdržíte e-mailové upozornění a bude potřeba aktualizovat platební údaje. Přihlaste se na web a na stránce předplatných použijte odkaz _Update payment details_.

#### **Jak zruším opakovanou licenci?**

Přihlaste se na web, otevřete stránku _Your subscriptions_, vyberte předplatné, které chcete zrušit, a klikněte na odkaz _Cancel Subscription_. Liberation můžete používat až do konce licenčního období.

#### **Na kolik počítačů mohu Liberation nainstalovat?**

Liberation můžete nainstalovat na libovolný počet počítačů. Autorizace licence je potřeba pouze pro povolení laserového / DMX výstupu a vaše licenční úroveň určuje, kolik počítačů může být současně autorizováno pro výstup. Viz [Jak funguje licencování](installation/how-licensing-works.md)

#### **Jak přesunu licenci z jednoho počítače na druhý?**

* Otevřete Liberation na počítači, který už nechcete používat
* Ujistěte se, že jste připojeni k internetu, a na obrazovce _About_ klikněte na tlačítko _De-authorise this computer_
* Nyní otevřete Liberation na novém počítači
* Na obrazovce _About_ klikněte na tlačítko _Authorise this computer_.
* Otevře se web, přihlaste se a podle pokynů na obrazovce dokončete autorizaci

Počítač, ke kterému už nemáte přístup, můžete zrušit i vzdáleně (s určitými omezeními). Viz [Autorizace a zrušení autorizace](installation/authorising-and-de-authorising.md)

#### **Mohu zrušit autorizaci Liberation na počítači, který se ztratil nebo byl odcizen?**

Autorizaci počítače můžete zrušit přes web. Pokud instalace Liberation nebyla od posledního obnovení online, lze to provést okamžitě.

Pokud ne, zrušení autorizace se projeví při obnovení předplatného nebo při připojení počítače k internetu, podle toho, co nastane dříve. Pokud nutně potřebujete znovu autorizovat nový počítač, kontaktujte podporu.

### Používání Liberation

#### Výchozí nastavení má 8 laserů – jak to změním?

Viz [Nastavení projektu](setting-up/setting-up-your-project.md) a [Přidávání a odebírání laserů](setting-up/adding-removing-lasers.md)

#### Mohu zkopírovat nastavení pro zone z jednoho laseru do ostatních?

Ano! Viz [Kopírování zones mezi lasery](output-view/copy-zones-between-lasers.md)

#### Mohu zadat číslo místo použití posuvníku?

Ano. Klikněte na posuvník se stisknutou klávesou `Cmd / Ctrl` a hodnotu můžete zadat pomocí klávesnice.

#### **Jak synchronizuji Liberation s hudbou?**

Má inteligentní systém „tap tempo“, který funguje tak, jak byste čekali, ale můžete použít také externí MIDI clock nebo Ableton Link. Viz [Synchronizace tempa](tempo-synchronisation.md). Timeline lze synchronizovat s příchozím LTC/SMPTE timecode přes libovolné zvukové rozhraní. Viz [Timecode](timecode.md).

#### Jaká nastavení mám upravit, abych z laseru dostal nejlepší výstup?

Hlavní nastavení je _Colour Shift_, které kompenzuje drobné zpoždění mezi pohybem zrcátek a změnou jasu laserů. Pokud mají laserové body/paprsky malé „ocásky“, je potřeba toto nastavení upravit. (Příklad „ocásků“ najdete na fotografiích na stránce [Laser Settings](setting-up/laser-settings.md))

Můžete také zkusit změnit rychlost skenerů – pomaleji, pokud máte základní skenery, nebo rychleji, pokud jsou kvalitní. **Používejte ale opatrně, protože při příliš velké zátěži můžete skenery poškodit.**

K dispozici je také několik předvoleb skenerů. Výchozí možnost je konzervativní a pro většinu požadavků na laserové paprsky je v pořádku. Pokud máte lepší skenery, existují další předvolby, a některé předvolby jsou laděné pro grafiku.

Další informace najdete v části [Laser Settings](setting-up/laser-settings.md) a informace o vytváření vlastních předvoleb najdete v části [Předvolby skenerů](advanced/scanner-presets.md) (pokročilé, rozpracováno)

Vyvážení barev můžete upravit také pomocí nastavení _Colour calibration_. Viz [Kalibrace barev](advanced/colour-calibration.md) (pokročilá technika)

#### Co dělá nastavení _Latency(ms)_?

Jde o latenci snímku, tedy maximální dobu mezi vygenerováním snímku a jeho následným odesláním do laseru. Neměli byste ji potřebovat upravovat, ale pokud máte problémy se sítí, můžete ji zkusit zvýšit. Další podrobnosti najdete v části [Nastavení Latency](setting-up/latency-setting.md).

### Clips

#### Jak upravím zones a nastavení pro Clip, aniž bych ho spustil?

Klikněte se stisknutou klávesou `Alt / Option`, aby se stal aktuálně vybraným Clip, ale neaktivoval se. Viz také [Spouštění a zastavování Clips](clips/starting-stopping-clips.md)

#### Jak zkopíruji Clips?

Klikněte a táhněte se stisknutou klávesou `Alt / Option`. Viz také [Uspořádání Clip Deck](clips/organising-your-clip-deck.md)

#### Jak smažu Clips?

Klikněte na ně a přetáhněte je mimo Clip Deck. Viz také [Uspořádání Clip Deck](clips/organising-your-clip-deck.md)

#### Jak vybrat více položek, mazat, slučovat Clip Decks atd.?

Viz [Uspořádání Clip Deck](clips/organising-your-clip-deck.md)

#### Co znamená malý symbol mikrofonu a další ikony na Clip?

Ukazují, že Clip přijímá zvukový nebo MIDI vstup, a tři tečky znamenají, že je nastavené zpoždění zone. Viz [Co znamenají malé ikony na tlačítkách Clip](clips/what-are-the-small-icons-on-the-clip-buttons.md)
