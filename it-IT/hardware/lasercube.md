---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/hardware/lasercube
---

# ✅ LaserCube

<figure><img src="../.gitbook/assets/main-image-4.jpg.webp" alt=""><figcaption><p>Immagine promozionale di LaserCube per gentile concessione di Wicked Lasers</p></figcaption></figure>

Il [LaserCube](https://www.laseros.com/lasercube/) di Wicked Lasers è un’unità laser a batteria estremamente compatta, disponibile in diverse configurazioni di potenza. È molto popolare tra gli hobbisti grazie all’app per smartphone facile da usare, ma i modelli recenti sono abbastanza capaci da essere utilizzati anche in spettacoli professionali.

L’app per telefono (chiamata LaserOS, disponibile anche per desktop) si scarica gratuitamente, è molto divertente da usare ed è più che sufficiente per la maggior parte degli utenti. Ma se gestisci spettacoli più grandi con più laser, ti serve qualcosa di più specializzato e potente: ed è qui che entra in gioco Liberation.

### Collegare un LaserCube

I primi LaserCube sono controllati via USB, ma tutti i modelli attuali hanno un controller di rete integrato. Questi cube controllati via rete sono conosciuti come "LaserCube Wifi". Liberation supporta entrambi i tipi di LaserCube\*, sia collegati via USB sia tramite rete.

\*(Il supporto per il protocollo di rete LaserCube è stato introdotto nella versione 0.7.3)

### LaserCube USB

Collega il LaserCube al computer con un cavo micro USB, poi cercalo nel pannello _Controller Assignment_ (vedi [Assegnazione dei controller](../setting-up/controller-assignment.md)). Se non compare automaticamente, premi il pulsante _REFRESH_.

### LaserCube "Wifi" di rete

{% hint style="danger" %}
Anche se i cube "Wifi" sono progettati per funzionare su una rete wireless, questa configurazione non è consigliata: è probabile che si verifichino interruzioni e glitch. Usa invece la porta RJ45 per collegare il LaserCube a una rete cablata, proprio come faresti con gli Ether Dream.
{% endhint %}

Collega il LaserCube alla tua rete cablata.

Metti il LaserCube in modalità "LAN Client" e assicurati che ci sia un router sulla rete. Il LaserCube riceverà un indirizzo IP dal router e dovrebbe quindi comparire nel pannello _Controller Assignment_. (Vedi [Assegnazione dei controller](../setting-up/controller-assignment.md)).

{% hint style="info" %}
È possibile configurare una rete senza router e assegnare indirizzi IP fissi a tutti i dispositivi, ed è una pratica molto comune nel settore degli eventi. Personalmente preferisco aggiungere un router alla rete e consiglio questa opzione a chi ha meno esperienza con le reti.

Il router assegna dinamicamente un indirizzo IP a tutto: secondo me è più semplice e riduce il rischio di errori.
{% endhint %}

{% hint style="danger" %}
A differenza dell’Ether Dream, _**i LaserCube NON ESEGUONO IL BLANK DEL LASER**_ se incontrano un buffer under-run, un pacchetto perso o altri dati corrotti/non corretti.

Invece, continuano semplicemente dal punto in cui si erano fermati e, in alcuni casi, questo può far attraversare a un raggio attivo aree che non rientrano nelle zone e, cosa ancora peggiore, può farlo passare attraverso le maschere software.

Sto parlando con i progettisti/sviluppatori di LaserCube e spero che questo aspetto venga risolto in futuro con un aggiornamento firmware. Nel frattempo, però, devi assicurarti di mascherare fisicamente qualsiasi area in cui non vuoi che il laser arrivi.

A essere onesti, probabilmente dovresti farlo comunque, ma io stesso uso maschere software per proteggere videocamere e proiettori. Quindi tieni presente che farlo usando il protocollo di rete LaserCube è più pericoloso rispetto all’Ether Dream (che entra in una modalità di arresto di sicurezza non appena si verifica un errore o mancano dati).

Inoltre, l’ho già detto ma **usa una connessione cablata al LaserCube**. Il Wifi non è sufficiente e renderà questo problema ancora peggiore.
{% endhint %}
