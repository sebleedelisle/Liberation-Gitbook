---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/midi-control/midi-send-receive
---

# 🟩 MIDI Send/Receive

MIDI Send/Receive -järjestelmä on erillinen APC40-ohjauksista. Sen avulla MIDI-dataa voidaan tuoda Liberationiin ja lähettää siitä ulos. Toiminnoilla, kuten klippien käynnistämisellä ja pysäyttämisellä, yleisten asetusten säätämisellä sekä efektien ja klippiparametrien ohjauksella, on kullakin oma MIDI-komentonsa.

{% hint style="info" %}
MIDI Send/Receive -järjestelmä rakennettiin alun perin ennen kuin Liberationissa oli Timeline-toimintoja. Se oli kiertotapa, jolla esityksen pystyi tallentamaan ja toistamaan musiikkiohjelmistossa, kuten Logic Prossa tai Cubasessa.

Se antaa suoran hallinnan klippeihin, efekteihin ja asetuksiin riippumatta näytöstä ja clip deckin vierityskohdasta. Järjestelmätason live-ohjaustoimintoja, kuten tap tempo, alueiden määrittäminen ja arm/disarm, ei ole toteutettu.
{% endhint %}

### MIDI Send/Receive -asetukset

Avaa _MIDI Send/Receive_ -paneeli valikosta _View -> MIDI Send/Receive_. Näet vaihtoehdot _SEND, RECEIVE,_ tai _BOTH_ lähettämistä ja vastaanottamista varten, ja voit valita, mitä MIDI-liitäntöjä haluat käyttää.

{% hint style="danger" %}
Käytä _BOTH_-asetusta varoen. MIDI-laitteet ja -ohjelmistot voidaan määrittää lähettämään takaisin niille tuleva data. Tämä voi aiheuttaa MIDI-datan takaisinkytkentäsilmukan, mikä ei ole hyvä asia.
{% endhint %}

### MIDI-määritys

Katso [midi-send-receive-default-mapping.md](../reference/midi-send-receive-default-mapping.md)

Aion lisätä tulevaisuudessa paljon mukautettavampia MIDI-määrityksiä, mutta sillä välin voit käyttää sovelluksia kuten [BOME](https://www.bome.com/products/miditranslator) ja [Chetaigne](http://benjamin.kuperberg.fr/chataigne/en) muuntamaan MIDI-viestejä Liberationin ja oman laitteistosi välillä.
