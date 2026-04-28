---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/hardware/lasercube
---

# ✅ LaserCube

<figure><img src="../.gitbook/assets/main-image-4.jpg.webp" alt=""><figcaption><p>Imagen promocional de LaserCube cortesía de Wicked Lasers</p></figcaption></figure>

El [LaserCube](https://www.laseros.com/lasercube/) de Wicked Lasers es una unidad láser extremadamente compacta alimentada por batería y disponible en varias configuraciones de potencia. Es popular entre aficionados por su app para smartphone, fácil de usar, pero los modelos recientes tienen capacidad suficiente para utilizarse en espectáculos profesionales.

La app para teléfono (llamada LaserOS, también disponible para escritorio) se descarga gratis, es muy divertida para probar y resulta suficiente para la mayoría de usuarios. Pero si trabajas en espectáculos más grandes con varios láseres, necesitas algo más especializado y potente; ahí es donde entra Liberation.

### Conectar a un LaserCube

Los primeros LaserCube se controlan por USB, pero los modelos actuales incorporan un controlador de red integrado. Estos cubos controlados por red se conocen como "LaserCube Wifi". Liberation es compatible con ambos tipos de LaserCube\*, tanto si están conectados por USB como por red.

\*(La compatibilidad con el protocolo de red de LaserCube se introdujo en la versión 0.7.3)

### USB LaserCube

Conecta tu LaserCube al ordenador con un cable micro USB y búscalo en el panel _Controller Assignment_ (consulta [controller-assignment.md](../setting-up/controller-assignment.md "mention")). Si no aparece automáticamente, pulsa el botón _REFRESH_.

### Network LaserCube "Wifi"

{% hint style="danger" %}
Aunque los cubos "Wifi" están diseñados para funcionar a través de una red inalámbrica, no es recomendable usarlos así: es probable que tengas cortes y fallos. En su lugar, usa el conector RJ45 para conectar tu LaserCube a una red cableada, igual que harías con Ether Dreams.
{% endhint %}

Conecta tu LaserCube a tu red cableada.

Pon tu LaserCube en modo "LAN Client" y asegúrate de que hay un router en tu red. El LaserCube obtendrá una dirección IP del router y debería aparecer en el panel _Controller Assignment_. (Consulta [controller-assignment.md](../setting-up/controller-assignment.md "mention")).

{% hint style="info" %}
Es posible configurar una red sin router y asignar direcciones IP fijas a todos tus dispositivos, y esto es muy habitual en el sector de eventos. Personalmente prefiero añadir un router a la red, y recomiendo esta opción a cualquiera que tenga menos experiencia con redes.

El router asigna dinámicamente una dirección IP a cada dispositivo; me parece más sencillo y menos propenso a errores.
{% endhint %}

{% hint style="danger" %}
A diferencia de Ether Dream, _**los LaserCube NO HACEN BLANKING DEL LÁSER**_ si se produce un buffer underrun, se pierde un paquete o llegan otros datos corruptos o incorrectos.

En su lugar, simplemente continúan desde donde se quedaron y, en algunos casos, esto puede hacer que un haz activo cruce zonas que no están dentro de las zonas definidas y, peor aún, que atraviese máscaras de software.

Estoy hablando con los diseñadores/programadores de LaserCube y espero que lo solucionen en el futuro con una actualización de firmware, pero mientras tanto debes asegurarte de enmascarar físicamente cualquier zona a la que no quieras que llegue el láser.

Para ser justos, probablemente deberías hacerlo de todos modos, pero yo uso máscaras de software para proteger cámaras y proyectores. Así que ten en cuenta que hacerlo con el protocolo de red de LaserCube es más peligroso que con Ether Dream (que entra en modo de parada de seguridad en cuanto hay cualquier error o falta algún dato).

Además, ya lo he dicho, pero **usa una conexión cableada con tu LaserCube**. El Wi-Fi no es suficiente y hará que este problema sea aún peor.
{% endhint %}
