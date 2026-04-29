---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clip-editor/fundamentals/render-profile
---

# 🟩 Render profile

Hay un ajuste _Render Profile_ en cada nodo _Creator_, y este determina cómo se dibujan (o _renderizan_) las formas con los láseres.

**Para la mayoría de usos, el ajuste&#x20;**_**DEFAULT**_**&#x20;es perfectamente válido**. Pero si trabajas con gráficos o contenido complejo, puede que quieras tener más control sobre cómo se renderiza cada forma.

{% hint style="info" %}
A diferencia de la mayoría del software láser, Liberation genera un flujo de puntos en tiempo real, justo antes de enviarlo a los controladores láser. Esto te ahorra mucho espacio en disco: los clips ocupan solo unos pocos kB, en lugar de MB de flujos de puntos prerrenderizados.

También significa que puedes ajustar el mismo contenido para distintos tipos de escáneres, láser por láser, sin tener que modificar los propios clips.

Para más información, consulta [◼️ Cómo genera Liberation contenido láser](../../advanced/how-liberation-generates-laser-content.md "mention")
{% endhint %}

Hay tres _Render Profiles_ predefinidos: _DEFAULT_, _FAST_ y _DETAIL._

_**DEFAULT**_ - un buen perfil general, el más adecuado para la mayoría de casos

_**FAST** -_ si tu clip tiene mucho contenido y parte de él son puntos y líneas rectas muy simples, puede que obtengas menos parpadeo si eliges esta opción.

_**DETAIL**_ - si estás dibujando algo que necesita esquinas definidas, usa esta opción. Pero ten en cuenta que tus escáneres se moverán más despacio, lo que hará que la salida parpadee más.

{% hint style="info" %}
Dentro del editor de clips, puedes asignar creators a distintos perfiles de renderizado, pero cada láser procesará estos perfiles según sus ajustes de escáner. Consulta [◼️ Preajustes de escáner y perfiles de renderizado](../../advanced/scanner-presets.md "mention")
{% endhint %}
