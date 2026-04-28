---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/setting-up/laser-settings
---

# ✅ Innstillingspanelet Laser output

Åpne innstillingspanelet _Laser output_ fra menyen _View -> Laser Output Settings._

<figure><img src="../.gitbook/assets/Copy Laser Setting in Laser Output.png" alt="" width="326"><figcaption></figcaption></figure>

Dette viser innstillingene for laseren som er valgt nå. Du kan bytte laser:

* via tallknappen i panelet _Laser overview_
* med en talltast på tastaturet, der tastene 1 til 0 åpner laser 1–10
* med `Tab`-tasten for å bla gjennom laserne (`Shift + Tab` går bakover).

Øverst i dette panelet ser du:

* en tallknapp – klikk på denne for å armere/dearmere denne laseren. Den er rød når laseren er armert.
* en _Brightness_-skyveknapp kun for denne laseren. Merk at denne kombineres med den globale lysstyrken.
* _Test Pattern_-bryter og mønstervelger. Dette lar deg velge et bestemt testmønster kun for denne laseren. (Disse kontrollene speiles i verktøylinjen i Output-visningen).

### Output-retning / korrigering av speiling

De neste elementene brukes til å korrigere oppsettet av laseren, slik at den oppfører seg konsekvent i Liberation.

* **Flip horizontal / vertical** – disse valgene lar deg korrigere laserens output

{% hint style="info" %}
Du skal normalt ikke trenge å endre innstillingene for horizontal / vertical flip, med mindre laseren er koblet feil, eller den har X/Y flip-knapper på baksiden som ikke er satt riktig. Hvis du vil speile output for en bestemt clip, kan dette gjøres på selve clipen.
{% endhint %}

* **Orientation** – hvis laseren er rigget på siden eller opp ned, kan du korrigere rotasjonen med denne innstillingen.
* **Fine position adjustments** – kan brukes til å korrigere svært små forskyvninger/rotasjoner. Dette er laget for å korrigere drift/setning hvis en laser har stått over natten eller i lengre perioder.

{% hint style="info" %}
Merk at korrigeringene for retning/speiling ikke endrer noe i 3D Visualiser. De skal brukes til å korrigere output fra den faktiske laseren, slik at den samsvarer med det som vises i 3D Visualiser!
{% endhint %}

### Copy laser settings

Se [#copy-laser-settings](laser-settings.md#copy-laser-settings "mention").

### Scanner settings

<figure><img src="../.gitbook/assets/Laser output scanner settings.png" alt=""><figcaption></figcaption></figure>

#### **Speed**

Speed-innstillingen bestemmer hvor raskt skannerne beveger seg.

{% hint style="danger" %}
Selv om standardinnstillingene er ganske forsiktige, kan du fortsatt skade skannerne hvis du driver dem for raskt. Vær forsiktig, spesielt når du øker hastigheten.
{% endhint %}

{% hint style="info" %}
Denne Speed-innstillingen endrer ikke punktraten. I stedet justerer den hvor spredt punktene er. Se [how-liberation-generates-laser-content.md](../advanced/how-liberation-generates-laser-content.md "mention") for mer informasjon.
{% endhint %}

#### **Scanner sync (Colour shift / blank shift)**

Strålen skifter farge og slås av og på mens skannerne flytter den rundt, og disse to tingene er vanligvis ikke perfekt synkronisert med hverandre. Juster denne innstillingen for å få dem på linje igjen.

{% hint style="info" %}
Dette kalles noen ganger _blank shift_, men jeg foretrekker personlig begrepet _scanner sync_ – det er litt mer presist, siden det justerer timingen for alle fargeendringene i forhold til skannerbevegelsen.
{% endhint %}

<div><figure><img src="../.gitbook/assets/Colour shift tails.jpeg" alt="" width="320"><figcaption><p>Laser-«haler» – Colour shift er ikke riktig innstilt</p></figcaption></figure> <figure><img src="../.gitbook/assets/Colour shift no tails.jpeg" alt="" width="320"><figcaption><p>Ingen laser-«haler»! Colour shift er bra!</p></figcaption></figure></div>

Hvis du ser små «haler» i laser-outputen, skyldes det sannsynligvis at Scanner sync må justeres. Hvis halene fortsatt vises uansett hva du gjør, driver du sannsynligvis skannerne/laserdriverne raskere enn de tåler. Prøv å redusere scanner speed.

#### Scanner presets

Bruk dette for å velge en forhåndsdefinert scanner-innstilling. Standardvalget er som regel fint, så du skal normalt ikke trenge å endre denne innstillingen med mindre du har spesielt dårlige (eller gode) skannere. Hvis du vil gå dypere, se [scanner-presets.md](../advanced/scanner-presets.md "mention")

#### Colour calibration

Du kan bruke dette systemet til å korrigere lysstyrkekurven og hvitbalansen til laseren. Se [colour-calibration.md](../advanced/colour-calibration.md "mention")

#### Advanced settings

Du skal normalt ikke trenge å tukle med disse, men hvis du er nysgjerrig, se [advanced-laser-settings.md](../advanced/advanced-laser-settings.md "mention")
