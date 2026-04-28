---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clip-editor/oscillators/sound-input-oscillator
---

# ✅ Oscillatore Sound input

## <img src="../../.gitbook/assets/sound-input-icon.png" alt="" data-size="line"> Sound input

Converte il livello dell'ingresso audio in un valore di proprietà.

{% hint style="info" %}
L'oscillatore Sound input usa l'interfaccia audio predefinita, ma puoi cambiarla in _Preferences_. Apri il menu _Liberation -> Preferences._

Nelle impostazioni _Sound Input_ puoi selezionare quale interfaccia audio vuoi usare, insieme ad alcune altre impostazioni per regolare il livello del volume.
{% endhint %}

* **range min / range max** - i valori minimo e massimo su cui viene mappata la forma d'onda
* **channel** - se la tua interfaccia audio ha più di un canale di ingresso, qui puoi selezionare quale vuoi usare.

{% hint style="info" %}
Una tecnica interessante è ricevere più segnali audio dal mixer: in questo modo puoi fare in modo che clip diverse reagiscano a strumenti musicali diversi.
{% endhint %}

{% hint style="info" %}
Puoi usare una sola interfaccia audio alla volta per tutti i _Sound Inputs_ (selezionata nel pannello _App Settings_). Se vuoi usare più di un'interfaccia per questo scopo, su macOS puoi [creare un Aggregate Device](https://support.apple.com/en-gb/HT202000) per combinare gli ingressi in un'unica sorgente audio virtuale. (Anche su Windows ci sono molte app che lo fanno, ma non le ho provate).
{% endhint %}

* **clamp min / clamp max** - usa questi valori per scegliere a quale intervallo di livelli vuoi rispondere. Non dovresti avere bisogno di modificarli se le impostazioni gate e limit (nel pannello _App Settings_) sono regolate correttamente, ma possono essere usati per alcuni effetti creativi.

{% hint style="info" %}
Vedrai una piccola icona a forma di microfono sul pulsante della clip ogni volta che contiene un oscillatore _Sound Input_.

<img src="../../.gitbook/assets/image (8).png" alt="" data-size="original">
{% endhint %}
