---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clip-editor/fundamentals/fills-masks-and-depth-sorting
---

# 🟩 Rellenos, máscaras y ordenación por profundidad

### Trazos, rellenos y máscaras

Verás que algunos nodos Creator tienen una opción _Fill state_; puedes dibujarlos con un trazo (un contorno), como una máscara (tapando lo que hay debajo) o ambas cosas.

Cuando renderizas una forma como máscara, es como si estuviera rellena de negro, y todo lo que haya debajo quedará oculto.

{% hint style="info" %}
Dibujar una línea (o _trazo_) con un láser es bastante sencillo: escaneas el láser desde el principio de la línea hasta el final. ¡Y ahí tienes tu línea!

Las formas rellenas son más complicadas. Si quieres una forma rellena de color, podrías hacer un tramado manual dibujando líneas y rellenando, pero Liberation no puede hacerlo automáticamente (todavía). E incluso si lo hiciéramos, seguirías viendo las líneas que hay debajo a través del relleno.

Lo que sí podemos hacer es rellenar formas con _negro_. Internamente, Liberation hace todos los cálculos necesarios para eliminar el contenido que queda debajo de la forma rellena de negro. Y créeme, ¡tiene su miga!

Pero funciona muy bien y crea la ilusión de una forma rellena de negro.
{% endhint %}

### Ordenación por profundidad

Como algunas formas pueden _tapar_ otras, Liberation tiene que ordenarlas por su profundidad. De forma predeterminada, los elementos se ordenan por profundidad según su posición en z. Si están en la misma posición en z, se ordenan según su posición de capa, que puedes cambiar usando los botones _MOVE TO FRONT_ y _MOVE TO BACK_ dentro de cada Creator.
