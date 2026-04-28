---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/reference/the-preset-system
---

# ✅ El sistema de presets

El sistema de presets aparece en varias partes de Liberation siempre que es necesario guardar varios ajustes seleccionables desde una lista de _presets_.

Este sistema se usa actualmente para:

* Ajustes de escáner
* Ajustes de calibración de color
* Ajustes de cámara del 3D Visualiser
* Ajustes de láser del 3D Visualiser
* Perfiles DMX

Así, si ajustas la configuración de escáner para tus nuevos CT6210, puedes guardarla como preset, llamarla "CT6210" y, a partir de entonces, estará disponible en la lista de presets siempre que la necesites y en el menú desplegable.

Todos los presets se guardan junto con tu proyecto (o con los ajustes de láser), tanto si los estás usando como si no. Por eso, cada vez que cargues uno de estos archivos, todos los presets que contenga se añadirán a tus presets existentes. Si uno de los presets cargados tiene el mismo nombre que uno de tus presets existentes, sobrescribirá el preset existente.

También puedes importar y exportar archivos de presets usando el botón de cargar/guardar (un icono de disquete) situado junto a la lista desplegable de presets. Esto abre una ventana emergente con botones para importar/exportar y también la opción de eliminar uno o varios de tus presets.

<figure><img src="../.gitbook/assets/scanner-settings-presets.png" alt=""><figcaption><p>El menú emergente que se abre al hacer clic en el icono de cargar/guardar</p></figcaption></figure>

Si editas un preset, por ejemplo el ajuste de escáner llamado _Default_, ten en cuenta que los demás láseres no se actualizarán automáticamente. En su lugar, los ajustes de escáner de cada uno aparecerán ahora etiquetados como _Default(edited)_. Para actualizarlos al nuevo preset _Default_, selecciónalo de nuevo en la lista desplegable.

{% hint style="info" %}
Si tienes muchos láseres y quieres actualizar todos sus ajustes de escáner, usa el sistema _COPY LASER SETTINGS_. Consulta [copy-laser-settings.md](../setting-up/copy-laser-settings.md "mention")
{% endhint %}

Si eliminas un preset que se usa en otro lugar, no perderás el ajuste; en su lugar, lo verás etiquetado como _(deleted)._
