---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/using-liberation-with-capture
---

# 🟩 Usar Liberation con Capture

Liberation admite [Capture](https://capture.se) como visualizador externo (a partir de la versión 1.0.3). Si ya usas Capture en tu flujo de trabajo, puedes utilizarlo para visualizar la salida láser en directo de Liberation dentro de tu escena 3D.

### Cómo funciona

No hace falta ningún proceso especial de conexión ni vinculación manual.

Siempre que:

* Liberation y Capture estén en la misma red
* Tu firewall permita la conexión

…todos los láseres que hayas configurado en Liberation aparecerán automáticamente dentro de Capture como fuentes multimedia. No necesitas configurar direcciones IP ni activar nada especial: simplemente aparecen.

### Ver láseres dentro de Capture

Todos los láseres configurados en Liberation aparecerán en Capture como fuentes multimedia disponibles.

Para ver realmente la salida:

* El láser debe estar armado en Liberation
* La fuente debe estar asignada a un dispositivo láser dentro de Capture

Una vez armado, Capture visualizará el flujo de salida en directo de Liberation. Si un láser se desarma en Liberation, seguirá siendo visible en Capture como fuente, pero no emitirá nada.

Consulta la documentación en [capture.se](https://www.capture.se/) para obtener más instrucciones y soporte sobre cómo configurar láseres en Capture. <br>

### Límites de licencia y láseres armados

Las conexiones de Capture se tratan exactamente igual que las salidas láser físicas.

Esto significa que:

* Solo puedes armar tantos láseres como permita tu nivel de licencia
* Solo los láseres armados enviarán datos activamente a Capture

### ¿Necesito Capture?

No, en absoluto.

Liberation incluye un visualizador 3D integrado, que siempre está disponible y no depende de tu nivel de licencia. Puedes diseñar y previsualizar shows directamente dentro de Liberation sin ningún software externo.

Capture es simplemente una opción adicional si ya lo usas para iluminación o diseño de shows.

### Solución de problemas

Si los láseres no aparecen en Capture:

* Comprueba que ambas aplicaciones estén en la misma red
* Revisa la configuración de tu firewall
* Asegúrate de que el láser esté armado en Liberation
