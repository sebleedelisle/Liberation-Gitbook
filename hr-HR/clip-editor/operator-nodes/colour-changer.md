---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clip-editor/operator-nodes/colour-changer
---

# 🟩 Colour change

## <img src="../../.gitbook/assets/image.png" alt="" data-size="line"> Colour change

Mijenja boje cijelog dolaznog sadržaja. Možete postaviti fiksne HSB vrijednosti ili se prebaciti na sustav gradijenta i uzorkovati boje iz prilagođenog gradijenta.

* **hue, saturation, brightness** - vrijednosti boje, pogledajte [Postavke boje i HSB](../fundamentals/colour-settings-and-hsb.md "mention")
* **hue mode** -
  * OFF - nijansa se ne mijenja
  * FIXED - nijansa elemenata postavlja se na vrijednost hue
  * SHIFT - nijansa elemenata pomiče se za zadanu vrijednost, pa će elementi različitih boja ostati različiti, ali će se samo pomaknuti duž vrijednosti hue.
* **saturation mode** -
  * OFF - zasićenost se ne mijenja
  * FIXED - zasićenost se fiksira na zadanu vrijednost.
* **brightness mode** -
  * OFF - svjetlina se ne mijenja
  * FIXED - svjetlina elemenata postavlja se na vrijednost brightness
  * MULTIPLY - svjetlina elemenata kombinira se s vrijednošću brightness, pa će, ako bljeskaju, i dalje bljeskati, ali samo do ovdje zadane svjetline.
* **gradient mode** - prebacuje s fiksnih HSB klizača na uređivač gradijenta. Node uzorkuje jednu boju iz gradijenta, a zatim je primjenjuje pomoću gore navedenih načina za nijansu, zasićenost i svjetlinu.
* **gradient position** - odabire koja se točka u gradijentu uzorkuje. Animirajte ovo od 0% do 100% pomoću Sawtooth Oscillator kako biste tijekom vremena prolazili kroz gradijent.
* **blend** - koliko se snažno primjenjuje promjena boje; 0% znači nimalo, 100% potpuno, a 50% kombinaciju postojeće boje i novih vrijednosti.

{% hint style="info" %}
Node Colour Change uzorkuje jednu boju iz gradijenta za cijeli ulaz. Ako želite da se gradijent proteže preko oblika prema položaju, umjesto toga upotrijebite [mjenjače na temelju položaja](position-based-changers.md "mention").
{% endhint %}

### Uređivač gradijenta

Kada je **gradient mode** uključen, uređivač gradijenta pojavljuje se ispod glavnih kontrola.

* Kliknite traku gradijenta kako biste dodali zaustavnu točku boje.
* Kliknite lijevom tipkom zaustavnu točku kako biste je odabrali, zatim je povucite u stranu kako biste je pomaknuli.
* Povucite odabranu zaustavnu točku prema dolje, dalje od trake, ili pritisnite Delete/Backspace kako biste je uklonili. Gradijent uvijek zadržava najmanje dvije zaustavne točke.
* Kliknite zaustavnu točku desnom tipkom kako biste je uredili pomoću birača boje.
* Upotrijebite **Position**, **Hue**, **Saturation** i **Brightness** za precizno uređivanje odabrane zaustavne točke.
* **interpolation** odabire kako se boje miješaju između zaustavnih točaka:
* **HSB** - miješa nijansu, zasićenost i svjetlinu. To je najbolje za glatko kretanje u stilu duge oko kotača boja.
* **RGB** - izravno miješa vrijednosti crvene, zelene i plave. To često više nalikuje prijelazu boja na zaslonu ili rasvjetnoj konzoli.
* **NONE** - skače s jedne zaustavne točke na sljedeću, bez miješanja.
* **hue direction** dostupno je kod HSB interpolacije:
* **AUTO** - uzima najkraći put oko kotača nijansi.
* **FORWARDS** - uvijek se kreće prema naprijed kroz vrijednosti nijanse.
* **BACKWARDS** - uvijek se kreće prema natrag kroz vrijednosti nijanse.
