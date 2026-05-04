---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/dmx-control/creating-dmx-zones
---

# 🟩 Crear zonas DMX

1. Conecta tu nodo Art-Net y configúralo siguiendo [Conectarse a un nodo Art-Net](../connecting-to-an-artnet-node.md "mention").
2. Abre **DMX Zones** y haz clic en **ADD DMX ZONE**.
3. Ajusta **Node**, **Universe** y **Address** de la zone para que coincidan con el fixture.
4. Elige un **Preset** para el fixture. El preset define qué canales DMX reciben valores fijos, valores de activación/desactivación de contenido, color RGB, posición X/Y, brillo o entradas DMX Value explícitas.
5. Haz clic en **Edit DMX profile/channel mapping** (icono de deslizadores) para editar el mapeo de canales. El preset predeterminado empieza con un canal de activación/desactivación de contenido y canales de color RGB.
6. Asigna Clips a la DMX zone del mismo modo que los asignas a beam zones o canvas zones.
7. Pulsa **ARM** cuando quieras que la zone empiece a emitir DMX.

{% hint style="warning" %}
Solo las DMX zones armadas envían valores en directo. Las DMX zones sin armar ponen a cero sus canales mapeados, lo que resulta más seguro al configurar fixtures.
{% endhint %}

La salida DMX también está limitada por tu nivel de licencia. Si el botón **ARM** está desactivado, comprueba si tu nivel incluye salida DMX o si ya se ha alcanzado el número máximo de DMX zones armadas.
