---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clips/global-settings
---

# 🟩 Globální transformace

Kromě transformací pro jednotlivé Clips (shift x/y, scale x/y) jsou k dispozici také Global Transformations, které se použijí na každý spuštěný Clip. Otevřete panel _Global Transformations_, kde je najdete. (Tento panel je obvykle na kartě vedle _Clip Settings_.)

Ve výchozím nastavení se všechna tato nastavení resetují, jakmile už není spuštěný žádný Clip. Toto automatické resetování můžete vypnout tlačítkem _AUTO RESET_ ve spodní části panelu _Global Transformations_.

{% hint style="info" %}
Global Transformations neovlivňují nic v Canvas, pouze beam zone a DMX zone.
{% endhint %}

### Scale X/Y

Vodorovné a svislé měřítko. Tyto hodnoty jsou vzájemně svázané, pokud nestisknete `Shift`. Ve výchozím nastavení jsou také namapované na ovladače APC40 Device Control 4 a 8 a zobrazují se v panelu napravo od Clip Deck.

### Shift X/Y

Vodorovný a svislý posun. Posune vše vodorovně / svisle.

### Spin

Otáčí veškerý obsah kolem středu. Kladná hodnota otáčí po směru hodinových ručiček, záporná hodnota proti směru hodinových ručiček. Uvidíte, že toto nastavení ovlivňuje transformaci _Rotation_. Ve výchozím nastavení je namapované na ovladač APC40 Device Control 3 a zobrazuje se v panelu napravo od Clip Deck.

### Spin 3D

Otáčí veškerý obsah kolem osy Y (svislá čára uprostřed). Uvidíte, že toto nastavení ovlivňuje transformaci _Rotation3D_. Ve výchozím nastavení je namapované na ovladač APC40 Device Control 7 a zobrazuje se v panelu napravo od Clip Deck.

### Rotation

Otočení kolem středu, hodnota ve stupních.

### Rotation 3D

Otočení kolem osy Y (svislá čára uprostřed), hodnota ve stupních.

### Auto reset

Když je zapnuté, resetuje všechny Global Transformations, jakmile se deaktivují všechny aktuálně spuštěné Clips. Díky tomu máte jistotu, že vás při příštím spuštění Clip nic nepřekvapí!
