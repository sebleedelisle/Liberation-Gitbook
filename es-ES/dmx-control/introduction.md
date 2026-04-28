---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/dmx-control/introduction
---

# ✅ Introducción

Liberation incluye un sistema DMX flexible y potente que te permite crear efectos de iluminación y controlar láseres compatibles con DMX mediante Art-Net. Está diseñado para que sea fácil mantener la iluminación sincronizada con tu show láser, sin necesidad de usar una mesa de luces aparte.

{% hint style="info" %}
**¿Qué es Art-Net y qué relación tiene con DMX?**

**DMX** es un sistema que se utiliza desde hace años para controlar luces, láseres, máquinas de humo y otros efectos escénicos. Envía señales de control a través de cables especiales, normalmente con conectores XLR, y cada aparato escucha un conjunto concreto de canales para saber qué tiene que hacer.

**Art-Net** es una forma más reciente de enviar esos mismos datos DMX a través de una red informática normal. En lugar de usar cables especiales, lo envía todo por Ethernet, igual que el tráfico de internet o de una red local.

En Liberation, toda la salida DMX se envía mediante Art-Net. Puedes usarlo para controlar directamente dispositivos compatibles con Art-Net, o puedes conectar un **nodo Art-Net**: una pequeña caja que convierte Art-Net de nuevo a DMX estándar. Esto significa que puedes seguir controlando luces y efectos DMX tradicionales, aunque no sean compatibles con Art-Net por sí mismos.
{% endhint %}

También puedes usarlo para controlar todo tipo de equipos escénicos, como máquinas de humo, máquinas de niebla, chorros de CO₂, máquinas de chispas frías y mucho más. Si es compatible con DMX, puedes configurarlo como una zona DMX y dispararlo directamente desde Liberation, junto con tu contenido láser.

Los aparatos DMX se añaden como **zonas DMX**, que aparecen en la lista de zonas junto a tus zonas de haces láser y áreas de destino del Canvas. Cada zona DMX utiliza un **preset DMX**, que indica a Liberation cómo asignar las propiedades de tus clips láser —como posición, color y brillo— a valores de canales DMX.

Cuando envías un clip a una zona DMX, Liberation toma el primer elemento del clip y convierte sus propiedades según el preset. Esto hace que sea sencillo controlar luces y efectos DMX directamente desde los mismos clips que ya estás usando para los láseres.

#### Liberation en Glastonbury

<figure><img src="../.gitbook/assets/show-arcadia-spider-2023.jpg" alt=""><figcaption></figcaption></figure>

La primera prueba real del sistema DMX de Liberation fue en Glastonbury 2023, donde Reach Lasers instaló un total de 90 fuentes de haz como parte del escenario "spider" de Arcadia.

18 láseres se controlaron con Ether Dreams internos, y otras 12 barras de haces de 6 cabezales se controlaron mediante Art-Net y DMX.
