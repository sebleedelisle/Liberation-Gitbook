---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clip-editor/fundamentals/colour-settings-and-hsb
---

# 🟩 Impostazioni colore e HSB

In Liberation il colore è definito in HSB anziché in RGB. All’inizio potrebbe sembrarti poco familiare, ma una volta che ci prendi la mano è un sistema molto più intuitivo.

{% hint style="info" %}
Se preferisci usare RGB, puoi fare clic sul quadrato del colore in qualsiasi impostazione colore. Si apre il pannello dell’editor colore, dove trovi opzioni per RGB e HSB.
{% endhint %}

### HSB - Hue, Saturation and Brightness

#### Hue

La tonalità del colore va da 0 a 255. 0 è rosso e, aumentando il valore, attraversi tutte le tonalità dell’arcobaleno: arancione, giallo, verde, ciano, blu, viola, magenta e poi di nuovo rosso a 255.

Dato che è un ciclo, puoi usare un’onda triangolare per scorrere tutti i colori.

#### Saturation

Questa impostazione regola la saturazione, cioè la vividezza del colore. In altre parole, quanto è _colorato_, con un intervallo da 0 a 255. Imposta la saturazione a 0 per i grigi e a 255 per i colori pieni dell’arcobaleno. Un valore intermedio produce colori pastello più spenti.

{% hint style="info" %}
Mi scuso con gli amici statunitensi per la vocale in più nella parola colour. Liberation è sviluppato in Inghilterra, quindi l’inglese britannico è l’impostazione predefinita. In futuro spero di offrire traduzioni in francese, spagnolo, tedesco, italiano, cinese semplificato e sì, persino in inglese americano. :innocent:
{% endhint %}

#### Brightness

Probabilmente è la più semplice da capire: 0 è completamente nero, 255 è la luminosità massima.

### Esempi d’uso

#### Ciclo arcobaleno :

Imposta _Brightness_ e _Saturation_ a 255. Collega un oscillatore _Sawtooth_ al socket _Hue_ e regola il suo intervallo da 0 a 255.

#### Luminosità pulsante :

Collega un oscillatore _Sawtooth_ al socket _Brightness_ e regola il suo intervallo da 255 a 0. Puoi anche regolare clamp min e max per controllare la durata del cambiamento. Poi usa le funzioni di easing per rifinire ulteriormente l’animazione.

#### Flash secco / strobo :

Seleziona un colore usando _Hue_ e _Saturation_ oppure facendo clic sul selettore colore. Collega un oscillatore _Square Wave_ al socket _Brightness_ e regola il suo intervallo da 255 a 0.

#### Ciclo su un intervallo personalizzato di tonalità :

Imposta _Brightness_ e _Saturation_ a 255. Collega un oscillatore _Triangle Wave_ al socket _Hue_ e regola il suo intervallo :

* per passare dal blu al ciano, usa un intervallo da 70 a 128
* per passare dal rosso al giallo, usa un intervallo da 0 a 40
* per passare dal rosso al magenta, usa un intervallo da 255 a 220
