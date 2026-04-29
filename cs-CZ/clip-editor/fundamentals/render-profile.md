---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clip-editor/fundamentals/render-profile
---

# 🟩 Render Profile

V každém node typu _Creator_ je nastavení _Render Profile_, které určuje, jak se tvary pomocí laserů kreslí (neboli _renderují_).

**Pro většinu použití je nastavení&#x20;**_**DEFAULT**_**&#x20;zcela v pořádku**. Pokud ale pracujete s grafikou nebo složitým obsahem, může se vám hodit větší kontrola nad tím, jak se jednotlivé tvary renderují.

{% hint style="info" %}
Na rozdíl od většiny laserového softwaru Liberation generuje proud bodů v reálném čase, těsně před předáním do zařízení typu laser controller. Tím ušetří hodně místa na disku: Clips mají jen několik kB místo MB předrenderovaných proudů bodů.

Zároveň to znamená, že stejný obsah můžete doladit pro různé typy skenerů zvlášť pro každý laser, aniž byste museli měnit samotné Clips.

Další podrobnosti najdete v části [Jak Liberation generuje laserový obsah](../../advanced/how-liberation-generates-laser-content.md)
{% endhint %}

K dispozici jsou tři přednastavené _Render Profiles_: _DEFAULT_, _FAST_ a _DETAIL._

_**DEFAULT**_ – dobrý univerzální profil, nejlepší pro většinu použití

_**FAST** –_ pokud váš Clip obsahuje hodně prvků a část z nich jsou jen velmi jednoduché tečky a rovné čáry, může tato volba omezit blikání.

_**DETAIL**_ – tuto volbu použijte, když kreslíte něco, co potřebuje ostré rohy. Počítejte ale s tím, že se skenery budou pohybovat pomaleji a výstup tak bude více blikat.

{% hint style="info" %}
V rozhraní Clip Editor můžete jednotlivým Creators přiřadit různé Render Profiles, ale každý laser bude tyto profily zpracovávat podle svého nastavení skenerů. Viz [Předvolby skenerů](../../advanced/scanner-presets.md)
{% endhint %}
