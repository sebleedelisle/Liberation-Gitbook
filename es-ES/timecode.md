---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/timecode
---

# ✅ Timecode

Liberation admite la sincronización con una señal externa de timecode SMPTE/LTC, usada habitualmente en espectáculos de música en directo para mantener luces, pirotecnia, vídeo y pistas de acompañamiento perfectamente sincronizados.

{% hint style="info" %}
¿Qué es SMPTE/LTC?

SMPTE es un estándar de timecode, y LTC es ese timecode convertido en una señal de audio. Si escuchas este audio, suena como un chirrido agudo bastante desagradable, pero para los ordenadores es información de sincronización de alta resolución.

**¡Datos para frikis!**

Históricamente, SMPTE se ha usado para mantener sincronizados vídeo y audio. También, al sincronizar con cinta analógica, se grababa el audio de timecode en una pista, algo que a veces se llamaba "striping" de la cinta. Podías usar esa pista de timecode para mantener varias pletinas de cinta sincronizadas entre sí, o para mantener un secuenciador MIDI sincronizado con la cinta. (¡Así no tenías que grabar los instrumentos MIDI en cinta; podías hacer que el secuenciador los reprodujera en directo mientras mezclabas!)

SMPTE significa Society of Motion Picture and Television Engineers, la organización que definió el estándar. LTC significa _Linear TimeCode._
{% endhint %}

Puedes recibir una señal de timecode LTC a través de cualquier interfaz de sonido de tu ordenador, pero se recomienda usar una interfaz profesional con al menos una entrada XLR ajustable y capacidad de monitorización.

He tenido una buena experiencia con la [M-Audio 192/6](https://www.m-audio.com/audio-midi-interfaces/air-192-6.html), ya que tiene monitorización por auriculares, 2 entradas XLR y no necesita controladores especiales (al menos en macOS). Si solo vas a usarla para timecode, puedes comprar la [M-Audio 192/4](https://www.m-audio.com/audio-midi-interfaces/air-192-4.html), algo más barata (solo tiene una entrada y no tiene MIDI), pero, sinceramente, cualquier interfaz de sonido medianamente decente debería funcionar.

{% hint style="info" %}
Las señales de timecode LTC suelen distribuirse mediante cables XLR balanceados, ya que son lo bastante robustos para transmitir señales de audio de bajo nivel a largas distancias. (XLR es el conector cilíndrico que se suele usar con micrófonos)
{% endhint %}

### Conexiones de hardware

Conecta el cable XLR de la señal de timecode a tu interfaz de sonido y asegúrate de que recibes una buena señal. Ajusta el nivel en la interfaz de sonido hasta que la señal sea fuerte, pero sin saturar. Si tu interfaz de sonido tiene salida de auriculares, puedes escuchar el timecode y comprobar que no tenga cortes ni demasiado ruido.

{% hint style="info" %}
En teoría, es posible recibir la señal mediante la toma jack de tu MacBook, pero necesitarías un cable personalizado. Estas tomas suelen ser minijacks TRRS de 4 polos y, sinceramente, no tengo claro cuáles de esos conectores pueden usarse como entrada de audio. Tampoco estoy seguro del nivel de tensión que admiten (he leído en algún sitio que era +/-1V, ¡pero úsalo bajo tu propia responsabilidad!).

Creo que te irá mejor simplemente haciéndote con una interfaz de sonido USB barata en lugar de intentar esto.
{% endhint %}

Si tu interfaz de sonido no tiene ningún tipo de monitorización de entrada, puedes comprobar en los ajustes del sistema de macOS (en _Sound_) que estás recibiendo señal. (En Windows, usa el _Sound Control Panel_).

<figure><img src=".gitbook/assets/mac-mic-input-volume.png" alt=""><figcaption><p>macOS muestra el nivel de entrada de cualquier interfaz de sonido en el panel de ajustes del sistema Sound</p></figcaption></figure>

### Configuración en Liberation

1. Selecciona tu interfaz de sonido y el canal de entrada correcto en la ventana de ajustes de Timecode.

![](.gitbook/assets/timecode-panel.png)

{% hint style="info" %}
Ten en cuenta que hay opciones separadas en el menú desplegable para cada canal de entrada de tu interfaz de sonido.

<img src=".gitbook/assets/m-audio.png" alt="" data-size="original">
{% endhint %}

Fíjate en el cuadrado de la izquierda: si estás recibiendo una señal de timecode válida, se pondrá verde. Si no, estará rojo.

2. Selecciona la frecuencia de fotogramas correcta para el timecode entrante. La persona que te proporcione el timecode debería poder decirte cuál es la frecuencia de fotogramas. (Si te equivocas, seguirá sincronizando, pero notarás un pequeño "salto" cada segundo)
3. Abre los ajustes de timecode de la Timeline usando el pequeño icono de reloj de la barra de la timeline y elige la opción SMPTE(LTC).

<figure><img src=".gitbook/assets/timeline-settings.png" alt=""><figcaption></figcaption></figure>

4. Ajusta el desplazamiento inicial (en horas, minutos, segundos y fotogramas) para que coincida con el inicio de la canción. Si tienes varias timelines, tendrás que configurar estas opciones por separado en cada una.

{% hint style="info" %}
En el mundo de las giras, es habitual que cada canción empiece en una hora distinta, por ejemplo 01:00:00:00 para la primera canción, 02:00:00:00 para la segunda, y así sucesivamente.

Liberation cambiará automáticamente a la timeline correspondiente según el timecode, así que nunca tendrás que cambiar de timeline manualmente durante un show.
{% endhint %}

Ten en cuenta que, a diferencia de MIDI Clock y Ableton Link, SMPTE es un sistema de tiempo _absoluto_, medido en horas, minutos, segundos y fotogramas. El sistema de tiempo principal de Liberation se basa en tiempos y compases, así que cuando reciba timecode usará el tempo configurado en la timeline. Tendrás que asegurarte de que ese tempo esté sincronizado con cualquier música que también esté sincronizada con el timecode.
