---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/hardware/compatible-lasers-and-controllers-dacs
---

# ✅ Láseres y controladores compatibles (DACs)

### ¿Qué láseres son compatibles con Liberation?

Si tu láser tiene una entrada ILDA estándar, puedes usarlo con Liberation junto con un controlador láser compatible, como Ether Dream o Helios DAC. [Consulta la lista completa más abajo](compatible-lasers-and-controllers-dacs.md#compatible-laser-controllers).

<figure><img src="../.gitbook/assets/helios-dac.png" alt="" width="563"><figcaption><p>El Helios DAC: la opción más económica para uso doméstico</p></figcaption></figure>

No necesitas un controlador externo ni una entrada ILDA si:

* Tu láser tiene Ether Dream instalado internamente, o;
* Tienes un LaserCube de Wicked Lasers, o;
* Tienes un proyector X-Laser con Mercury integrado, o;
* Tienes un láser Laser Animation Sollinger con un controlador AVB integrado (actualmente en pruebas solo en macOS)

{% hint style="info" %}
**¿Qué es un controlador láser?**

Un controlador láser, o DAC, es un dispositivo de hardware que toma los datos digitales de Liberation y los convierte en las señales analógicas necesarias para controlar los escáneres y la salida de tu láser. De ahí DAC: Digital to Analog Converter.

El controlador se conecta a tu ordenador por USB o a través de una red informática estándar. Puede ser un dispositivo externo o estar instalado dentro del láser.

Si es externo, lo conectas a tu láser mediante la conexión ILDA. ILDA es un estándar del sector que utiliza un conector antiguo tipo “D” de 25 pines. Consigue un cable ILDA, conecta un extremo al controlador y el otro al láser.
{% endhint %}

<figure><img src="../.gitbook/assets/etherdream-ilda.png" alt="" width="375"><figcaption><p>La salida ILDA en un Ether Dream externo</p></figcaption></figure>

<figure><img src="../.gitbook/assets/opt-laser-rear.jpg" alt="" width="317"><figcaption><p>El panel trasero de un láser con las distintas conexiones, incluida la entrada ILDA</p></figcaption></figure>

<figure><img src="../.gitbook/assets/ilda-cable.jpg" alt="" width="375"><figcaption><p>Un cable ILDA estándar</p></figcaption></figure>

### ¿Qué controlador me conviene más?

Si eres usuario doméstico, o haces shows pequeños con 4 láseres o menos cerca del ordenador, los controladores USB como **Helios DAC** son la opción **más económica**.

Los DAC de red como **Ether Dream** son la **mejor opción para laseristas profesionales** que no tienen problema en configurar una red y quieren manejar un gran número de láseres. Todos los shows grandes de Liberation hasta ahora se han ejecutado con Ether Dreams.

Si tienes un **LaserCube**, no necesitas ningún controlador láser aparte: Liberation es compatible con todos los LaserCubes. Los modelos anteriores se conectan con un cable USB, y los modelos más recientes se conectan por red.

Si eres profesional y buscas la opción más sencilla, considera unidades X-Laser con Mercury integrado o láseres Laser Animation Sollinger que utilicen AVB.

### Controladores láser compatibles

#### Ether Dream (red)

[Ether Dream](https://ether-dream.com) lleva más de diez años en el mercado y actualmente está en la versión 4, aunque Liberation también funciona con Ether Dream versión 1, 2 y 3. Son extremadamente fiables.

Te conectas a ellos a través de una red estándar. Se pueden comprar como unidades independientes o, aún mejor, instalarse dentro de los láseres.

#### Helios (USB)

[Helios](https://bitlasers.com/helios-laser-dac/) es la mejor opción para principiantes y es más barato que Ether Dream, pero al conectarse por USB no se recomienda para tiradas de cable largas. Además, puedes tener problemas con los datos USB y los drivers cuando conectes más de 4, especialmente en Windows.

Pero si solo quieres manejar un par de láseres en casa, es la opción más barata y sencilla.

#### Mercury (integrado en unidades X-Laser)

[**Mercury**](https://x-laser.com/pages/mercury-laser-control-system) es el potente sistema de control láser DMX de X-Laser, diseñado para diseñadores de iluminación que quieren manejar láseres directamente desde una consola de iluminación tradicional. Con la última actualización de firmware, Mercury también incluye **emulación de Ether Dream**, lo que significa que ahora funciona perfectamente con Liberation, así como con cualquier otro software compatible con Ether Dream.

#### AVB (integrado en unidades Laser Animation Sollinger)

**AVB** es un protocolo abierto basado en red para transmisión de audio y datos de alto rendimiento y baja latencia. Muchos proyectores LaserAnimation Sollinger incluyen compatibilidad con AVB directamente en el hardware, lo que permite a Liberation conectarse a ellos por red sin necesidad de DAC externos. La compatibilidad con AVB en Liberation actualmente es **solo para macOS y está en pruebas**, y requiere **dispositivos de red compatibles con AVB**. Cuando está configurado correctamente, ofrece un flujo de trabajo más sencillo, menos dispositivos externos y una fiabilidad sólida para shows profesionales. I

#### Controladores que serán compatibles en el futuro:

* [IDN](http://www.ilda-digital.com) (un protocolo de red abierto de ILDA que puede implementar cualquier fabricante)

### Sugerencias de cableado

Para obtener un rendimiento óptimo, mantén los DAC USB cerca del ordenador y conéctalos a los láseres usando cables ILDA más largos. Aunque ten cuidado, porque los cables ILDA pueden comportarse como un gancho durante el desmontaje.

Si usas Ether Dreams, también puedes mantenerlos todos juntos y conectarlos a los láseres con cables ILDA largos, o puedes montarlos cerca de los láseres y usar cables de red más largos.

La configuración ideal es tener los Ether Dreams, u otros controladores, instalados directamente dentro de tus láseres. Rob, de Stanwax Laser, puede hacerlo por ti en el Reino Unido.
