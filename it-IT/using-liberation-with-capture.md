---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/using-liberation-with-capture
---

# 🟩 Usare Liberation con Capture

Liberation supporta [Capture](https://capture.se) come visualizzatore esterno (dalla versione 1.0.3 in poi). Se usi già Capture nel tuo flusso di lavoro, puoi usarlo per visualizzare l’output laser live di Liberation nella tua scena 3D.

### Come funziona

Non serve alcuna procedura di connessione speciale né un collegamento manuale.

Finché:

* Liberation e Capture sono sulla stessa rete
* Il firewall consente la connessione

…tutti i laser che hai configurato in Liberation appariranno automaticamente in Capture come sorgenti media. Non devi configurare indirizzi IP né abilitare opzioni particolari: compaiono semplicemente.

### Visualizzare i laser in Capture

Tutti i laser configurati in Liberation appariranno in Capture come sorgenti media disponibili.

Per vedere effettivamente l’output:

* Il laser deve essere armato in Liberation
* La sorgente deve essere collegata a un apparecchio laser dentro Capture

Una volta armato, Capture visualizzerà lo stream di output live proveniente da Liberation. Se un laser viene disarmato in Liberation, resterà visibile in Capture come sorgente, ma non genererà alcun output.

Consulta la documentazione su [capture.se](https://www.capture.se/) per ulteriori istruzioni e supporto sulla configurazione dei laser in Capture. <br>

### Limiti della licenza e laser armati

Le connessioni a Capture vengono trattate esattamente come le uscite laser fisiche.

Questo significa che:

* Puoi armare solo il numero di laser consentito dal livello della tua licenza
* Solo i laser armati invieranno attivamente dati a Capture

### Mi serve Capture?

No, non è necessario.

Liberation include un visualizzatore 3D integrato, sempre disponibile e indipendente dal livello della tua licenza. Puoi progettare e visualizzare in anteprima gli show direttamente in Liberation senza software esterni.

Capture è semplicemente un’opzione aggiuntiva se lo usi già per il lighting o per la progettazione di show.

### Risoluzione dei problemi

Se i laser non appaiono in Capture:

* Verifica che entrambe le applicazioni siano sulla stessa rete
* Controlla le impostazioni del firewall
* Assicurati che il laser sia armato in Liberation
