---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/setting-up/latency-setting
---

# ✅ Ajuste de latencia

En el panel _Settings_ (_Liberation->Settings_ o CMD/CTRL ,) verás un deslizador llamado _Latency(ms)._ (En versiones anteriores de Liberation estaba en el panel Laser Overview)

{% hint style="info" %}
El ajuste de latencia predeterminado de 150 ms debería ir bien en la mayoría de los casos, pero si tienes problemas de red puedes probar a aumentarlo.
{% endhint %}

### La explicación complicada

Este ajuste de “latencia de fotograma” es el tiempo máximo entre que Liberation crea un fotograma y el láser empieza a emitirlo. Si aumentas este valor, puede que notes un pequeño retraso entre Liberation y la salida del láser.

La ventaja de una latencia de fotograma más larga es que Liberation puede llenar los búferes de los controladores láser con contenido lo antes posible; si hay congestión en la red, es menos probable que el controlador se quede sin puntos.

Normalmente esto solo se aplica a DAC de red, y un ajuste de 100 ms debería ofrecer un buen equilibrio entre velocidad y protección frente a retrasos de red. Si tienes una red realmente sólida, deberías poder reducirlo a 50 ms.&#x20;
