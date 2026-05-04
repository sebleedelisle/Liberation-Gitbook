---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/loading-and-saving
---

# 🟩 Načítání a ukládání

Liberation průběžně ukládá svůj stav na disk, takže pokud dojde k výpadku napájení nebo problému se systémem, spustí se přesně tam, kde skončil. Neměli byste tak nikdy přijít o své zones, časové osy ani další obsah.

Své nastavení ale můžete exportovat pro zálohování nebo přenos do jiného počítače.

### Import/export projektu

Soubor projektu ukládá téměř vše z aktuálního nastavení, včetně:

* Všeho uvedeného níže v části [Načítání a ukládání](loading-and-saving.md#laser-settings-import-export "mention")
* Clips, efektů a nastavení skupin
* Všech vašich časových os (bez zvukových a video médií)
* Nastavení Art-Net
* Nastavení odesílání/příjmu MIDI
* Nastavení tempa / synchronizace

V současnosti neukládá ani nenačítá:

* Nastavení zvukového a MIDI vstupu používaná v MIDI notes node a v Sound Input Oscillator (nastavení odesílání/příjmu MIDI i zvukový vstup pro timecode se _ukládají_)
* Škálování rozhraní
* Média pro vodicí obrázky Canvas
* Zvuková a video média pro časové osy
* Fonty použité v Text node

{% hint style="danger" %}
Zvukové a video soubory v časové ose se neukládají do souborů projektu, proto je při přenosu do jiného počítače nezapomeňte uložit samostatně. Viz [Důležitá poznámka k mediálním souborům časové osy](loading-and-saving.md#important-note-about-timeline-media-files "mention")
{% endhint %}

### Import/export Laser Settings

* Laser Settings pro každý laser
* Beam zones
* Cílové oblasti Canvas
* DMX zones
* Přiřazení laser controller (a aliasy pro všechny controller, které jste přejmenovali)
* Nastavení a předvolby kalibrace skeneru laseru a barev
* Nastavení a předvolby 3D vizualizéru

### Import/export Clip Deck

* Všechny Clips a jejich přiřazení k zones, nastavení a parametry
* Všechna nastavení skupin, flash mode, časy fade in/out atd.

V současnosti neukládá ani nenačítá:

* Všechny efekty a jejich parametry a nastavení

{% hint style="info" %}
**Načtení Clips ze souboru projektu bez načtení celého projektu**

Pokud chcete z projektu importovat pouze Clips, vyberte _**Clips->Import Clip Deck**_ a místo souboru Clip Deck (.cpdk) zvolte soubor projektu.
{% endhint %}

### Připojení Clip Deck

Pomocí _Append Clip Deck_ můžete do aktuálního projektu přidat Clips z exportovaného souboru Clip Deck. Clips se přidají na konec aktuálního Clip Deck, ale efekty a nastavení skupin ze souboru se neimportují.

### Export vybraných Clips

Všechny aktuálně vybrané Clips se exportují do souboru. Nastavení skupin a efekty se neuloží, uloží se pouze Clips. Pozor: aktuálně spuštěné aktivní Clips se neexportují, pokud zároveň nejsou vybrané.

{% hint style="info" %}
Clips vyberete pomocí Option/Alt - Shift - kliknutí (nebo použijte laso). Vybrané Clips poznáte podle silného bílého obrysu kolem nich. Viz [Spouštění a zastavování Clips](clips/starting-stopping-clips.md "mention")
{% endhint %}

### Import/export efektů

Načítá a ukládá všechny efekty včetně jejich nastavení skupin a parametrů.

{% hint style="info" %}
**Načtení efektů ze souboru projektu bez načtení celého projektu**

Pokud chcete z projektu importovat pouze efekty, vyberte _**Effects->Import Effects**_ a místo souboru efektů (.efts) zvolte soubor projektu.
{% endhint %}

### Export časové osy

Exportuje soubor časové osy s jednou nebo více časovými osami. Upozorňujeme, že Clip Deck je vždy součástí exportovaných souborů časové osy (i když při zpětném importu můžete vybrat, které Clips chcete importovat; viz níže [Import časové osy](loading-and-saving.md#timeline-import "mention")).

Pokud máte v souboru projektu více než jednu časovou osu, otevře se panel, ve kterém můžete vybrat, které časové osy chcete exportovat.

{% hint style="danger" %}
Zvukové a video soubory v časové ose se neukládají do souborů časové osy, proto je při přenosu obsahu do jiného počítače nezapomeňte uložit samostatně. Viz [Důležitá poznámka k mediálním souborům časové osy](loading-and-saving.md#important-note-about-timeline-media-files "mention")
{% endhint %}

### Import časové osy

Importuje jednu nebo více časových os z jednoho souboru časové osy. Po výběru souboru časové osy se otevře panel s několika možnostmi importu.

Pokud soubor časové osy obsahuje více než jednu časovou osu, zobrazí se všechny v seznamu. Zaškrtněte ty, které chcete zahrnout.

* Replace existing timelines\
  Odstraní všechny aktuální časové osy a nahradí je importovanými
* Import used clips only\
  Importuje pouze použité Clips a uspořádá je do skupin, jednu pro každou časovou osu. Pokud tato možnost není vybraná, celý Clip Deck ze souboru časové osy se připojí k vašim stávajícím Clips.
* Replace existing clip deck\
  Nahradí aktuální Clip Deck pomocí Clips ze souboru časové osy. Dostupné pouze v případě, že je vybraná možnost _Replace existing timelines_.

{% hint style="info" %}
**Načtení časových os ze souboru projektu bez načtení celého projektu**

Pokud chcete z projektu importovat pouze časové osy, vyberte _**Timeline->Import Timeline(s)**_ a místo souboru časové osy (.ltml) zvolte soubor projektu.
{% endhint %}

### Import/export DMX / Art-Net

Ukládá a načítá Art-Net nodes včetně jejich IP adres. Zahrnuje také DMX zones a všechny vaše DMX předvolby.

### Důležitá poznámka k mediálním souborům časové osy

Zvukové a video soubory se v současnosti **neexportují** společně se souborem časové osy, takže pokud potřebujete přesunout obsah do jiného počítače, nezapomeňte je zahrnout.

{% hint style="info" %}
**Jak časová osa vyhledává mediální soubory**

Při načtení časové osy se budou soubory hledat ve stejné složce jako soubor časové osy (nebo projektu) a také ve všech jejích podsložkách. Pokud tedy soubory jsou ve stejné složce nebo v některé podsložce (například _/videos_ nebo _/sound_), při načítání se najdou.
{% endhint %}
