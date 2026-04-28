---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/timeline/synchronising-tempo-to-an-audio-track
---

# 🟩 Sincronizar el tempo con una pista de audio

<iframe src="https://www.youtube.com/embed/sL0SsuTf7Pc" title="Synchronising tempo to an audio track" style="width: 100%; aspect-ratio: 16 / 9; border: 0;" allowfullscreen></iframe>

La línea de tiempo de Liberation está diseñada para trabajar con tempos fijos o cambiantes, pero una sincronización fiable siempre empieza por encontrar el tempo y alinear correctamente el audio. Esta sección describe el flujo de trabajo recomendado.

#### 1. Alinear el primer tiempo fuerte

Añade tu pista de audio a la línea de tiempo y asegúrate de que esté ajustada a un pulso, de modo que el **primer tiempo fuerte musical** de la pista coincida exactamente con el inicio de un compás.

Este paso es fundamental.

Si el audio no empieza de forma natural en un tiempo fuerte, tienes dos opciones:

* **Ajustar el retardo del clip**\
  Haz clic con el botón derecho en el clip de audio y ajusta el valor Delay hasta que el primer tiempo fuerte coincida con un marcador de pulso o de compás.
* **Recortar el audio externamente**\
  Edita el archivo de audio en un editor externo, como Audacity, para que el archivo empiece exactamente en el primer tiempo fuerte y, después, impórtalo de nuevo.

{% hint style="info" %}
**Importante:**\
Si el inicio del audio no está alineado con un pulso o un compás, la posición inicial percibida de la música se desplazará hacia atrás y hacia delante al cambiar el tempo. Esto hace que ajustar el tempo con precisión sea extremadamente difícil.
{% endhint %}

#### 2. Definir un tempo inicial

Si tienes una idea aproximada del BPM, introdúcela en el control de tempo de la línea de tiempo e inicia la reproducción desde el principio.

Observa con atención los marcadores de pulso y de compás mientras se reproduce la pista.

* Si los marcadores se adelantan a la música, reduce ligeramente el tempo.
* Si se quedan por detrás, aumenta ligeramente el tempo.
* Detén la reproducción, ajusta el tempo y vuelve a probar.

En la mayoría de la música moderna, el tempo es un valor BPM entero fijo. Cuando encuentres el valor correcto, debería mantenerse sincronizado durante toda la pista.

#### 3. Usar la forma de onda como guía visual

La forma de onda del audio es una referencia útil para ajustar el tempo.

* Los transitorios y picos deberían alinearse con los marcadores verticales de compás.
* Haz zoom para comprobar la alineación a lo largo de varios compases.

**Consejo:**\
Usa la rueda del ratón o el gesto del trackpad para hacer zoom en la línea de tiempo. Usa la rueda de desplazamiento horizontal o el gesto correspondiente para moverte a izquierda y derecha. Trabajar con zoom facilita mucho los ajustes pequeños.

#### 4. Pistas con BPM no entero

Si la pista no usa un BPM entero, la desviación será más gradual.

* Haz más zoom.
* Usa ajustes de tempo más pequeños.
* Comprueba la alineación en secciones más largas de la pista, no solo en los primeros compases.

#### 5. Música con cambios de tempo

Si la música acelera o desacelera, usa el Tempo Map:

* Reproduce la pista y observa los marcadores de pulso.
* Cuando la desviación sea perceptible, añade un cambio de tempo en ese punto.
* Ajusta el tempo de la nueva sección hasta que vuelva a quedar sincronizada.

Repite este proceso para cada cambio de tempo de la música.

#### 6. Análisis externo del tempo (opcional)

Como último recurso, puedes analizar la pista en una DAW como Logic Pro y generar automáticamente un mapa de tempo. Ten en cuenta que esto suele producir un gran número de cambios de tempo, a veces uno por compás, lo que puede ser más detallado de lo necesario para la mayoría de los shows.
