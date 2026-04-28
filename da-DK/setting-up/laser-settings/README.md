# ✅ Indstillingspanelet Laser output

Åbn indstillingspanelet _Laser output_ via menuen _View -> Laser Output Settings._

<figure><img src="../../.gitbook/assets/Copy Laser Setting in Laser Output.png" alt="" width="326"><figcaption></figcaption></figure>

Det viser indstillingerne for den aktuelt valgte laser, som du kan ændre:

* via dens nummerknap i panelet _Laser overview_
* med en nummertast på tastaturet, hvor tasterne 1 til 0 åbner laser 1-10
* med tasten `Tab` for at skifte gennem laserne (`Shift + Tab` går baglæns).

Øverst i dette panel ser du:

* en nummerknap – klik på den for at armere/desarmere denne laser. Den er rød, når laseren er armeret.
* en _Brightness_-skyder kun for denne laser. Bemærk, at den kombineres med den globale lysstyrke.
* _Test Pattern_-til/fra-knap og mønstervælger. Her kan du vælge et bestemt testmønster kun for denne laser. (Disse kontroller spejles i værktøjslinjen i Output-visningen).

### Output-orientering / korrektion af spejling

De næste elementer bruges til at korrigere opsætningen af din laser, så den opfører sig konsekvent i Liberation.

* **Flip horizontal / vertical** – disse indstillinger giver dig mulighed for at korrigere laserens output

{% hint style="info" %}
Du bør ikke have brug for at ændre indstillingerne for horizontal / vertical flip, medmindre din laser er forkert forbundet, eller den har X/Y flip-knapper på bagsiden, som ikke er indstillet korrekt. Hvis du vil have output spejlvendt for et bestemt clip, kan det gøres på selve clippet.
{% endhint %}

* **Orientation** – hvis din laser er monteret på siden eller på hovedet, kan du korrigere rotationen med denne indstilling.
* **Fine position adjustments** – kan bruges til at korrigere meget små forskydninger/rotationer. Beregnet til at korrigere drift/sætning, hvis en laser har stået natten over eller i længere tid.

{% hint style="info" %}
Bemærk, at korrektioner af orientering/spejling ikke ændrer noget i 3D Visualiser. De skal bruges til at korrigere outputtet fra den faktiske laser, så det matcher det, der vises i 3D Visualiser!
{% endhint %}

### Kopiér laserindstillinger

Se [#copy-laser-settings](./#copy-laser-settings "mention").

### Scannerindstillinger

<figure><img src="../../.gitbook/assets/Laser output scanner settings.png" alt=""><figcaption></figcaption></figure>

#### **Speed**

Indstillingen Speed bestemmer, hvor hurtigt scannerne bevæger sig.

{% hint style="danger" %}
Selvom standardindstillingerne er ret konservative, kan du stadig beskadige dine scannere, hvis du driver dem for hurtigt. Vær forsigtig, især når du øger hastigheden.
{% endhint %}

{% hint style="info" %}
Denne Speed-indstilling ændrer ikke point rate. I stedet justerer den, hvor spredt punkterne ligger. Du kan læse mere under [how-liberation-generates-laser-content.md](../../advanced/how-liberation-generates-laser-content.md "mention")
{% endhint %}

#### **Scanner sync (Colour shift / blank shift)**

Strålen skifter farve og tænder og slukker, mens scannerne flytter den rundt, og de to ting er normalt ikke helt perfekt synkroniserede. Justér denne indstilling for at få dem tilbage på linje.

{% hint style="info" %}
Dette kaldes nogle gange _blank shift_, men jeg foretrækker personligt betegnelsen _scanner sync_ – den er lidt mere præcis, da den justerer timingen af alle farveskift i forhold til scannerbevægelsen.
{% endhint %}

<div><figure><img src="../../.gitbook/assets/Colour shift tails.jpeg" alt="" width="320"><figcaption><p>Laser-"haler" – Colour shift er ikke indstillet korrekt</p></figcaption></figure> <figure><img src="../../.gitbook/assets/Colour shift no tails.jpeg" alt="" width="320"><figcaption><p>Ingen laser-"haler"! Colour shift er god!</p></figcaption></figure></div>

Hvis du ser små "haler" på dit laseroutput, skyldes det sandsynligvis, at scanner sync skal justeres. Hvis halerne stadig vises uanset hvad, driver du sandsynligvis dine scannere/laserdrivere hurtigere, end de kan håndtere. Prøv at sænke scannerhastigheden.

#### Scanner presets

Brug denne indstilling til at vælge en foruddefineret scannerindstilling. Standardindstillingen er normalt fin, så du bør ikke behøve at ændre den, medmindre du har særligt dårlige (eller gode) scannere. Hvis du vil gå mere i dybden, kan du se [scanner-presets.md](../../advanced/scanner-presets.md "mention")

#### Farvekalibrering

Du kan bruge dette system til at korrigere lysstyrkekurven og hvidbalancen for din laser. Se [colour-calibration.md](../../advanced/colour-calibration.md "mention")

#### Avancerede indstillinger

Du bør ikke behøve at rode med disse, men hvis du er nysgerrig, kan du se [advanced-laser-settings.md](../../advanced/advanced-laser-settings.md "mention")
