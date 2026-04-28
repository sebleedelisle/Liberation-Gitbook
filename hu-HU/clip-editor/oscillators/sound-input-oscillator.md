---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clip-editor/oscillators/sound-input-oscillator
---

# ✅ Sound input oszcillátor

## <img src="../../.gitbook/assets/sound-input-icon.png" alt="" data-size="line"> Sound input

A hangbemenet szintjét tulajdonságértékké alakítja.

{% hint style="info" %}
A Sound input oszcillátor az alapértelmezett hanginterfészt használja, de ezt a _Preferences_ részben módosíthatod. Nyisd meg a _Liberation -> Preferences_ menüt.

A _Sound Input_ beállításoknál kiválaszthatod, melyik hanginterfészt szeretnéd használni, valamint néhány további beállítással módosíthatod a hangerőszint kezelését.
{% endhint %}

* **range min / range max** - azok a minimum- és maximumértékek, amelyekre a hullámforma leképeződik
* **channel** - ha a hanginterfészednek egynél több bemeneti csatornája van, itt választhatod ki, melyiket szeretnéd használni.

{% hint style="info" %}
Jó technika, ha több hangjelet kapsz a keverőpultból; így különböző klipek különböző hangszerekre reagálhatnak.
{% endhint %}

{% hint style="info" %}
Az összes _Sound Input_ esetén egyszerre csak egy hanginterfészt használhatsz (az _App Settings_ panelen kiválasztva). Ha ehhez egynél több interfészt szeretnél használni, macOS-en [létrehozhatsz egy Aggregate Device eszközt](https://support.apple.com/en-gb/HT202000), amellyel a bemeneteket egyetlen virtuális hangforrássá vonhatod össze. (Windowsra is sok alkalmazás létezik erre, de ezeket nem próbáltam.)
{% endhint %}

* **clamp min / clamp max** - ezzel választhatod ki, melyik szinttartományra szeretnél reagálni. Ezt általában nem kell módosítanod, ha a gate és limit beállítások (az _App Settings_ panelen) megfelelően vannak beállítva, de kreatív effektekhez hasznos lehet.

{% hint style="info" %}
A clip gombján egy kis mikrofon ikon jelenik meg, amikor _Sound Input_ oszcillátor van rajta.

<img src="../../.gitbook/assets/image (8).png" alt="" data-size="original">
{% endhint %}
