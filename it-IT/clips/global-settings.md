---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clips/global-settings
---

# 🟩 Trasformazioni globali

Oltre alle trasformazioni dei clip (shift x/y, scale x/y), ci sono le Global Transformations, che si applicano a ogni clip che esegui. Apri il pannello _Global Transformations_ per visualizzarle. Questo pannello si trova di solito in una scheda accanto a _Clip Settings_.

Per impostazione predefinita, tutte queste impostazioni vengono reimpostate non appena non ci sono più clip in riproduzione. Puoi disattivare questo comportamento con il pulsante _AUTO RESET_ in basso nel pannello _Global Transformations_.

{% hint style="info" %}
Tieni presente che le Global Transformations non influiscono su nulla nel Canvas, ma solo sulle zone Beam e DMX
{% endhint %}

### Scale X/Y

Scala orizzontale e verticale: questi valori sono collegati tra loro, a meno che tu non prema `Shift`. Per impostazione predefinita, sono anche mappati sulle manopole APC40 Device Control 4 e 8 e compaiono nel pannello contestuale Parameters a destra del Clip Deck.

### Shift X/Y

Spostamento orizzontale e verticale. Trasla tutto in orizzontale / verticale.

### Spin

Fa ruotare tutti i contenuti attorno al centro. Un valore positivo ruota in senso orario, un valore negativo ruota in senso antiorario. Vedrai che questa impostazione influisce sulla trasformazione _Rotation_. Per impostazione predefinita, è mappata sulla manopola APC40 Device Control 3 e compare nel pannello contestuale Parameters a destra del Clip Deck.

### Spin 3D

Fa ruotare tutti i contenuti attorno all’asse Y (che è una linea verticale al centro). Vedrai che questa impostazione influisce sulla trasformazione _Rotation3D_. Per impostazione predefinita, è mappata sulla manopola APC40 Device Control 7 e compare nel pannello contestuale Parameters a destra del Clip Deck.

### Rotation

Una rotazione attorno al centro, con valore in gradi.

### Rotation 3D

Una rotazione attorno all’asse Y (che è una linea verticale al centro), con valore in gradi.

### Auto reset

Quando è attivo, reimposta tutte le Global Transformations non appena tutti i clip attualmente in esecuzione vengono disattivati. Così puoi essere sicuro di non avere sorprese la prossima volta che esegui un clip!
