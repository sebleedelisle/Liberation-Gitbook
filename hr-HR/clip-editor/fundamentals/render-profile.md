---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clip-editor/fundamentals/render-profile
---

# 🟩 Render Profile

Svaki _Creator_ node ima postavku _Render Profile_, koja određuje kako se oblici crtaju (ili _renderiraju_) laserima.

**Za većinu primjena postavka&#x20;**_**DEFAULT**_**&#x20;sasvim je dovoljna**. No ako radite s grafikom ili složenim sadržajem, možda ćete htjeti više kontrole nad načinom renderiranja svakog oblika.

{% hint style="info" %}
Za razliku od većine laserskog softvera, Liberation generira tok točaka u stvarnom vremenu, neposredno prije slanja na laser controller uređaje. Time se štedi mnogo prostora na disku: svaki Clip zauzima samo nekoliko kB, umjesto MB unaprijed renderiranih tokova točaka.

To također znači da isti sadržaj možete prilagoditi različitim vrstama skenera za svaki laser zasebno, bez potrebe za mijenjanjem samih Clips.

Za više pojedinosti pogledajte [Kako Liberation generira laserski sadržaj](../../advanced/how-liberation-generates-laser-content.md)
{% endhint %}

Postoje tri unaprijed definirana _Render Profile_: _DEFAULT_, _FAST_ i _DETAIL._

_**DEFAULT**_ - dobar opći profil, najbolji za većinu sadržaja

_**FAST** -_ ako vaš Clip ima mnogo sadržaja, a dio njega čine vrlo jednostavne točke i ravne linije, ovom opcijom možete smanjiti treperenje.

_**DETAIL**_ - ako crtate nešto što zahtijeva oštre kutove, upotrijebite ovu opciju. Imajte na umu da će se skeneri kretati sporije, zbog čega izlaz može više treperiti.

{% hint style="info" %}
U Clip Editor možete dodijeliti Creators različitim Render Profile postavkama, ali svaki laser obrađuje te profile ovisno o svojim postavkama skenera. Pogledajte [Preseti skenera](../../advanced/scanner-presets.md)
{% endhint %}
