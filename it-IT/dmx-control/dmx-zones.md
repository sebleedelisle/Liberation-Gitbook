---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/dmx-control/dmx-zones
---

# ◼️ Zone DMX

Le DMX zone sono zone di Output di Liberation che inviano Art-Net/DMX invece di punti laser. Compaiono insieme alle beam zone e alle canvas zone, quindi puoi assegnare i Clip anche a loro con lo stesso flusso di selezione delle zone.

Apri **DMX Zones** dal menu, oppure usa la sezione DMX in Laser Overview, per gestirle.

* **ADD DMX ZONE** - crea una nuova DMX zone.
* **ARM** - abilita l’uscita DMX per quella zone. Una DMX zone non armata azzera i canali mappati.
* **Node** - seleziona il numero del nodo Art-Net.
* **Universe** - seleziona l’universo Art-Net. Il valore visualizzato parte da 1, quindi Universe 1 è il primo universo.
* **Address** - imposta l’indirizzo iniziale del fixture. Anche il valore visualizzato parte da 1.
* **Preset** - sceglie il preset DMX che mappa il contenuto del Clip sui canali DMX.
* **Edit DMX zone settings** (icona a matita) - apre le impostazioni della zone, come l’inoltro manuale della zone e l’orientamento del fixture.
* **Edit DMX profile/channel mapping** (icona con cursori) - apre l’editor del preset/canali DMX.
* **Delete** - rimuove la DMX zone.

### Limiti di armamento

Il numero di DMX zone che puoi armare contemporaneamente dipende dal livello della tua licenza. Se il tuo livello non consente l’uscita DMX, oppure hai già armato il numero massimo di DMX zone, il pulsante **ARM** per le zone aggiuntive è disabilitato e mostra un’icona di divieto al passaggio del mouse.

Disarma un’altra DMX zone, oppure usa un livello di licenza con un limite DMX più alto, prima di armare altre zone.
