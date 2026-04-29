---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clip-editor/fundamentals/render-profile
---

# 🟩 Render profile

Det finns en _Render Profile_-inställning i varje _Creator_-nod, och den avgör hur formerna ritas (eller _renderas_) med lasrarna.

**För de flesta användningar fungerar inställningen&#x20;**_**DEFAULT**_**&#x20;utmärkt**. Men om du arbetar med grafik eller komplext innehåll kan du vilja ha mer kontroll över hur varje form renderas.

{% hint style="info" %}
Till skillnad från de flesta laserprogram genererar Liberation en punktström i realtid, precis innan den skickas vidare till laserkontrollerna. Det sparar mycket diskutrymme, eftersom clips bara är några få kB i stället för MB med förrenderade punktströmmar.

Det betyder också att du kan anpassa samma innehåll för olika skannertyper, laser för laser, utan att behöva ändra själva clipsen.

Mer information finns i [◼️ Så genererar Liberation laserinnehåll](../../advanced/how-liberation-generates-laser-content.md "mention")
{% endhint %}

Det finns tre förinställda _Render Profiles_: _DEFAULT_, _FAST_ och _DETAIL._

_**DEFAULT**_ - en bra allmän profil som passar bäst för det mesta

_**FAST** -_ om ditt clip innehåller mycket material och en del av det bara är mycket enkla punkter och raka linjer, kan du få mindre flimmer om du väljer det här alternativet.

_**DETAIL**_ - använd det här alternativet om du ritar något som behöver skarpa hörn. Tänk dock på att skannrarna rör sig långsammare, vilket gör att utsignalen kan flimra.

{% hint style="info" %}
I clip-editorn kan du tilldela _Creator_-noder till olika render profiles, men varje laser bearbetar dessa profiler beroende på sina skannerinställningar. Se [◼️ Skannerförinställningar och renderprofiler](../../advanced/scanner-presets.md "mention")
{% endhint %}
