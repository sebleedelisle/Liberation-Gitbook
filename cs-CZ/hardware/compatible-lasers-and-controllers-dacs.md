---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/hardware/compatible-lasers-and-controllers-dacs
---

# ✅ Kompatibilní lasery a kontrolery (DAC)

### Které lasery jsou kompatibilní s Liberation?

Pokud má váš laser standardní ILDA vstup, můžete ho s Liberation používat spolu s kompatibilním laserovým kontrolerem, například Ether Dream nebo Helios DAC – [viz úplný seznam níže](compatible-lasers-and-controllers-dacs.md#compatible-laser-controllers).

<figure><img src="../.gitbook/assets/helios-dac.png" alt="" width="563"><figcaption><p>Helios DAC – nejlevnější volba pro domácí použití</p></figcaption></figure>

Externí kontroler ani ILDA vstup nepotřebujete, pokud:

* má váš laser uvnitř nainstalovaný Ether Dream, nebo;
* máte LaserCube od Wicked Lasers, nebo;
* máte zařízení X-Laser s vestavěným Mercury, nebo;
* máte laser Laser Animation Sollinger s vestavěným AVB kontrolerem (aktuálně se testuje pouze na macOS)

{% hint style="info" %}
**Co je laserový kontroler?**

Laserový kontroler, tedy DAC, je hardwarové zařízení, které převádí digitální data z Liberation na analogové signály potřebné k řízení skenerů a výstupu laseru. Odtud název DAC: Digital to Analog Converter, tedy digitálně-analogový převodník.

Kontroler se k počítači připojuje přes USB nebo přes běžnou počítačovou síť. Může jít o externí zařízení, nebo může být zabudovaný přímo v laseru.

Pokud je externí, připojíte ho k laseru přes ILDA konektor. ILDA je oborový standard, který používá starší 25pinový konektor typu „D“. Pořiďte si ILDA kabel, jeden konec zapojte do kontroleru a druhý do laseru.
{% endhint %}

<figure><img src="../.gitbook/assets/etherdream-ilda.png" alt="" width="375"><figcaption><p>ILDA výstup na externím Ether Dream</p></figcaption></figure>

<figure><img src="../.gitbook/assets/opt-laser-rear.jpg" alt="" width="317"><figcaption><p>Zadní panel laseru s různými konektory včetně ILDA vstupu</p></figcaption></figure>

<figure><img src="../.gitbook/assets/ilda-cable.jpg" alt="" width="375"><figcaption><p>Standardní ILDA kabel</p></figcaption></figure>

### Který kontroler je pro mě nejlepší?

Pokud používáte lasery doma nebo provozujete menší show s maximálně 4 lasery umístěnými blízko počítače, jsou USB kontrolery, například **Helios DAC**, **nejdostupnější** volbou.

Síťové DAC, například **Ether Dream**, jsou **nejlepší volbou pro profesionální** laserové operátory, kterým nevadí nastavit síť a chtějí provozovat větší počet laserů. Všechny velké show v Liberation dosud běžely na Ether Dream.

Pokud máte **LaserCube**, samostatný laserový kontroler vůbec nepotřebujete – Liberation je kompatibilní se všemi LaserCube. Starší modely se připojují USB kabelem, novější modely přes síť.

Pokud jste profesionál a hledáte co nejjednodušší řešení, zvažte jednotky X-Laser s vestavěným Mercury nebo lasery Laser Animation Sollinger používající AVB.

### Kompatibilní laserové kontrolery

#### Ether Dream (síť)

[Ether Dream](https://ether-dream.com) je na trhu už více než deset let a aktuálně je ve verzi 4, i když Liberation funguje také s Ether Dream verze 1, 2 a 3. Jsou mimořádně spolehlivé.

Připojují se přes běžnou síť. Lze je koupit jako samostatné jednotky, nebo ještě lépe vestavět přímo do laserů.

#### Helios (USB)

[Helios](https://bitlasers.com/helios-laser-dac/) je nejlepší volba pro začátečníky a je levnější než Ether Dream. Protože se ale připojuje přes USB, nedoporučuje se pro dlouhá kabelová vedení. Jakmile připojíte více než 4 zařízení, mohou se také objevit problémy s USB daty a ovladači, zejména ve Windows.

Pokud ale chcete doma provozovat jen pár laserů, je to nejlevnější a nejjednodušší volba.

#### Mercury (vestavěné v jednotkách X-Laser)

[**Mercury**](https://x-laser.com/pages/mercury-laser-control-system) je výkonný systém X-Laser pro řízení laserů přes DMX, navržený pro světelné designéry, kteří chtějí ovládat lasery přímo z tradičního světelného pultu. S nejnovější aktualizací firmwaru Mercury obsahuje také **emulaci Ether Dream**, takže nyní bez problémů funguje s Liberation i s jakýmkoli dalším softwarem, který podporuje Ether Dream.

#### AVB (vestavěné v jednotkách Laser Animation Sollinger)

**AVB** je otevřený síťový protokol pro vysoce výkonné audio a datové streamování s nízkou latencí. Mnoho projektorů LaserAnimation Sollinger má podporu AVB přímo v hardwaru, takže se k nim Liberation může připojit po síti bez potřeby externích DAC. Podpora AVB v Liberation je aktuálně **pouze pro macOS a ve fázi testování** a vyžaduje **kompatibilní síťová zařízení s podporou AVB**. Při správném nastavení nabízí jednodušší workflow, méně externích zařízení a vysokou spolehlivost pro profesionální show.

#### Kontrolery, které budou podporovány v budoucnu:

* [IDN](http://www.ilda-digital.com) (otevřený síťový protokol od ILDA, který může implementovat libovolný výrobce)

### Doporučení ke kabeláži

Pro optimální výkon ponechte USB DAC blízko počítače a k laserům je připojte delšími ILDA kabely. Pozor ale: ILDA kabely se při demontáži umí chovat jako hák!

Pokud používáte Ether Dream, můžete je také ponechat všechny pohromadě a k laserům vést dlouhé ILDA kabely. Případně je můžete zavěsit blízko laserů a použít delší síťové kabely.

Ideální řešení je mít Ether Dream nebo jiné kontrolery nainstalované přímo uvnitř laserů. Ve Spojeném království vám to může udělat Rob ze Stanwax Laser.
