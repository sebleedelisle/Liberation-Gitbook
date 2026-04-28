---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/troubleshooting/unable-to-deauthorise-on-windows
---

# ✅ Non riesci a rimuovere l’autorizzazione su Windows?

#### Non riesci a rimuovere l’autorizzazione su Windows?

Se non riesci a rimuovere l’autorizzazione di un computer su Windows, assicurati prima di tutto di rimuovere l’autorizzazione della licenza usando la stessa versione di Liberation con cui era stata autorizzata in origine, prima di autorizzarla di nuovo in una versione diversa.

Se questo non funziona e stai usando una versione precedente alla 1.0, il problema è probabilmente dovuto al modo in cui le vecchie build Windows di Liberation identificavano il computer. In quelle versioni, il sistema usato per generare l’ID macchina era meno affidabile e, in alcuni casi, l’ID poteva cambiare tra un riavvio e l’altro, anche se apparentemente non era cambiato alcun hardware.

Se non riesci a rimuovere l’autorizzazione e non hai cambiato versione, contatta support@liberationlaser.com e potremo rimuovere manualmente l’autorizzazione della macchina per te.

**Perché succede**

Nelle prime build Windows di Liberation (pre-1.0), usavamo il metodo di sistema consigliato da Windows per generare un ID macchina. Purtroppo, in alcune situazioni si è rivelato incoerente. Per questo motivo, il sistema di licenza è stato riscritto per la versione 1.0 usando una combinazione di metodi più robusta, che ora funziona in modo affidabile.

Di conseguenza, l’ID del computer usato dalle versioni più vecchie di Liberation può essere diverso da quello usato dalle versioni attuali. Se l’ID è già cambiato, la rimozione dell’autorizzazione deve essere gestita manualmente dal supporto.

***
