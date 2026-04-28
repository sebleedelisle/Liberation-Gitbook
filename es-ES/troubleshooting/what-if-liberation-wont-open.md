---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/troubleshooting/what-if-liberation-wont-open
---

# ✅ ¿Qué hacer si Liberation no se abre?

Es poco habitual, pero a veces Liberation puede no iniciarse o cerrarse justo después de abrirse. Casi siempre ocurre porque uno de los archivos de configuración locales se ha dañado, normalmente después de un fallo del sistema o de algo inesperado en tu ordenador.

Por suerte, se soluciona fácilmente restableciendo los ajustes locales. Aquí tienes cómo hacerlo en macOS y Windows.

> **Importante**
>
> * Cierra Liberation antes de hacer nada.
> * Estos pasos solo afectan a los ajustes locales, registros y cachés. Tu licencia y tu cuenta no se verán afectadas.

***

#### Dónde encontrar la carpeta de trabajo

Cada versión de Liberation tiene su propia carpeta de trabajo. Por ejemplo, si estás usando la versión 1.0.0, el nombre de la carpeta será 1.0.0.

* **macOS**: `~/Library/Application Support/Liberation/1.0.0`
* **Windows**: `AppData\Local\Liberation\1.0.0`

**Cómo abrir la carpeta rápidamente**

**macOS**

1. En Finder, pulsa **Shift + Cmd + G**.
2.  Pega esta ruta y pulsa **Enter**:

    ```
    ~/Library/Application Support/Liberation
    ```
3. Abre la carpeta que coincida con tu número de versión, por ejemplo `1.0.0`.

**Windows**

1.  Pulsa **Win + R**, pega esto y pulsa **Enter**:

    ```
    %LOCALAPPDATA%\Liberation
    ```
2. Abre la carpeta que coincida con tu número de versión, por ejemplo `1.0.0`.

> **Consejo para Windows**: Si navegas desde File Explorer, activa los elementos ocultos: **View > Show > Hidden items**.

***

#### Paso 1 – Restablece de forma segura tu archivo de ajustes

Dentro de la carpeta de tu versión, abre:

```
data/liberation/
```

Dentro de la carpeta liberation deberías encontrar un archivo llamado se`ttings.json`. Elimina este archivo.

* **Ejemplo en macOS**: `~/Library/Application Support/Liberation/1.0.0/data/liberation/settings.json`
* **Ejemplo en Windows**: `%LOCALAPPDATA%\Liberation\1.0.0\data\liberation\settings.json`

Ahora intenta iniciar Liberation. Si se abre, ya has terminado.

***

#### Paso 2 – Comprueba si hay un clip problemático

Si Liberation se cerró mientras estabas editando un clip, es posible que algo en ese archivo de clip esté causando el problema.

En la misma carpeta que tu archivo settings.json deberías encontrar un archivo llamado clipEdit`.json`

Haz una copia de seguridad de este archivo en un lugar seguro (por ejemplo, en tu Desktop) y después elimínalo de la carpeta de trabajo de Liberation.

Intenta iniciar Liberation de nuevo. Si ahora se abre con normalidad, envía por correo el archivo de copia de seguridad a [**info@liberationlaser.com**](mailto:info@liberationlaser.com) para que podamos investigar qué causó el problema.

***

#### Paso 3 - Haz una copia de seguridad y elimina toda la carpeta de trabajo

Si el Paso 1 y el Paso 2 no han ayudado:

1. **Haz una copia de seguridad** de toda la carpeta de la versión:
   * macOS: Haz clic derecho en la carpeta `1.0.0` y elige **Compress** para crear un zip, o cópiala en un lugar seguro como Desktop.
   * Windows: Haz clic derecho en la carpeta `1.0.0` y elige **Send to > Compressed (zipped) folder**, o cópiala en un lugar seguro como Desktop.
2. Después de hacer la copia de seguridad, **elimina** la carpeta `1.0.0` original de la ubicación de trabajo de Liberation.
3. Inicia Liberation de nuevo. Creará una carpeta de trabajo nueva.

Si Liberation se abre ahora, continúa con el Paso 4.

***

#### Paso 4 - Envíanos la copia de seguridad

Esto nos ayuda a identificar qué causó el problema para poder evitarlo en versiones futuras.

Comprime en zip tu **copia de seguridad** del Paso 3 si aún no lo has hecho y envíanosla por correo para que podamos diagnosticar la causa.

* **Para**: [info@liberationlaser.com](mailto:info@liberationlaser.com)
* **Asunto**: Liberation start-up fix - working folder backup
* **Cuerpo**: Incluye:
  * Sistema operativo y versión (por ejemplo, macOS 14.6 o Windows 11 23H2)
  * Versión de Liberation (por ejemplo, 1.0.0)
  * Qué paso lo solucionó, si alguno lo hizo (Paso 1, Paso 2 o Paso 3)
  * Una breve descripción de lo que ocurrió antes de que empezara el problema
* **Adjunto**: la copia de seguridad comprimida en zip de tu carpeta de trabajo `1.0.0`.

> Si el zip es demasiado grande para enviarlo por correo, súbelo a una unidad en la nube y comparte un enlace.

***

#### ¿Sigue sin iniciarse después del Paso 3?

Si Liberation sigue sin abrirse después de eliminar la carpeta de trabajo:

* Reinicia el ordenador e inténtalo de nuevo.
* Desactiva temporalmente el antivirus o las herramientas de seguridad que puedan bloquear la creación de carpetas nuevas y vuelve a intentar iniciarlo.
* Reinstala la versión más reciente de Liberation encima de la instalación existente.
* Si nada de lo anterior funciona, contacta con soporte en [**info@liberationlaser.com**](mailto:info@liberationlaser.com) con los detalles y cualquier registro de fallos de la subcarpeta `logs`, si existe.

***

#### Resumen

1. Elimina `data/liberation/settings.json` en tu carpeta de trabajo con versión.
2. Si estabas editando un clip, haz una copia de seguridad y después elimina `data/liberation/clipEdit.json`.
3. Si sigue sin abrirse, haz una copia de seguridad y después elimina toda la carpeta `1.0.0` (o la de tu versión).
4. Si el Paso 3 lo soluciona (o si no lo hace), comprime la copia de seguridad en zip y envíala a [**info@liberationlaser.com**](mailto:info@liberationlaser.com) con tu sistema operativo y la versión de Liberation.
