---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/dmx-control/creating-dmx-zones
---

# ◼️ Creare zone DMX

1. Collega il tuo node Art-Net e configuralo in [Connessione a un node Art-Net](../connecting-to-an-artnet-node.md "mention").
2. Apri **DMX Zones** e fai clic su **ADD DMX ZONE**.
3. Imposta **Node**, **Universe** e **Address** della zone in modo che corrispondano al dispositivo.
4. Scegli un **Preset** per il dispositivo. Il preset definisce quali canali DMX ricevono valori fissi, valori di contenuto on/off, colore RGB, posizione X/Y, luminosità oppure ingressi DMX Value espliciti.
5. Fai clic su **Edit DMX profile/channel mapping** (icona con gli slider) per modificare la mappatura dei canali. Il preset predefinito inizia con un canale di contenuto on/off e canali colore RGB.
6. Assegna i Clip alla DMX zone nello stesso modo in cui li assegni alle beam zone o alle canvas zone.
7. Premi **ARM** quando sei pronto a far sì che la zone invii DMX in uscita.

{% hint style="warning" %}
Solo le DMX zone abilitate inviano valori live. Le DMX zone non abilitate azzerano i canali mappati, una condizione più sicura durante la configurazione dei dispositivi.
{% endhint %}

L'uscita DMX è limitata anche dal livello della tua licenza. Se il pulsante **ARM** è disattivato, verifica se il tuo livello include l'uscita DMX o se è già stato raggiunto il numero massimo di DMX zone abilitate.
