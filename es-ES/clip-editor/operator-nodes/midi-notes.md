---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clip-editor/operator-nodes/midi-notes
---

# 🟩 MIDI notes

## MIDI notes

Crea efectos de estilo “arpa láser”, donde las notas MIDI entrantes activan haces o formas a lo largo de un rango. El nodo usa como _fuente_ para cada nota el contenido que le pases: si le pasas un punto, obtendrás una fila de puntos. Si le pasas una forma como un círculo, obtendrás una fila de círculos; las formas más complejas se replicarán del mismo modo.

Puedes elegir la interfaz MIDI que Liberation escucha en **Liberation → Settings** (`Cmd / Ctrl + ,`)

* **midi channel** – canal MIDI que se va a escuchar (0 = todos los canales, 1–16 = canal específico).
* **width** – anchura total sobre la que se distribuyen las notas.
* **midi note min / max** – valores MIDI de la nota más baja y más alta del rango.
* **ignore out of range notes** – filtra cualquier nota que quede fuera del rango definido. Si está desactivado, las notas fuera de rango se "limitan" a la nota disponible más cercana (las notas altas activan la parte superior del rango y las bajas, la inferior).
* **auto extend range** – amplía automáticamente el rango si se tocan notas fuera de él.

{% hint style="info" %}
¿No tienes claro qué rango de notas estás recibiendo? Activa **auto extend range**, ajusta **midi note min** a un valor muy alto y **midi note max** a uno muy bajo, y luego toca tus notas. El sistema las capturará todas y ampliará el rango por ti. Cuando lo tengas todo, desactiva **auto extend range** para dejarlo fijado.
{% endhint %}

* **leave all notes visible** – crea haces o formas para todas las notas del rango, estén sonando o no, lo que produce un efecto de “arpa láser”.
* **hit colour** – color que aparece cuando se activa una nota.
* **hit colour hold time** – cuánto tiempo permanece el color de activación a brillo completo antes de empezar a desvanecerse. El valor está en segundos (0–1). _100% = 1 segundo._
* **hit colour decay time** – cuánto tiempo tarda el color de activación en desvanecerse después del tiempo de mantenimiento. El valor está en segundos (0–1). _100% = 1 segundo._

{% hint style="info" %}
Si tu contenido ya es blanco puro, ajustar el color de activación a blanco no producirá ningún cambio. Para obtener mejores resultados, usa un color saturado para tu contenido y ajusta el color de activación a blanco; así conseguirás un efecto de destello muy agradable cuando se activen las notas.
{% endhint %}

* **note off fade out time** – cuánto tarda la nota en desvanecerse después de soltarse. El valor está en segundos (0–1). _100% = 1 segundo._
* **hit scale factor** – cuánto aumenta la escala de la nota al activarse (por ejemplo, 2 = el doble de tamaño).
* **hit scale hold time** – cuánto tiempo permanece la nota ampliada antes de volver a reducirse. El valor está en segundos (0–1). _100% = 1 segundo._
* **hit scale decay time** – cuánto tarda la nota en volver a su tamaño original. El valor está en segundos (0–1). _100% = 1 segundo._
* **note off shrink time** – cuánto tarda en volver al tamaño original después de soltar la nota. El valor está en segundos (0–1). _100% = 1 segundo._ (No tiene efecto cuando **leave all notes visible** está activado.)

{% hint style="info" %}
Escalado: ten en cuenta que, si tu contenido es un único punto, el escalado no tendrá ningún efecto.
{% endhint %}
