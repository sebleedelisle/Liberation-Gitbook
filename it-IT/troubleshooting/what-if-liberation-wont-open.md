---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/troubleshooting/what-if-liberation-wont-open
---

# ✅ Cosa fare se Liberation non si apre?

È raro, ma a volte Liberation potrebbe non avviarsi o chiudersi subito dopo l’apertura. Quasi sempre succede perché uno dei file di configurazione locali si è danneggiato, di solito dopo un crash del sistema o un evento imprevisto sul computer.

Per fortuna, il problema si risolve facilmente reimpostando le impostazioni locali. Ecco come farlo su macOS e Windows.

> **Importante**
>
> * Chiudi Liberation prima di fare qualsiasi operazione.
> * Questi passaggi riguardano solo impostazioni locali, log e cache. La tua licenza e il tuo account non vengono modificati.

***

#### Dove trovare la cartella di lavoro

Ogni versione di Liberation ha la propria cartella di lavoro. Per esempio, se stai usando la versione 1.0.0, il nome della cartella sarà 1.0.0.

* **macOS**: `~/Library/Application Support/Liberation/1.0.0`
* **Windows**: `AppData\Local\Liberation\1.0.0`

**Come aprire rapidamente la cartella**

**macOS**

1. In Finder, premi **Shift + Cmd + G**.
2.  Incolla questo percorso e premi **Enter**:

    ```
    ~/Library/Application Support/Liberation
    ```
3. Apri la cartella corrispondente al numero della tua versione, per esempio `1.0.0`.

**Windows**

1.  Premi **Win + R**, incolla questo percorso e premi **Enter**:

    ```
    %LOCALAPPDATA%\Liberation
    ```
2. Apri la cartella corrispondente al numero della tua versione, per esempio `1.0.0`.

> **Suggerimento per Windows**: se invece navighi tramite File Explorer, abilita gli elementi nascosti: **View > Show > Hidden items**.

***

#### Passaggio 1 – Reimposta in modo sicuro il file delle impostazioni

All’interno della cartella della tua versione, apri:

```
data/liberation/
```

Dentro la cartella liberation dovresti trovare un file chiamato se`ttings.json`. Elimina questo file.

* **Esempio macOS**: `~/Library/Application Support/Liberation/1.0.0/data/liberation/settings.json`
* **Esempio Windows**: `%LOCALAPPDATA%\Liberation\1.0.0\data\liberation\settings.json`

Ora prova ad avviare Liberation. Se si apre, hai finito.

***

#### Passaggio 2 – Controlla se c’è un clip problematico

Se Liberation si è chiuso in modo anomalo mentre stavi modificando un clip, è possibile che qualcosa in quel file del clip stia causando il problema.

Nella stessa cartella del file settings.json dovresti trovare un file chiamato clipEdit`.json`

Fai una copia di backup di questo file in un posto sicuro, per esempio sul Desktop, poi eliminalo dalla cartella di lavoro di Liberation.

Prova ad avviare di nuovo Liberation. Se ora si apre normalmente, invia il file di backup via email a [**info@liberationlaser.com**](mailto:info@liberationlaser.com), così possiamo verificare che cosa ha causato il problema.

***

#### Passaggio 3 - Fai un backup, poi elimina l’intera cartella di lavoro

Se il Passaggio 1 e il Passaggio 2 non hanno risolto il problema:

1. **Fai un backup** dell’intera cartella della versione:
   * macOS: fai clic destro sulla cartella `1.0.0` e scegli **Compress** per creare uno zip, oppure copiala in un posto sicuro, per esempio sul Desktop.
   * Windows: fai clic destro sulla cartella `1.0.0` e scegli **Send to > Compressed (zipped) folder**, oppure copiala in un posto sicuro, per esempio sul Desktop.
2. Dopo aver fatto il backup, **elimina** la cartella originale `1.0.0` dalla posizione di lavoro di Liberation.
3. Avvia di nuovo Liberation. Verrà creata una nuova cartella di lavoro pulita.

Se Liberation ora si apre, passa al Passaggio 4.

***

#### Passaggio 4 - Inviaci il backup

Questo ci aiuta a capire che cosa ha causato il problema, così possiamo prevenirlo nelle versioni future.

Comprimi in zip il tuo **backup** del Passaggio 3, se non l’hai già fatto, poi inviacelo via email per permetterci di diagnosticare la causa.

* **A**: [info@liberationlaser.com](mailto:info@liberationlaser.com)
* **Oggetto**: Correzione avvio Liberation - backup cartella di lavoro
* **Corpo**: includi:
  * Sistema operativo e versione (per esempio macOS 14.6 o Windows 11 23H2)
  * Versione di Liberation (per esempio 1.0.0)
  * Quale passaggio ha risolto il problema, se applicabile (Passaggio 1, Passaggio 2 o Passaggio 3)
  * Una breve descrizione di cosa è successo prima che il problema iniziasse
* **Allegato**: il backup in formato zip della tua cartella di lavoro `1.0.0`.

> Se lo zip è troppo grande per l’email, caricalo su un servizio cloud e condividi un link.

***

#### Non si avvia ancora dopo il Passaggio 3?

Se Liberation continua a non aprirsi dopo aver eliminato la cartella di lavoro:

* Riavvia il computer e riprova.
* Disattiva temporaneamente antivirus o strumenti di sicurezza che potrebbero bloccare la creazione di nuove cartelle, poi prova ad avviare Liberation.
* Reinstalla l’ultima build di Liberation sopra l’installazione esistente.
* Se nessuna delle soluzioni precedenti funziona, contatta il supporto a [**info@liberationlaser.com**](mailto:info@liberationlaser.com) con i dettagli e gli eventuali crash log presenti nella sottocartella `logs`.

***

#### Riepilogo

1. Elimina `data/liberation/settings.json` nella cartella di lavoro della tua versione.
2. Se stavi modificando un clip, fai un backup e poi elimina `data/liberation/clipEdit.json`.
3. Se continua a non aprirsi, fai un backup e poi elimina l’intera cartella `1.0.0` (o quella della tua versione).
4. Se il Passaggio 3 risolve il problema (o anche se non lo risolve), comprimi il backup in zip e invialo a [**info@liberationlaser.com**](mailto:info@liberationlaser.com) indicando sistema operativo e versione di Liberation.
