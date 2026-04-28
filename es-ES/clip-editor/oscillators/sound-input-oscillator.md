---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clip-editor/oscillators/sound-input-oscillator
---

# ✅ Oscilador de entrada de sonido

## <img src="../../.gitbook/assets/sound-input-icon.png" alt="" data-size="line"> Entrada de sonido

Convierte el nivel de la entrada de sonido en un valor de propiedad.

{% hint style="info" %}
El oscilador Sound input usa la interfaz de sonido predeterminada, pero puedes cambiarla en _Preferences_. Abre el menú _Liberation -> Preferences._

En los ajustes de _Sound Input_, puedes seleccionar qué interfaz de sonido quieres usar, además de otros ajustes para regular el nivel de volumen.
{% endhint %}

* **range min / range max** - los valores mínimo y máximo a los que se asigna la forma de onda
* **channel** - si tu interfaz de sonido tiene más de un canal de entrada, aquí puedes seleccionar cuál quieres captar.

{% hint style="info" %}
Una técnica interesante es obtener varias señales de sonido desde la mesa de mezclas; así puedes hacer que distintos clips respondan a distintos instrumentos musicales.
{% endhint %}

{% hint style="info" %}
Solo puedes usar una interfaz de sonido a la vez para todos los _Sound Inputs_ (seleccionada en el panel _App Settings_). Si quieres usar más de una interfaz para esto, en macOS puedes [crear un Aggregate Device](https://support.apple.com/en-gb/HT202000) para combinar entradas en una única fuente de sonido virtual. (En Windows también hay muchas aplicaciones que hacen esto, aunque no las he probado).
{% endhint %}

* **clamp min / clamp max** - usa esto para elegir a qué rango de niveles quieres responder. No deberías necesitar ajustarlo si los ajustes de puerta y límite (en el panel _App Settings_) están bien configurados, pero pueden usarse para algunos efectos creativos.

{% hint style="info" %}
Verás un pequeño icono de micrófono en el botón del clip siempre que tenga un oscilador _Sound Input_.

<img src="../../.gitbook/assets/image (8).png" alt="" data-size="original">
{% endhint %}
