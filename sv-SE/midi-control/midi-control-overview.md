---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/midi-control/midi-control-overview
---

# 🟩 Översikt över MIDI-kontroll

Liberation använder MIDI på flera sätt:

* Som live-controller. APC40 Mk1/Mk2, APC Mini och MIDI Fighter Twister kan anslutas automatiskt när motsvarande enhet är tillgänglig. Se [MIDI-styrenheter för livekontroll](live-control-with-the-apc40.md "mention").
* Som källa för klocksynkronisering, med MIDI clock och MIDI song position-meddelanden. Se [MIDI clock](../tempo-synchronisation.md#midi-clock "mention")
* Som interaktiv ingång på MIDI notes-noden för att skapa effekter i stil med en ”laserharpa”. Se [MIDI notes](../clip-editor/operator-nodes/midi-notes.md "mention")
* Som ett mer allmänt in-/utgångssystem med MIDI Send/Receive-systemet. Se [MIDI Send/Receive](midi-send-receive.md "mention")

Live-controllers som stöds följer Liberation:s tillstånd på skärmen: knappar för Clips lyser med sina gruppfärger, zone-knappar visar status för varje zone, och mappade rattar eller encoders följer den aktuella effekten eller kontrollerna i panelen Parameters.
