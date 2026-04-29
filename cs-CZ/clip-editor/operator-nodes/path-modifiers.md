---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clip-editor/operator-nodes/path-modifiers
---

# 🟩 Modifikátory cest

## &#x20;Dotter

Tento node nahrazuje obsah tvořený čarami a tvary rovnoměrně rozmístěnými tečkami (existující tečky zůstanou beze změny).

* **Colour** – barva teček. Ignoruje se, pokud je zapnuté _Inherit Colour_, viz níže. _Viz také_ [Nastavení barev a HSB](../fundamentals/colour-settings-and-hsb.md)
* **Spacing** – vzdálenost mezi tečkami, měřená v pixelech. Menší hodnoty = více teček, větší hodnoty = méně teček.
* **Offset** – posouvá počáteční pozici teček jako procento hodnoty spacing. Lze animovat (např. pomocí Oscillator Node s pilovým průběhem) a vytvářet tak efekty „putujících“ teček.
* **Keep Original** – pokud je zapnuté, původní čáry/tvary zůstanou zachované a tečky se vykreslí přes ně.
* **Render Profile** – vybírá kvalitu vykreslování. _Viz_ [Render Profile](../fundamentals/render-profile.md)
* **Length Auto Divisible by Spacing** – automaticky upraví spacing tak, aby se délka cesty dělila rovnoměrně.
* **Fade Out Ends** – postupně snižuje jas teček směrem k začátku a konci cesty. Hodí se při animování **Offset** pomocí Oscillator Node s pilovým průběhem, aby tečky při pohybu ke konci tvaru plynule mizely a objevovaly se.

## &#x20;Trimmer

Tento node ořezává viditelnou délku čar a tvarů, takže je můžete v čase odhalovat, skrývat nebo animovat.

* **Offset** – určuje, kde začíná viditelná část tvaru. I když je _Trim Size_ nastavené na 0 %, animace Offset od 0 % → 100 % způsobí, že se tvar vykreslí, při 50 % bude plně viditelný a poté znovu zmizí.
* **Trim Size** – nastavuje, jak velká část tvaru zůstane zachovaná, jako procento jeho celkové délky.
* **Loop** – bere tvar jako souvislou smyčku, takže konec se napojí zpět na začátek místo toho, aby zmizel.
* **All Shapes** – spojí všechny vstupní tvary a ořízne je, jako by šlo o jednu cestu. Pokud je vypnuté, každý tvar se ořízne samostatně.
* **Add Dot at Start / Add Dot at End** – přidá tečku zvolené barvy do bodů ořezu. (Pokud není použitý žádný ořez, žádné tečky se nepřidají.)
* **Colour** – barva teček v bodech ořezu. _Viz také_ [Nastavení barev a HSB](../fundamentals/colour-settings-and-hsb.md)
* **Render Profile** – vybírá render profile pro tečky. _Viz_ [Render Profile](../fundamentals/render-profile.md)
