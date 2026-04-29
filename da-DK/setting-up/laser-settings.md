---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/setting-up/laser-settings
---

# ✅ Panelet Laser output settings

Åbn indstillingspanelet _Laser output_ via menuen _View -> Laser Output Settings._

<figure><img src="../.gitbook/assets/Copy Laser Setting in Laser Output.png" alt="" width="326"><figcaption></figcaption></figure>

Dette viser indstillingerne for den aktuelt valgte laser, som du kan ændre:

* via dens nummerknap i panelet _Laser overview_
* med en taltast på dit tastatur; tasterne 1 til 0 åbner laser 1-10
* med tasten `Tab` for at skifte gennem laserne (`Shift + Tab` går baglæns).

Øverst i panelet ser du:

* en nummerknap – klik på den for at aktivere/deaktivere denne laser. Den er rød, når laseren er aktiveret.
* en _Brightness_-skyder kun for denne laser. Bemærk, at den kombineres med den globale lysstyrke.
* _Test Pattern_-til/fra-knap og mønstervælger. Her kan du vælge et bestemt testmønster kun for denne laser. (Disse kontroller spejles i værktøjslinjen i Output-visningen).

### Outputretning / korrektion af spejling

De næste elementer bruges til at korrigere opsætningen af din laser, så den opfører sig ensartet i Liberation.

* **Flip horizontal / vertical** – disse indstillinger giver dig mulighed for at korrigere laserens output

{% hint style="info" %}
Du bør ikke have brug for at ændre indstillingerne for horizontal / vertical flip, medmindre din laser er forkert forbundet, eller den har X/Y flip-knapper på bagsiden, som ikke er indstillet korrekt. Hvis du vil have output spejlvendt for en bestemt clip, kan det gøres på selve clippet.
{% endhint %}

* **Orientation** – hvis din laser er monteret på siden eller på hovedet, kan du korrigere rotationen med denne indstilling.
* **Fine position adjustments** – kan bruges til at korrigere meget små forskydninger/rotationer. Beregnet til at rette drift/sætning, hvis en laser har stået natten over eller i længere perioder.

{% hint style="info" %}
Bemærk, at korrektioner af orientation / mirroring ikke ændrer noget i 3D Visualiser. De skal bruges til at korrigere outputtet fra den fysiske laser, så det matcher det, der vises i 3D Visualiser!
{% endhint %}

### Kopiér laserindstillinger

Se [Panelet Laser output settings](laser-settings.md#copy-laser-settings "mention").

### Scannerindstillinger

<figure><img src="../.gitbook/assets/Laser output scanner settings.png" alt=""><figcaption></figcaption></figure>

#### **Speed**

Indstillingen speed bestemmer, hvor hurtigt scannerne bevæger sig.

{% hint style="danger" %}
Selvom standardindstillingerne er ret konservative, kan du stadig beskadige dine scannere, hvis du kører dem for hurtigt. Vær forsigtig, især når du øger hastigheden.
{% endhint %}

{% hint style="info" %}
Denne speed-indstilling ændrer ikke point rate. I stedet justerer den, hvor spredt punkterne er placeret. Se [◼️ Sådan genererer Liberation laserindhold](../advanced/how-liberation-generates-laser-content.md "mention") for mere information.
{% endhint %}

#### **Scanner sync (Colour shift / blank shift)**

Strålen skifter farve og tændes/slukkes, mens scannerne flytter den rundt, og de to ting er normalt ikke helt synkroniserede. Justér denne indstilling for at få dem på linje igen.

{% hint style="info" %}
Dette kaldes nogle gange _blank shift_, men jeg foretrækker selv betegnelsen _scanner sync_ – den er lidt mere præcis, fordi den justerer timingen for alle farveskift i forhold til scannerbevægelsen.
{% endhint %}

<div><figure><img src="../.gitbook/assets/Colour shift tails.jpeg" alt="" width="320"><figcaption><p>Laser-"haler" – Colour shift er ikke indstillet korrekt</p></figcaption></figure> <figure><img src="../.gitbook/assets/Colour shift no tails.jpeg" alt="" width="320"><figcaption><p>Ingen laser-"haler"! Colour shift er god!</p></figcaption></figure></div>

Hvis du ser små "haler" på laseroutputtet, skyldes det sandsynligvis, at scanner sync skal justeres. Hvis halerne stadig vises uanset hvad, kører du sandsynligvis dine scannere/laserdrivere hurtigere, end de kan håndtere. Prøv at sænke scannerhastigheden.

#### Scanner presets

Brug dette til at vælge en foruddesignet scannerindstilling. Standardindstillingen er normalt fin, så du bør ikke have brug for at ændre den, medmindre du har særligt dårlige (eller gode) scannere. Hvis du vil gå mere i dybden, se [◼️ Scanner-presets og render-profiler](../advanced/scanner-presets.md "mention")

#### Colour calibration

Du kan bruge dette system til at korrigere laserens lysstyrkekurve og hvidbalance. Se [Farvekalibrering](../advanced/colour-calibration.md "mention")

#### Advanced settings

Du bør ikke have brug for at rode med disse, men hvis du er nysgerrig, se [◼️ Avancerede laserindstillinger](../advanced/advanced-laser-settings.md "mention")
