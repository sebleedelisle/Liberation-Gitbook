---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clips/zone-delay-chase
---

# 🟩 Zone delay / chase

Todos estamos de acuerdo en que cuantos más láseres, más diversión; pero si todos hacen exactamente lo mismo, te estás perdiendo muchas posibilidades creativas.

El sistema de Zone delay es un método sencillo pero muy eficaz para introducir variedad entre zonas y sacar mucho más partido a una configuración con varios láseres. También puede usarse para crear un efecto de chase más tradicional.

#### Cómo funciona

_Zone delay_ añade un retardo al tiempo del clip en cada zona, creando una especie de barrido entre las zonas.

Es muy eficaz aplicar Zone delay a un clip que ya está en reproducción y usar el control correspondiente del APC40 para ajustar el nivel y el patrón. Consulta [Referencia de APC40](../reference/apc40-reference.md "mention"). También puedes usar el panel _Clip Settings_.

Ajustes de Zone delay:

* **Zone delay** - controla la cantidad de tiempo de retardo aplicada a cada zona, medida en notas de 1/64.
* **Pattern** - elige el orden de las zonas
  * Left to right
  * Right to left
  * Inside to outside
  * Outside to inside

{% hint style="info" %}
El patrón funciona con los números de zona y presupone que tus zonas están ordenadas de izquierda a derecha. Zone delay trata las zonas de Canvas y las zonas DMX como grupos separados al calcular los patrones.
{% endhint %}

* **Delay mode**
  1. No delay - usa este modo en chase mode
  2. Delay - el modo predeterminado; retrasa el tiempo de cada zona
  3. Delay with re-trigger - reinicia el clip desde el principio cada vez a lo largo del patrón. Funciona bien con _Chase mode_.
* **Chase mode** - con chase mode activado, cada zona se enciende y se apaga como en un efecto chase tradicional. Ajusta el aspecto del chase con los ajustes _Fade in, Hold,_ y _Fade out_. Estos ajustes se definen como una proporción del valor de Zone delay, así que un valor de 1 tendría la misma duración que la especificada en _Zone delay_. Es un poco difícil de explicar, así que mi consejo es que lo pruebes por ti mismo.

{% hint style="info" %}
Zone delay también se aplica a cualquier efecto activo. Por ejemplo, un efecto de parpadeo se retrasará entre las zonas, además de la propia animación dentro del clip.
{% endhint %}

Cuando un clip tiene cualquier tipo de _Zone delay_, verás un icono de tres puntos en la esquina superior derecha del clip. Estos puntos están animados para mostrarte el estilo de _Zone delay_ de ese clip. Consulta [¿Qué son los pequeños iconos de los botones de clip?](what-are-the-small-icons-on-the-clip-buttons.md "mention") para obtener más detalles.

<figure><img src="../.gitbook/assets/Screenshot 2025-01-21 at 10.00.14.png" alt=""><figcaption><p>El símbolo de tres puntos que indica que un clip tiene Zone delay y muestra su modo</p></figcaption></figure>

{% hint style="info" %}
Zone delay es un ajuste propio de cada clip; no es global, sino que forma parte del diseño creativo de un clip.
{% endhint %}
