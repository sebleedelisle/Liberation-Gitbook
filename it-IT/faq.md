---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/faq
---

# ✅ FAQ

## Hardware

#### **Liberation funziona su Windows?**

Sì: Liberation supporta pienamente **Windows 10 e 11 (64-bit)**, con le stesse identiche funzionalità della versione Mac. Ogni release viene pubblicata contemporaneamente per entrambe le piattaforme.

#### **Liberation funziona su Mac?**

Sì: Liberation supporta pienamente **Mac (macOS 12 Monterey e versioni successive)**, con parità completa di funzionalità rispetto alla versione Windows. Tutti gli aggiornamenti vengono rilasciati insieme.

#### **Quali sono i requisiti minimi del computer?**

Dipende da quanti laser vuoi controllare. Se usi solo pochi laser, va bene anche un computer poco potente. Qualsiasi Mac con Apple Silicon funziona molto bene e dovrebbe riuscire a controllare fino a 100 laser. Se invece stai gestendo show complessi in contesti critici, ti consigliamo di usare il miglior computer che puoi permetterti.

#### **Quanti laser posso controllare con Liberation?**

Liberation può gestire molti laser da un solo computer: è stato testato con oltre 100 controller laser, quindi la risposta dipende da:

* la CPU del tuo computer
* la velocità della rete
* il tipo di abbonamento

#### **Quali controller MIDI posso usare?**

Liberation è stato progettato e ottimizzato intorno al popolare controller MIDI APC40 Mk2. Funziona anche con APC40 Mk1. Vedi [Controllo live con APC40](midi-control/live-control-with-the-apc40.md "mention")

Liberation supporta anche APC Mini e MIDI Fighter Twister. L’APC40 Mk2 resta comunque il controller di riferimento più completo.

È disponibile anche il sistema MIDI Send/Receive, che offre controlli MIDI aggiuntivi. Vedi [MIDI Send/Receive](midi-control/midi-send-receive.md "mention")

Vedi [Controllo MIDI](midi-control/ "mention") per ulteriori informazioni.

#### **Posso usarlo con qualsiasi controller MIDI?**

Per altri controller, usa il sistema MIDI Send/Receive o un traduttore MIDI in grado di inviare i messaggi MIDI predefiniti di Liberation. Cerca nel [forum](https://forum.liberationlaser.com) consigli su questa configurazione, ma realisticamente l’APC40 Mk2 resta l’opzione migliore per la maggior parte degli show dal vivo.

## Controller laser

#### **Quali controller laser sono compatibili con Liberation?**

* [Ether Dream (consigliato)](https://ether-dream.com)
* [Helios DAC](https://bitlasers.com/helios-laser-dac/)
* [Mercury by X-Laser](https://x-laser.com/pages/mercury-laser-control-system) (potresti dover aggiornare il firmware)
* LaserCube USB (e LaserDock)
* Protocollo di rete LaserCube (con connessione cablata)
* AVB, come usato dai [laser LASollinger](https://laseranimation.com/en/) (attualmente solo macOS, in fase di test)

Vedi [Laser e controller compatibili (DAC)](hardware/compatible-lasers-and-controllers-dacs.md "mention") per ulteriori informazioni

#### **Perché non supportate i controller laser \[di altre marche]?**

Per favorire una maggiore interoperabilità tra software e hardware, Liberation supporta solo DAC con un protocollo di comunicazione pubblicato. Credo che questo sia il modo migliore per far progredire il settore laser.

#### **Come faccio a sapere se il mio laser può essere usato con Liberation?**

Se il tuo laser dispone di una delle seguenti opzioni, puoi usarlo con Liberation:

* Un **ingresso ILDA esterno** – un connettore D a 25 pin, da usare con un controller esterno compatibile.
* Un **Ether Dream** installato internamente.
* Qualsiasi **LaserCube** (funziona sia con LaserCube USB sia Wi-Fi).
* Un’**unità X-Laser con sistema Mercury integrato** (in modalità Ether Dream).
* Un **proiettore LaserAnimation Sollinger con AVB integrato** (solo macOS, richiede dispositivi di rete compatibili con AVB, attualmente in fase di test).

Vedi [Laser e controller compatibili (DAC)](hardware/compatible-lasers-and-controllers-dacs.md "mention") per ulteriori informazioni

#### **Posso usare Liberation con il mio LaserCube?**

Sì, Liberation funziona direttamente con qualsiasi LaserCube. Vedi [LaserCube](hardware/lasercube.md "mention")

## Licenze

#### **Quanto costa una licenza?**

Vedi la pagina [shop](https://liberationlaser.com/shop) per i prezzi aggiornati.

#### **Quali sono le limitazioni tra i livelli di licenza?**

Vedi la pagina [shop](https://liberationlaser.com/shop) per le opzioni di licenza attualmente disponibili.

Tieni presente che puoi configurare, visualizzare in anteprima e progettare show con tutti i laser che vuoi in **ogni** livello, anche quello gratuito. Non ci sono altre limitazioni, a parte il numero di laser che puoi _armare_. Tutte le altre funzionalità di Liberation sono disponibili per tutti.

#### **Posso passare a un livello superiore?**

Puoi passare a un livello superiore in qualsiasi momento. Riceverai un rimborso parziale per il tempo residuo della licenza attuale e il nuovo piano partirà immediatamente. Vedi [Upgrade / downgrade della tua licenza](installation/upgrade-downgrade-your-license.md "mention")

#### **Posso passare a una licenza inferiore?**

Puoi passare a un livello inferiore in qualsiasi momento, ma la modifica avrà effetto alla fine del periodo di licenza corrente. Vedi [Upgrade / downgrade della tua licenza](installation/upgrade-downgrade-your-license.md "mention")

#### **Come autorizzo il mio computer con la mia licenza?**

Dopo aver acquistato una licenza, puoi autorizzare il computer direttamente dal software Liberation. Nella schermata _About_ vedrai un pulsante _Authorise_, che ti chiederà di accedere al sito web. Segui le istruzioni a schermo per completare il processo di autorizzazione. Vedi [Autorizzazione e revoca dell'autorizzazione](installation/authorising-and-de-authorising.md "mention")

#### **Quanto spesso devo collegare il computer a internet?**

Ogni volta che la licenza si rinnova, dovrai collegare Liberation a internet per aggiornare la sua licenza interna. Con un pagamento ricorrente mensile, dovrai collegarti ogni mese.

#### **Cosa succede se non riesco a collegare il computer a internet dopo il rinnovo?**

Liberation ti concede un periodo di tolleranza di 7 giorni dopo il rinnovo della licenza per collegarti a internet e aggiornare la licenza interna. Dopo questo periodo, Liberation tornerà in modalità _Free_.

#### **Cosa succede se la mia carta di credito scade?**

Riceverai una notifica via email dal nostro provider di pagamento e dovrai aggiornare il metodo di pagamento. Accedi al sito web e usa il link _Update payment details_ nella pagina degli abbonamenti.

#### **Come annullo la mia licenza ricorrente?**

Accedi al sito web, apri la pagina _Your subscriptions_, seleziona l’abbonamento che vuoi annullare, quindi fai clic sul link _Cancel Subscription_. Potrai continuare a usare Liberation fino al termine del periodo di licenza.

#### **Su quanti computer posso installare Liberation?**

Puoi installare Liberation su tutti i computer che vuoi. Le autorizzazioni della licenza sono necessarie solo per abilitare l’output laser / DMX, e il tuo livello di licenza determina quanti computer possono essere autorizzati per l’output contemporaneamente. Vedi [Come funziona la licenza](installation/how-licensing-works.md "mention")

#### **Come sposto la mia licenza da un computer a un altro?**

* Apri Liberation sul computer che non vuoi più usare
* Assicurati di essere connesso a internet e fai clic sul pulsante _De-authorise this computer_ nella schermata _About_
* Ora apri Liberation sul nuovo computer
* Fai clic sul pulsante _Authorise this computer_ nella schermata _About_.
* Si aprirà il sito web: effettua l’accesso e segui le istruzioni a schermo per completare l’autorizzazione

Puoi anche disautorizzare da remoto un computer a cui non hai più accesso, con alcune limitazioni. Vedi [Autorizzazione e revoca dell'autorizzazione](installation/authorising-and-de-authorising.md "mention")

#### **Posso disautorizzare Liberation su un computer perso o rubato?**

Puoi disautorizzare il computer tramite il sito web. Se l’installazione di Liberation non è stata online dall’ultimo rinnovo, puoi farlo immediatamente.

In caso contrario, la disautorizzazione avrà effetto al rinnovo dell’abbonamento oppure quando il computer si collega a internet, a seconda di quale evento avviene prima. Se hai urgente bisogno di autorizzare di nuovo un nuovo computer, contatta il supporto.

### Uso di Liberation

#### La configurazione predefinita ha 8 laser: come posso modificarla?

Vedi [Configurare il tuo progetto](setting-up/setting-up-your-project.md "mention") e [Aggiungere / rimuovere laser](setting-up/adding-removing-lasers.md "mention")

#### Posso copiare le impostazioni delle zone da un laser agli altri?

Sì. Vedi [Copiare le zone tra laser](output-view/copy-zones-between-lasers.md "mention")

#### Posso digitare un numero invece di usare uno slider?

Sì. Fai `Cmd / Ctrl`-click sullo slider e potrai inserire il valore con la tastiera.

#### **Come sincronizzo Liberation con la musica?**

Ha un sistema intelligente di "tap tempo" che funziona come ti aspetteresti, ma puoi anche usare un clock MIDI esterno o Ableton Link. Vedi [Tempo / sincronizzazione](tempo-synchronisation.md "mention"). La timeline può essere sincronizzata al timecode LTC/SMPTE in ingresso tramite qualsiasi interfaccia audio. Vedi [Timecode](timecode.md "mention").

#### Quali impostazioni devo regolare per ottenere il miglior output dal laser?

L’impostazione principale è _Colour Shift_, che compensa il leggero ritardo tra il movimento degli specchi e il cambiamento di luminosità dei laser. Se i punti o i fasci del laser hanno piccole “code”, dovrai regolare questa impostazione. Per un esempio di “code”, guarda le foto nella pagina [Pannello delle impostazioni Laser output](setting-up/laser-settings.md "mention")

Puoi anche provare a modificare la velocità degli scanner: più lenta se i tuoi scanner sono di base, oppure più veloce se sono di buona qualità. Ma **usa questa impostazione con cautela, perché puoi danneggiare gli scanner se li spingi troppo.**

Sono disponibili anche alcune impostazioni scanner predefinite. L’opzione predefinita è prudente e va bene per la maggior parte delle esigenze con fasci laser. Ci sono però altri preset per scanner migliori, e preset ottimizzati per la grafica.

Per ulteriori informazioni, vedi [Pannello delle impostazioni Laser output](setting-up/laser-settings.md "mention"); per sapere come creare i tuoi preset, vedi [◼️ Preset scanner e profili di rendering](advanced/scanner-presets.md "mention") (avanzato, in corso)

Puoi anche correggere il bilanciamento del colore usando le impostazioni _Colour calibration_. Vedi [Calibrazione del colore](advanced/colour-calibration.md "mention")(tecnica avanzata)

#### A cosa serve l’impostazione _Latency(ms)_?

È la latenza dei frame, cioè il tempo massimo tra la generazione di un frame e il suo successivo invio a un laser. Normalmente non dovresti aver bisogno di modificarla, ma se hai problemi di rete puoi provare ad aumentarla. Vedi [Impostazione della latenza](setting-up/latency-setting.md "mention") per maggiori dettagli.

### Clip

#### Come regolo le zone e le impostazioni di un Clip senza avviarlo?

Fai `Alt / Option`-click per renderlo il _Clip attualmente selezionato_, senza però attivarlo. Vedi anche [Avviare / fermare le clip](clips/starting-stopping-clips.md "mention")

#### Come copio i Clip?

Fai clic e trascina tenendo premuto il tasto `Alt / Option`. Vedi anche [Organizzare il Clip Deck](clips/organising-your-clip-deck.md "mention")

#### Come elimino i Clip?

Fai clic e trascinali fuori dal Clip Deck. Vedi anche [Organizzare il Clip Deck](clips/organising-your-clip-deck.md "mention")

#### Come faccio selezioni multiple, elimino, combino Clip Deck ecc.?

Vedi [Organizzare il Clip Deck](clips/organising-your-clip-deck.md "mention")

#### Cosa indicano il piccolo simbolo del microfono e le altre icone sul Clip?

Servono a indicare che un Clip riceve input audio o MIDI, mentre i 3 puntini indicano che è presente un ritardo di zona. Vedi [Cosa sono le piccole icone sui pulsanti delle clip?](clips/what-are-the-small-icons-on-the-clip-buttons.md "mention")
