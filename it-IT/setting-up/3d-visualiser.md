---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/setting-up/3d-visualiser
---

# ✅ 3D Visualiser

### Introduzione

Il 3D Visualiser di Liberation è una funzione estremamente utile: puoi progettare e rifinire i tuoi show senza bisogno di alcun laser! Per me si è rivelato uno strumento preziosissimo, soprattutto con setup particolarmente complessi e con molti laser.

### Muoversi nello spazio 3D

<figure><img src="../.gitbook/assets/White.png" alt=""><figcaption><p>La vista 3D Visualiser</p></figcaption></figure>

* Fai clic e trascina per ruotare la vista attorno al punto di orbita
* Usa la rotellina del mouse per avvicinarti o allontanarti dal punto di orbita
* Fai clic e trascina tenendo premuto il tasto shift per spostare lateralmente la camera (strafe) a sinistra, a destra, in alto e in basso lungo il piano XY
* Fai doppio clic in qualsiasi punto del visualiser per reimpostare la posizione della camera

### Settings

Apri il pannello _3D Visualiser Settings_ dal menu _Window_.

<figure><img src="../.gitbook/assets/Screenshot 2025-01-22 at 10.33.17.png" alt="" width="375"><figcaption><p>Il pannello 3D Visualiser Settings</p></figcaption></figure>

* **Visualiser size** - modifica la dimensione del visualiser rispetto al resto dell’app
* **Brightness Adjustment** - modifica la luminosità con cui vengono visualizzati i laser
* **Show laser numbers** - mostra il numero corrispondente sopra ogni laser
* **Show zone names** - mostra i nomi delle zone corrispondenti sotto ogni laser

### Camera settings

Queste impostazioni riguardano principalmente la camera virtuale nello spazio 3D. È disponibile un menu a discesa con preset per queste impostazioni, che puoi salvare e ricaricare.

* **Camera distance -** La camera è sempre puntata verso il suo _Orbit point_. La distanza della camera indica quanto è lontana da questo punto. Puoi regolare questa impostazione anche con la rotellina del mouse.
* **FOV -** Field of view: determina quanto la camera è grandangolare o zoomata.
* **Orbit position** - descrive la rotazione corrente attorno al punto di orbita. Il primo valore è la rotazione attorno all’asse X (pitch) e il secondo valore è la rotazione attorno all’asse Y (yaw).
* **Orbit centre point** - la posizione del punto di orbita nello spazio 3D, x, y, z.
* **Grid height** - l’altezza della griglia rispetto al “suolo” (cioè dove y = 0).

### Content settings

Queste impostazioni determinano dove vengono posizionati i laser (e il Canvas) all’interno dell’ambiente 3D. È disponibile un menu a discesa con preset per queste impostazioni, che puoi salvare e ricaricare.

#### Lasers

Ogni laser ha il proprio gruppo di impostazioni, che puoi espandere usando il piccolo triangolo bianco.

<figure><img src="../.gitbook/assets/Camera Visualiser Laser Settings.png" alt="" width="375"><figcaption><p>Impostazioni laser del 3D visualiser</p></figcaption></figure>

* **3D Position** - la posizione x, y e z del laser.
* **3D Orientation** - la rotazione del laser attorno a ciascuno degli assi x, y e z.
* **Flip X / Flip Y** - inverte l’output virtuale del laser. NOTA: non dovrebbe essere necessario; è meglio usare le impostazioni di flip/orientamento del laser per correggere eventuali incoerenze con il tuo hardware.
* **Output Range horizontal / vertical** - riguarda l’angolo massimo/minimo degli scanner del tuo laser. 60º è lo standard, ma puoi modificarlo se i tuoi laser sono diversi.

#### Canvas

Se usi il sistema canvas, puoi anche scegliere di includere l’immagine del canvas nella vista 3D. Attiva la checkbox per visualizzare il canvas e usa le impostazioni di posizione, orientamento e scala per definire come appare nella tua vista 3D.

<figure><img src="../.gitbook/assets/Camera Visualiser Canva Settings.png" alt="" width="375"><figcaption><p>Impostazioni canvas del 3D visualiser</p></figcaption></figure>

{% hint style="info" %}
Vedi laser “fantasma”? Il 3D Visualiser è in parte indipendente dal setup dei laser ed è possibile avere più laser nel visualiser di quanti ne siano presenti in Liberation. Quando aggiungi un laser al progetto, viene aggiunto anche un nuovo oggetto laser all’interno del visualiser. Se però elimini un laser, nel visualiser rimane comunque un oggetto laser “fantasma”.

Per rimuovere tutti i laser fantasma, fai clic sul pulsante _Remove extra 3D laser objects_ (in fondo al pannello delle impostazioni 3D Visualiser).

<img src="../.gitbook/assets/Remove extra 3D laser.png" alt="" data-size="original">
{% endhint %}
