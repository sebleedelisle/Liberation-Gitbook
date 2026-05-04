---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/midi-control/live-control-with-the-apc40
---

# 🟩 Live MIDI Controllers

<figure><img src="../.gitbook/assets/qs-apc40.jpeg" alt=""><figcaption></figcaption></figure>

### **APC40-ohjain**

Tämä on Liberationin oletusarvoinen laiteohjain. Sen käyttöä suositellaan vahvasti, ja voidaan hyvin sanoa, että Liberation on alusta asti suunniteltu tämän laitteen ympärille. Kun liität APC40:n, Liberation muodostaa siihen yhteyden automaattisesti heti.

{% hint style="warning" %}
_Voi ei! USB-liitin irtosi kesken esityksen!_

Ei hätää – liitä se vain takaisin. Liberation muodostaa yhteyden automaattisesti uudelleen ilman säätöä.
{% endhint %}

### APC40 Mark 1 vai Mark 2?

Lyhyesti: Mark 2 on suositeltu, koska siinä on täysväriset painikkeet, jotka vastaavat paremmin Liberationin Clip Deck -käyttöliittymää. Mark 1 toimii tarvittaessa, mutta sen käyttö on hieman sekavampaa, koska asettelu poikkeaa jonkin verran näytöllä näkyvästä ja painikkeet voivat olla vain punaisia, oransseja tai vihreitä, joten ne eivät vastaa Clip-värejä.

{% hint style="info" %}
Alkuperäinen APC40 Mark 1 julkaistiin vuonna 2009(!), ja jotkut suosivat sitä yhä metallirakenteen ja tukevan, konsolimaisen muodon vuoksi. Päivitetty Mark 2 julkaistiin vuonna 2014. Vaikka sen valmistus lopetettiin vuonna 2024, se palaa tuotantoon vuonna 2025 visuaalisten artistien (Resolume jne.) ja laserkäyttäjien kysynnän vuoksi.
{% endhint %}

Täydellinen luettelo APC40:n ohjaimista on kohdassa [APC40-viite](../reference/apc40-reference.md "mention")

### APC Mini

Liberation 1.0.3 sisältää myös APC Mini -profiilin. Se määrittää 8x5-kokoisen Clip-ruudukon, zone-painikkeet, zone X/Y -peilausohjaimet, ryhmäpainikkeet, kaikkien Clips-toistojen pysäytyksen, Clip-sivun siirron, zone-sivun siirron, tap tempon, tahdin nollauksen ja tempon hienosäädön. Sen liu’ut säätävät tehostetasoja, ja shift-tilassa liu’ut säätävät tehosteparametreja. Viimeinen liuku säätää Global Brightness -arvoa.

### MIDI Fighter Twister

MIDI Fighter Twister -profiili on tarkoitettu erityisesti enkoodereihin perustuvaan ohjaukseen Clipien käynnistämisen sijaan. Yksi enkooderirivi ohjaa parametria 1 tehostepaikoissa 1–8, ja toinen rivi seuraa Parameters-paneelin kahdeksaa kontekstikohtaista ohjainta, mukaan lukien Clip-siirto, zone-viive, globaali pyöritys/skaalaus ja ryhmähäivytykset.
