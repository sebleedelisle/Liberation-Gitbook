---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/dmx-control/dmx-zones
---

# ◼️ Zonas DMX

Las DMX zone son zonas de Output de Liberation que envían Art-Net/DMX en lugar de puntos láser. Aparecen junto a las beam zone y canvas zone, por lo que puedes asignar Clips a ellas con el mismo flujo de trabajo del selector de zone.

Abre **DMX Zones** desde el menú, o usa la sección DMX en Laser Overview, para gestionarlas.

* **ADD DMX ZONE** - crea una nueva DMX zone.
* **ARM** - activa la salida DMX para esa zone. Una DMX zone que no esté armada pone a cero sus canales asignados.
* **Node** - selecciona el número de node de Art-Net.
* **Universe** - selecciona el universo Art-Net. El valor mostrado empieza en 1, así que Universe 1 es el primer universo.
* **Address** - define la dirección inicial del fixture. El valor mostrado también empieza en 1.
* **Preset** - elige el preset DMX que asigna el contenido del Clip a los canales DMX.
* **Edit DMX zone settings** (icono de lápiz) - abre los ajustes de la zone, como el reenvío manual de zone y la orientación del fixture.
* **Edit DMX profile/channel mapping** (icono de deslizadores) - abre el editor de presets/canales DMX.
* **Delete** - elimina la DMX zone.

### Límites de armado

El número de DMX zone que pueden estar armadas al mismo tiempo depende de tu nivel de licencia. Si tu nivel no permite salida DMX, o ya has armado el número máximo de DMX zone, el botón **ARM** de las zones adicionales se desactiva y muestra un icono de prohibido al pasar el cursor por encima.

Desarma otra DMX zone, o usa un nivel de licencia con un límite DMX más alto, antes de armar más zones.
