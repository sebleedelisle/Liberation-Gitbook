---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clip-editor/fundamentals/render-profile
---

# 🟩 Renderprofil

Der er en _Render Profile_-indstilling i hver _Creator_-node, og den bestemmer, hvordan formerne tegnes (eller _renderes)_ med laserne.

**Til de fleste formål er indstillingen&#x20;**_**DEFAULT**_**&#x20;helt fin**. Men hvis du arbejder med grafik eller komplekst indhold, kan du få brug for mere kontrol over, hvordan hver form renderes.

{% hint style="info" %}
I modsætning til det meste lasersoftware genererer Liberation en punktstream i realtid, lige før den sendes videre til lasercontrollerne. Det sparer dig for meget diskplads: clips fylder kun få kB i stedet for MB med præ-renderede punktstreams.

Det betyder også, at du kan tilpasse det samme indhold til forskellige scannertyper fra laser til laser uden at skulle ændre selve clipsene.

Du kan læse mere i [◼️ Sådan genererer Liberation laserindhold](../../advanced/how-liberation-generates-laser-content.md "mention")
{% endhint %}

Der er tre forudindstillede _Render Profiles_: _DEFAULT_, _FAST_ og _DETAIL._

_**DEFAULT**_ - en god generel profil, bedst til det meste

_**FAST** -_ hvis dit clip har meget indhold, og noget af det kun er meget simple prikker og lige linjer, kan du få mindre flimmer ved at vælge denne indstilling.

_**DETAIL**_ - brug denne indstilling, hvis du tegner noget, der kræver skarpe hjørner. Men vær opmærksom på, at dine scannere bevæger sig langsommere, hvilket kan få outputtet til at flimre.

{% hint style="info" %}
I clip-editoren kan du tildele creators til forskellige renderprofiler, men hver laser behandler disse profiler afhængigt af dens scannerindstillinger. Se [◼️ Scanner-presets og render-profiler](../../advanced/scanner-presets.md "mention")
{% endhint %}
