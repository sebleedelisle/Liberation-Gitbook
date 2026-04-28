---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/graphics-and-the-canvas-system/canvas-target-areas
---

# 🟩 Áreas de destino del Canvas

Ya sabemos cómo llevar partes del canvas a zonas dentro de cada láser, pero para introducir contenido en el canvas en primer lugar necesitas las, con nombre algo confuso pero preciso, _Canvas target areas_.

Las áreas de destino del Canvas son secciones del canvas en las que puedes dibujar clips, y se muestran en la vista _CANVAS_ como rectángulos con contorno azul.

Muchas veces solo necesitarás una única área de destino del Canvas, y después dividirla en varias zonas que se envían a distintos láseres.

Y, a veces, quizá quieras usar varias áreas de destino del Canvas para diferentes partes de un edificio, o para aprovechar el retardo de zona entre ellas. (¡Sí! ¡El retardo de zona sigue funcionando entre áreas de destino del Canvas!).

### Enviar clips a áreas de destino del Canvas

Si miras en el Clip Deck, junto a los botones de beam zone, verás los botones de las áreas de destino del Canvas. Puede que tengas que desplazarte por los botones de salida para verlos; usa `Shift + Left / Right Arrow`, o los botones ZONE PAGE en pantalla, o los botones del APC40 (consulta [apc40-reference.md](../reference/apc40-reference.md "mention")).

Asigna clips a áreas de destino del Canvas activando estos botones exactamente del mismo modo que lo harías con los botones de beam zone.

### Añadir / editar áreas de destino del Canvas

En la barra de menú superior, selecciona _View -> Canvas Target Areas_: verás todos los ajustes de cada área de destino del Canvas que tengas en tu proyecto.

Y en la parte superior está el botón _ADD CANVAS TARGET AREA_.

Elimina un área de destino del Canvas con el botón rojo con el signo menos.

Ajusta el tamaño y la posición con los deslizadores. Haz doble clic en un deslizador para escribir un valor.

### Scale mode

* **FIT TO AREA** - reduce el contenido para que encaje por completo dentro del área de destino del Canvas, manteniendo la relación de aspecto. (Este es el ajuste predeterminado)
* **FILL AREA** - escala el contenido para llenar el área de destino del Canvas, manteniendo la relación de aspecto. Parte del contenido puede quedar recortada en los bordes.
* **STRETCH TO FIT** - estira el contenido para llenar toda el área de destino del Canvas, ignorando la relación de aspecto.
