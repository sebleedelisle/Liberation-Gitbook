---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/troubleshooting/intermittent-flashing-output
---

# ✅ Salida intermitente / parpadeante

Abre el panel _Laser Overview_ y mira la luz de conexión junto al láser con el que tienes problemas.

**Si la luz de conexión NO está constantemente en verde:**\
Entonces tienes un problema de red o de rendimiento de CPU:

**Rendimiento de red -**

* Asegúrate de que no estás conectado a una red wifi. Debes usar siempre una conexión por cable. Asegúrate de que tu sistema operativo da prioridad a la red cableada frente al wifi, o desactiva el wifi si no estás seguro.
* Comprueba tu adaptador de red y prueba con otro adaptador USB-C.
* Usuarios de Windows: comprueba/actualiza los drivers de red y ejecuta las herramientas de prueba de red adecuadas.
* Comprueba todo el cableado, switches y routers. Sustituye y prueba metódicamente cada cable.
* Reinicia todo tu equipo de red, incluidos switches, routers y cada Ether Dream.

**Rendimiento de CPU**

Si tienes un equipo antiguo o de bajas prestaciones, puede que sea demasiado lento para ejecutar Liberation. Comprueba el indicador de velocidad de fotogramas en el lado derecho de la barra de iconos.

Hay dos números: la velocidad de fotogramas real y la velocidad de fotogramas objetivo. Si la velocidad real cae por debajo de 30, es posible que tengas problemas.

Las siguientes acciones pueden ayudar:

* Elimina los láseres que no uses; por ejemplo, si solo tienes un láser conectado, borra los demás.
* Cambia a la vista Output o Canvas.
* Cierra todos los demás programas, comprueba la configuración del firewall de red y cierra antivirus, Dropbox, etc.
* Reduce la resolución de pantalla y haz más pequeña la ventana de Liberation.

Si nada de esto funciona, plantéate actualizar tu ordenador.

***

**Si la luz de conexión SÍ está constantemente en verde:**

Entonces es probable que se trate de un problema de hardware. Esto queda fuera del alcance de este manual, pero puedes probar las siguientes acciones:

* Desactiva el sistema SFS (Scan Fail Safety). Algunos láseres tienen una función que desactiva la salida si los scanners dejan de moverse, es decir, si producen un haz estático intenso. Pueden ser un poco demasiado cautelosos o poco fiables.

{% hint style="danger" %}
Ten muchísimo cuidado al desactivar el sistema scan fail safety. ¡Los haces estáticos intensos pueden provocar quemaduras! Asegúrate de tener a mano un botón de parada y un extintor.
{% endhint %}

* Comprueba los cables y sistemas de enclavamiento.
* Comprueba todo el cableado entre el controlador y el láser.

Un [ILDA Gem](https://shop.stanwaxlaser.co.uk/ilda-gem-pocket-2020-718-p.asp) puede ser una herramienta muy valiosa para solucionar problemas con láseres.
