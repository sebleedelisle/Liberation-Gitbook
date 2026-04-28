---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clip-editor/oscillators/sound-input-oscillator
---

# ✅ Oscilador Sound input

## <img src="../../.gitbook/assets/sound-input-icon.png" alt="" data-size="line"> Sound input

Converte o nível da entrada de som em um valor de propriedade.

{% hint style="info" %}
O oscilador Sound input usa a interface de som padrão, mas você pode alterá-la em _Preferences_. Abra o menu _Liberation -> Preferences._

Nas configurações de _Sound Input_, você pode selecionar qual interface de som deseja usar, além de algumas outras configurações para ajustar o nível de volume.
{% endhint %}

* **range min / range max** - os valores mínimo e máximo nos quais a forma de onda será mapeada
* **channel** - se a sua interface de som tiver mais de um canal de entrada, você pode selecionar aqui qual deles será captado.

{% hint style="info" %}
Uma técnica interessante é receber várias entradas de som da mesa de som. Assim, você pode fazer com que clips diferentes respondam a instrumentos musicais diferentes.
{% endhint %}

{% hint style="info" %}
Você só pode usar uma interface de som por vez em todos os _Sound Inputs (_&#x73;elecionados no painel _App Settings_). Se quiser usar mais de uma interface para isso, no macOS você pode [criar um Aggregate Device](https://support.apple.com/en-gb/HT202000) para combinar entradas em uma única fonte de som virtual. (Também há muitos apps no Windows que fazem isso, mas eu não os testei).
{% endhint %}

* **clamp min / clamp max** - use isto para escolher a faixa de níveis à qual você quer responder. Você não deve precisar ajustar isso se as configurações de gate e limit (no painel _App Settings_) estiverem ajustadas corretamente, mas elas podem ser usadas para alguns efeitos criativos.

{% hint style="info" %}
Você verá um pequeno ícone de microfone no botão do clip sempre que ele tiver um oscilador _Sound Input_.

<img src="../../.gitbook/assets/image (8).png" alt="" data-size="original">
{% endhint %}
