---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/appendix-articles/scanner-specifications-and-liberation
---

# 🟩 Especificaciones de los scanners y Liberation

### La realidad poco ordenada de las especificaciones de los scanners

Las tasas de puntos y las especificaciones de los scanners pueden resultar algo confusas. A menudo verás especificaciones como 30kpps @ 8º o 50kpps @ 4º, pero no siempre es evidente qué representan realmente esos números.

{% hint style="info" %}
Aviso: no soy especialista en hardware de scanners, pero sí tengo años de experiencia práctica consiguiendo que scanners de calidades muy distintas se vean bien mediante software y generación de flujos de puntos, en lugar de mediante ajuste de hardware. Esto se basa en esa experiencia.
{% endhint %}

#### **De dónde salen estos números**

Términos como “30K” y “50K” son abreviaturas basadas en cómo se evalúan los scanners usando el patrón de prueba ILDA a esas tasas de puntos y en condiciones concretas.

Cuando un scanner se anuncia con algo como: _30Kpps @ 8°_, en realidad significa:

> “Este scanner puede reproducir el patrón de prueba ILDA a 30.000 puntos/s con un ángulo de escaneo de 8°, si está correctamente ajustado.”

No es una medición completa ni totalmente estandarizada del rendimiento en el mundo real. De hecho, originalmente ni siquiera se diseñó como benchmark: se usaba para un **procedimiento de ajuste**. Ejecutas un patrón conocido a una tasa de puntos fija (por ejemplo, 30.000 puntos/s) y ajustas la amortiguación y la ganancia hasta que se ve correctamente.

Aun así, sigue siendo la referencia más utilizada que tenemos, y puede darte una buena idea de la calidad de los scanners, al menos con fabricantes reputados. Aunque con los _menos reputados_...

#### Si quieres probar los scanners según su especificación

{% hint style="danger" %}
**Esta es una técnica avanzada y puedes dañar tus scanners si no tienes cuidado. No se recomienda salvo que sepas lo que estás haciendo.**
{% endhint %}

Tendrás que encontrar software que pueda emitir el [ILDA Test Pattern](https://ilda.com/technical.htm?r=7950) —creo que LaserShowGen quizá pueda hacerlo— y ajustar el tamaño de salida para que coincida con el ángulo de escaneo especificado (por ejemplo, 8°). Consulta la documentación de ILDA para obtener recomendaciones sobre cómo analizar la salida.

#### Por qué quizá no sea un buen benchmark

Para empezar, tu patrón de prueba podría mostrarse de forma incorrecta aunque tus scanners sean buenos, porque no están ajustados de una manera optimizada para ese patrón.

Puede ser una guía general útil para distinguir scanners "buenos" de "malos", pero a veces los fabricantes se toman bastantes libertades con estas especificaciones.

#### Entonces, ¿cómo elijo un buen scanner?

Creo que lo principal es asegurarte de que estén fabricados por un fabricante reputado. Los fabricantes de scanners caros de gama alta, como Cambridge Technology (CT), Eye Magic (EMS) y ScannerMAX (una filial de Pangolin), siempre son una buena opción y no te equivocarás. Pero cuando un par de scanners cuesta alrededor de 1000 $, para muchos de los que estamos empezando eso es más caro que nuestros láseres.

Así que, en la mayoría de los casos, he usado fabricantes chinos. Los scanners Dragon Tiger (DT) son decentes y asequibles, y creo que LightSpace los usa. Muchos otros fabricantes (incluidos OPT y Able en algunos modelos) también usan sistemas basados en DT.

Phenix Technology (PT) suele estar en un nivel inferior, pero sinceramente probablemente sean suficientes para la mayoría de las cosas.

**Si tus scanners no tienen marca, ahí es cuando probablemente deberías preocuparte por la calidad.**

#### Cómo ayuda Liberation

Para empezar, en la mayoría de los casos no necesitas scanners realmente caros. Unos DT de 30kpps asequibles, o incluso PT, funcionarán bien. Los ajustes predeterminados de scanner son deliberadamente conservadores y, en general, _no deberías tener que modificarlos_ (salvo _Scanner sync_).

Aunque tengas scanners mejores, no tiene sentido forzarlos más de lo necesario. Esto prolongará significativamente su vida útil.

#### Qué es un "flujo de puntos"

Probablemente ya hayas oído este término: es la forma en que controlamos la trayectoria de los scanners.

Un flujo de puntos es una lista de posiciones X/Y, cada una con un color. Para dibujar algo como una línea blanca, envías una secuencia de puntos a lo largo de esa línea, todos configurados en blanco. Los scanners se mueven entonces de un punto a otro a una velocidad fija —la tasa de puntos por segundo (PPS)— y el haz traza la forma.

#### Cómo funciona esto en el software láser tradicional

El software láser tradicional almacena un flujo de puntos para cada cue. En cues animados, eso suele significar un flujo de puntos independiente para cada fotograma. Lo importante es que todo está completamente predeterminado. Como resultado, aumentar la tasa de puntos hace que los scanners se muevan más rápido por los mismos datos predefinidos.

{% hint style="info" %}
En el software más antiguo este enfoque era necesario: los ordenadores sencillamente no eran lo bastante rápidos para generar flujos de puntos en tiempo real. Por eso normalmente hay un editor de cues independiente, usado para pregenerar los datos de cada fotograma de la animación.

Esto también explica por qué el contenido puede ocupar gigabytes de espacio. En la práctica, estás almacenando formas de onda grandes y sin comprimir a tasas de muestreo bastante altas.
{% endhint %}

#### Por qué "point rate" tiene menos sentido en Liberation

Liberation genera el flujo de puntos en tiempo real, lo que nos da una enorme flexibilidad. Fíjate en el ajuste "Scanner speed" del panel Laser Settings. Esto nos permite acelerar y ralentizar los scanners, pero es importante entender que **no** cambia la tasa de puntos subyacente (PPS).

#### Espera, ¿qué? ¿Cómo?

Lo sé, al principio suena raro.

Como Liberation genera el flujo de puntos en tiempo real, puede ajustar ese flujo de puntos. Cuanto más separados están los puntos, más rápido se mueven los scanners. Cuanto más juntos están, más despacio se mueven los scanners.

{% hint style="info" %}
En las versiones recientes de Liberation, la _point rate_ real (en los ajustes avanzados) no afecta en absoluto a la velocidad de los scanners. En su lugar, el renderizador ajusta la distribución de puntos para que coincida con la tasa de puntos seleccionada, manteniendo sin cambios el movimiento de los scanners.

Esto sí tiene un efecto sobre la "resolución" de la trayectoria de puntos, pero eso marca la diferencia sobre todo en gráficos (y puede ayudar a ajustar con más precisión el ajuste _scanner sync_).
{% endhint %}

#### ¡Genial! Entonces, ¿qué significa todo esto en la práctica?

Buena pregunta. Estos son mis consejos:

* Evita los scanners sin marca. Si puedes conseguir scanners más rápidos, hazlo: mínimo 30KPPS.
* En la mayoría de los casos, los scanners DT30 van bien, y los scanners PT30 probablemente sean aceptables en láseres más baratos.
* Si haces gráficos, en la mayoría de los casos será mejor tener más láseres que scanners más rápidos.
* Cuando llegues a configuraciones de gama más alta, cualquiera de las marcas de gama alta consolidadas funcionará bien.
* Si solo puedes conseguir los scanners sin marca más baratos, los ajustes predeterminados de Liberation son bastante conservadores y probablemente obtendrás resultados aceptables para trabajo básico con haces. Si le cuesta, reduce el ajuste **Speed** (¡pero no cambies la tasa de puntos!).

#### ¿Y el ILDA Test Pattern?

…sigue siendo muy útil como herramienta de calibración y referencia, pero nunca se diseñó como un benchmark completo y los fabricantes pueden usarlo mal o interpretarlo de forma laxa.
