---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/reference/the-preset-system
---

# ✅ Il sistema Preset

Il sistema Preset è presente in diverse aree di Liberation ogni volta che è necessario salvare più impostazioni selezionabili da un elenco di _preset_.

Attualmente questo sistema viene usato per:

* Impostazioni degli scanner
* Impostazioni di calibrazione colore
* Impostazioni della camera del 3D visualiser
* Impostazioni laser del 3D visualiser
* Profili DMX

Quindi, se configuri le impostazioni scanner per i tuoi nuovi CT6210, puoi salvarle come preset, chiamarlo "CT6210" e da quel momento sarà disponibile nell’elenco dei preset ogni volta che ti servirà in futuro, tramite il menu a discesa.

Tutti i preset vengono salvati insieme al tuo progetto (o alle impostazioni laser), che tu li stia usando o meno. Quindi, ogni volta che carichi uno di questi file, tutti i preset al suo interno verranno aggiunti ai preset esistenti. Se uno dei preset caricati ha lo stesso nome di uno dei preset già presenti, sovrascriverà quello esistente.

Puoi anche importare ed esportare file preset usando il pulsante load/save (l’icona del floppy disk) accanto all’elenco a discesa dei preset. Questo apre una finestra pop-up con i pulsanti di import/export e anche l’opzione per eliminare uno o più preset.

<figure><img src="../.gitbook/assets/scanner-settings-presets.png" alt=""><figcaption><p>Il menu pop-up che si apre quando fai clic sull’icona load/save</p></figcaption></figure>

Se modifichi un preset, ad esempio l’impostazione scanner chiamata _Default_, tieni presente che gli altri laser non verranno aggiornati automaticamente. Le rispettive impostazioni scanner verranno invece etichettate come _Default(edited)_. Per aggiornarle al nuovo preset _Default_, selezionalo di nuovo dall’elenco a discesa.

{% hint style="info" %}
Se hai molti laser e vuoi aggiornare tutte le loro impostazioni scanner, usa il sistema _COPY LASER SETTINGS_. Vedi [Copiare le impostazioni tra laser](../setting-up/copy-laser-settings.md)
{% endhint %}

Se elimini un preset usato altrove, non perderai l’impostazione: la vedrai invece etichettata come _(deleted)._
