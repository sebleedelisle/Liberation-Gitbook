---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clips/global-settings
---

# 🟩 Transformaciones globales

Además de las transformaciones de clip (shift x/y, scale x/y), hay Global Transformations que se aplican a cada clip que ejecutes. Abre el panel _Global Transformations_ para verlas. (Este panel suele estar en una pestaña junto a _Clip Settings_).

De forma predeterminada, todos estos ajustes se restablecen en cuanto deja de haber clips en reproducción. Puedes desactivar este comportamiento de restablecimiento con el botón _AUTO RESET_ en la parte inferior del panel _Global Transformations_.

{% hint style="info" %}
Ten en cuenta que Global Transformations no afecta a nada en el canvas, solo a las zonas Beam y DMX
{% endhint %}

### Scale X/Y

Escala horizontal y vertical. Estos valores están bloqueados entre sí salvo que pulses `Shift`. De forma predeterminada, también están asignados a los knobs 4 y 8 de APC40 Device Control y aparecen en el panel situado a la derecha del Clip Deck.

### Shift X/Y

Desplazamiento horizontal y vertical. Traslada todo horizontal o verticalmente.

### Spin

Gira todo el contenido alrededor del centro. Un valor positivo gira en sentido horario; un valor negativo gira en sentido antihorario. Verás que este ajuste afecta a la transformación _Rotation_. De forma predeterminada, está asignado al knob 3 de APC40 Device Control y aparece en el panel situado a la derecha del Clip Deck.

### Spin 3D

Gira todo el contenido alrededor del eje Y (que es una línea vertical en el centro). Verás que este ajuste afecta a la transformación _Rotation3D_. De forma predeterminada, está asignado al knob 7 de APC40 Device Control y aparece en el panel situado a la derecha del Clip Deck.

### Rotation

Una rotación alrededor del centro, con el valor en grados.

### Rotation 3D

Una rotación alrededor del eje Y (que es una línea vertical en el centro), con el valor en grados.

### Auto reset

Cuando está activado, restablece todas las Global Transformations en cuanto se desactivan todos los clips que se estén ejecutando. Así puedes tener la seguridad de que no tendrás sorpresas la próxima vez que ejecutes un clip.
