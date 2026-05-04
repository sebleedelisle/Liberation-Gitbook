---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/dmx-control/creating-dmx-zones
---

# 🟩 Skapa DMX-zoner

1. Anslut din Art-Net node och konfigurera den enligt [Ansluta till en Art-Net node](../connecting-to-an-artnet-node.md "mention").
2. Öppna **DMX Zones** och klicka på **ADD DMX ZONE**.
3. Ställ in zonens **Node**, **Universe** och **Address** så att de matchar armaturen.
4. Välj en **Preset** för armaturen. Förinställningen definierar vilka DMX-kanaler som får fasta värden, på/av-värden för innehåll, RGB-färg, X/Y-position, ljusstyrka eller explicita DMX Value-indata.
5. Klicka på **Edit DMX profile/channel mapping** (reglageikonen) för att redigera kanalmappningen. Standardförinställningen börjar med en på/av-kanal för innehåll och RGB-färgkanaler.
6. Tilldela Clips till en DMX zone på samma sätt som du tilldelar dem till beam zones eller canvas zones.
7. Tryck på **ARM** när du är redo att låta zonen skicka DMX.

{% hint style="warning" %}
Endast aktiverade DMX zones skickar livevärden. DMX zones som inte är aktiverade nollställer sina mappade kanaler, vilket är säkrare när du konfigurerar armaturer.
{% endhint %}

DMX-utdata begränsas också av din licensnivå. Om knappen **ARM** är inaktiverad, kontrollera om din nivå omfattar DMX-utdata eller om det maximala antalet aktiverade DMX zones redan har nåtts.
