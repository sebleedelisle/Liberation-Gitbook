---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/timecode
---

# ✅ Timecode

Liberation podporuje synchronizaci s externím signálem časového kódu SMPTE/LTC, který se běžně používá u živých hudebních show k časovému sladění světel, pyrotechniky, videa a doprovodných audio stop.

{% hint style="info" %}
Co je SMPTE/LTC?

SMPTE je standard pro časový kód a LTC je tento časový kód převedený na audio signál. Když si tento zvuk pustíte, zní jako nepříjemné vysoké pískání, ale pro počítače jde o časovou informaci s vysokým rozlišením.

**Něco pro technické nadšence!**

Historicky se SMPTE používá k synchronizaci videa a zvuku. Při synchronizaci s analogovým páskem se někdy jedna stopa nahrála jako audio časového kódu, čemuž se říkalo „striping“ pásku. Tuto stopu s časovým kódem pak bylo možné použít k synchronizaci více páskových přehrávačů mezi sebou nebo k udržení MIDI sekvenceru v čase s páskem. (Takže jste nemuseli nahrávat MIDI nástroje na pásek – sekvencer je mohl přehrávat živě během mixu!)

SMPTE znamená Society of Motion Picture and Television Engineers, tedy organizaci, která tento standard definovala. LTC znamená _Linear TimeCode._
{% endhint %}

Signál časového kódu LTC můžete přijímat přes libovolné zvukové rozhraní v počítači, ale doporučujeme použít profesionální rozhraní alespoň s jedním nastavitelným XLR vstupem a možností monitoringu.

Dobré zkušenosti mám s [M-Audio 192/6](https://www.m-audio.com/audio-midi-interfaces/air-192-6.html), protože má sluchátkový monitoring, 2 XLR vstupy a nepotřebuje žádné speciální ovladače (alespoň na macOS). Pokud ho budete používat jen pro timecode, můžete zvolit o něco levnější [M-Audio 192/4](https://www.m-audio.com/audio-midi-interfaces/air-192-4.html) (má jen jeden vstup a nemá MIDI), ale upřímně řečeno by mělo fungovat jakékoli slušné zvukové rozhraní.

{% hint style="info" %}
Signály časového kódu LTC se typicky vedou po symetrických XLR kabelech, protože jsou dostatečně odolné pro přenos nízkoúrovňových audio signálů na dlouhé vzdálenosti. (XLR je kulatý konektor obvykle používaný u mikrofonů.)
{% endhint %}

### Hardwarové připojení

Zapojte XLR kabel se signálem časového kódu do zvukového rozhraní a ověřte, že přijímáte kvalitní signál. Nastavte úroveň na zvukovém rozhraní tak, aby byl signál silný, ale nepřebuzoval se. Pokud má vaše zvukové rozhraní sluchátkový výstup, můžete si timecode poslechnout a zkontrolovat, že nevypadává a není v něm příliš mnoho šumu.

{% hint style="info" %}
Teoreticky je možné přijímat signál přes jack konektor na MacBooku, ale vyžadovalo by to vlastní kabel. Tyto konektory jsou obvykle 4pólové TRRS mini jacky a upřímně si nejsem jistý, které z těchto kontaktů lze použít jako audio vstup. Také si nejsem jistý, jakou napěťovou úroveň zvládnou (někde jsem četl, že to bylo +/-1 V, ale použití je na vlastní riziko!).

Myslím, že bude lepší pořídit si levné USB zvukové rozhraní, než se pokoušet o toto řešení.
{% endhint %}

Pokud vaše zvukové rozhraní nemá žádný vstupní monitoring, můžete v systémových nastaveních macOS (v části _Sound_) zkontrolovat, že signál opravdu přichází. (Ve Windows použijte _Sound Control Panel_.)

<figure><img src=".gitbook/assets/mac-mic-input-volume.png" alt=""><figcaption><p>macOS zobrazuje vstupní úroveň libovolného zvukového rozhraní v panelu systémových nastavení Sound</p></figcaption></figure>

### Nastavení v Liberation

1. V okně nastavení Timecode vyberte své zvukové rozhraní a správný vstupní kanál.

![](.gitbook/assets/timecode-panel.png)

{% hint style="info" %}
Všimněte si, že v rozbalovací nabídce jsou samostatné volby pro každý vstupní kanál vašeho zvukového rozhraní.

<img src=".gitbook/assets/m-audio.png" alt="" data-size="original">
{% endhint %}

Všimněte si čtverce vlevo: pokud přijímáte platný signál časového kódu, zezelená. Pokud ne, bude červený.

2. Vyberte správnou snímkovou frekvenci pro příchozí timecode. Ten, kdo vám timecode poskytuje, by vám měl říct, jaká je snímková frekvence. (Pokud ji nastavíte špatně, synchronizace bude stále fungovat, ale každou sekundu si všimnete malého „přeskočení“.)
3. Otevřete nastavení timecode pro Timeline pomocí malé ikony hodin na liště Timeline a zvolte možnost SMPTE(LTC).

<figure><img src=".gitbook/assets/timeline-settings.png" alt=""><figcaption></figcaption></figure>

4. Nastavte počáteční posun (v hodinách, minutách, sekundách a snímcích) tak, aby odpovídal začátku skladby. Pokud máte více timelines, musíte tyto volby nastavit pro každou zvlášť.

{% hint style="info" %}
Ve světě touringových produkcí je běžnou konvencí, že každá skladba začíná v jiné hodině, například 01:00:00:00 pro první skladbu, 02:00:00:00 pro druhou skladbu a tak dále.

Liberation se podle timecode automaticky přepne na příslušnou timeline, takže během show nemusíte timelines ručně měnit.
{% endhint %}

Na rozdíl od MIDI Clock a Ableton Link je SMPTE _absolutní_ časový systém, měřený v hodinách, minutách, sekundách a snímcích. Základní časový systém v Liberation je založený na beatech a taktech, takže při příjmu timecode se použije tempo nastavené v timeline. Musíte zajistit, aby toto tempo bylo synchronní s hudbou, která je také synchronizovaná na timecode.
