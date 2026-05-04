---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/dmx-control/creating-dmx-zones
---

# ◼️ Criando zonas DMX

1. Conecte seu Art-Net node e configure-o em [Conectar a um Art-Net node](../connecting-to-an-artnet-node.md "mention").
2. Abra **DMX Zones** e clique em **ADD DMX ZONE**.
3. Defina **Node**, **Universe** e **Address** da zone para corresponder ao fixture.
4. Escolha um **Preset** para o fixture. O preset define quais canais DMX recebem valores fixos, valores de conteúdo ligado/desligado, cor RGB, posição X/Y, brilho ou entradas explícitas de DMX Value.
5. Clique em **Edit DMX profile/channel mapping** (ícone de sliders) para editar o mapeamento de canais. O preset padrão começa com um canal de conteúdo ligado/desligado e canais de cor RGB.
6. Atribua Clips à DMX zone da mesma forma que você os atribui a beam zones ou canvas zones.
7. Pressione **ARM** quando você estiver pronto para que a zone envie DMX.

{% hint style="warning" %}
Somente DMX zones armadas enviam valores ao vivo. DMX zones desarmadas zeram os canais mapeados, o que é mais seguro ao configurar fixtures.
{% endhint %}

A saída DMX também é limitada pelo nível da sua licença. Se o botão **ARM** estiver desativado, verifique se o seu nível inclui saída DMX ou se o número máximo de DMX zones armadas já foi atingido.
