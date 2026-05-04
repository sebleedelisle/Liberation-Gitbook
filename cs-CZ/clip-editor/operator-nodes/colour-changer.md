---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clip-editor/operator-nodes/colour-changer
---

# 🟩 Colour change

## <img src="../../.gitbook/assets/image.png" alt="" data-size="line"> Colour change

Mění barvy veškerého příchozího obsahu. Můžete buď nastavit pevné hodnoty HSB, nebo přepnout na systém gradientu a vzorkovat barvy z vlastního gradientu.

* **hue, saturation, brightness** - hodnoty barvy, viz [Nastavení barev a HSB](../fundamentals/colour-settings-and-hsb.md "mention")
* **hue mode** -
  * OFF - odstín se nemění
  * FIXED - odstín prvků se nastaví na hodnotu hue
  * SHIFT - odstín prvků se posune o danou hodnotu, takže různě barevné prvky zůstanou navzájem odlišné, jen se posunou po hodnotě odstínu.
* **saturation mode** -
  * OFF - sytost se nemění
  * FIXED - sytost se pevně nastaví na zadanou hodnotu.
* **brightness mode** -
  * OFF - jas se nemění
  * FIXED - jas prvků se nastaví na hodnotu brightness
  * MULTIPLY - jas prvků se zkombinuje s hodnotou brightness, takže pokud blikají, budou blikat dál, ale jen do zde zadaného jasu.
* **gradient mode** – přepne z pevných posuvníků HSB do editoru gradientu. node vzorkuje jednu barvu z gradientu a potom ji aplikuje pomocí výše uvedených režimů odstínu, sytosti a jasu.
* **gradient position** – určuje, který bod gradientu se vzorkuje. Animujte tuto hodnotu od 0 % do 100 % pomocí Sawtooth Oscillator, aby barva v čase procházela gradientem.
* **blend** - jak silně se změna barvy použije; 0 % znamená vůbec, 100 % plně a 50 % kombinaci stávající barvy a nových hodnot.

{% hint style="info" %}
node Colour Change vzorkuje jednu barvu z gradientu pro celý vstup. Pokud chcete, aby gradient probíhal napříč tvarem podle pozice, použijte místo toho [měniče založené na pozici](position-based-changers.md "mention").
{% endhint %}

### Editor gradientu

Když je zapnutý **gradient mode**, pod hlavními ovládacími prvky se zobrazí editor gradientu.

* Kliknutím na pruh gradientu přidáte barevnou zarážku.
* Levým kliknutím zarážku vyberte a tažením do strany ji přesuňte.
* Vybranou zarážku odstraníte tak, že ji přetáhnete dolů pryč od pruhu nebo stisknete Delete/Backspace. Gradient vždy zachová alespoň dvě zarážky.
* Pravým kliknutím na zarážku ji upravíte pomocí výběru barvy.
* Pomocí **Position**, **Hue**, **Saturation** a **Brightness** můžete vybranou zarážku přesně upravit.
* **interpolation** určuje, jak se barvy mezi zarážkami prolínají:
* **HSB** – prolíná odstín, sytost a jas. Hodí se nejlépe pro plynulý duhový pohyb po barevném kruhu.
* **RGB** – přímo prolíná hodnoty červené, zelené a modré. Často působí spíše jako barevný přechod na obrazovce nebo osvětlovacím pultu.
* **NONE** – přeskakuje z jedné zarážky na další bez prolínání.
* **hue direction** je k dispozici při interpolaci HSB:
* **AUTO** – zvolí nejkratší cestu po kruhu odstínu.
* **FORWARDS** – vždy postupuje dopředu hodnotami odstínu.
* **BACKWARDS** – vždy postupuje dozadu hodnotami odstínu.
