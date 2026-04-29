---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clip-editor/fundamentals/colour-settings-and-hsb
---

# 🟩 Nastavení barev a HSB

Barva je v Liberation definována jako HSB, ne jako RGB. Možná vám to nebude hned známé, ale jakmile si na tento systém zvyknete, je podle mě mnohem intuitivnější.

{% hint style="info" %}
Pokud raději používáte RGB, můžete v libovolném nastavení barvy kliknout na barevný čtverec. Otevře se panel editoru barev, který nabízí možnosti pro RGB i HSB.
{% endhint %}

### HSB – Hue, Saturation a Brightness

#### Hue

Odstín barvy má rozsah 0 až 255. Hodnota 0 je červená a při zvyšování hodnoty postupně projdete všemi odstíny duhy: oranžovou, žlutou, zelenou, azurovou, modrou, fialovou, purpurovou a na hodnotě 255 zpět k červené.

Protože jde o smyčku, můžete pomocí trojúhelníkové vlny cyklovat přes všechny barvy.

#### Saturation

Toto nastavení upravuje sytost neboli výraznost barvy. Jinými slovy určuje, jak moc je barva _barevná_, a má rozsah 0 až 255. Nastavením Saturation na 0 získáte odstíny šedé, při hodnotě 255 plné duhové barvy. Hodnoty někde uprostřed vytvoří pastelové, vybledlejší barvy.

{% hint style="info" %}
Omlouvám se americkým přátelům za nadbytečnou samohlásku v anglickém slově colour. Liberation vzniká v Anglii, takže výchozí je britská angličtina. Do budoucna doufám, že nabídnu překlady do francouzštiny, španělštiny, němčiny, italštiny, zjednodušené čínštiny a ano, dokonce i do americké angličtiny. :innocent:
{% endhint %}

#### Brightness

Pravděpodobně nejjednodušší položka k pochopení: 0 znamená úplně černou, 255 plný jas.

### Příklady použití

#### Duhový cyklus:

Nastavte _Brightness_ a _Saturation_ na 255. Připojte oscilátor _Sawtooth_ ke vstupu _Hue_ a upravte jeho rozsah od 0 do 255.

#### Pulzující jas:

Připojte oscilátor _Sawtooth_ ke vstupu _Brightness_ a upravte jeho rozsah od 255 do 0. Dále můžete upravit minimální a maximální hodnotu clamp, abyste řídili dobu trvání změny. Potom pomocí easing funkcí animaci ještě doladíte.

#### Tvrdý záblesk / stroboskop:

Vyberte barvu pomocí _Hue_ a _Saturation_ nebo kliknutím na výběr barvy. Připojte oscilátor _Square Wave_ ke vstupu _Brightness_ a upravte jeho rozsah od 255 do 0.

#### Cyklus přes vlastní rozsah odstínů:

Nastavte _Brightness_ a _Saturation_ na 255. Připojte oscilátor _Triangle Wave_ ke vstupu _Hue_ a upravte jeho rozsah:

* pro modrou až azurovou použijte rozsah 70 až 128
* pro červenou až žlutou použijte rozsah 0 až 40
* pro červenou až purpurovou použijte rozsah 255 až 220
