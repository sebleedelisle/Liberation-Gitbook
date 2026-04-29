---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clips/zone-delay-chase
---

# 🟩 Zone delay / chase

Todos concordamos que mais lasers significam mais diversão, mas, se todos estiverem fazendo exatamente a mesma coisa, você deixa de aproveitar muitas possibilidades criativas.

O sistema de zone delay é um método simples e eficaz para criar variedade entre as zonas e aproveitar melhor uma configuração com vários lasers. Ele também pode ser usado para criar um efeito de chase mais tradicional.

#### Como funciona

_Zone delay_ adiciona um atraso ao tempo do clip em cada zona, criando uma espécie de varredura entre as zonas.

É muito eficaz aplicar zone delay a um clip que já está em execução, usando o controle correspondente no APC40 para ajustar o nível e o padrão. (Veja [Referência do APC40](../reference/apc40-reference.md)). Ou você pode usar o painel _Clip Settings_.

Configurações de Zone delay:

* **Zone delay** - controla a quantidade de tempo de atraso aplicada a cada zona, medida em notas de 1/64.
* **Pattern** - escolha a ordem das zonas
  * Left to right
  * Right to left
  * Inside to outside
  * Outside to inside

{% hint style="info" %}
O padrão funciona com base nos números das zonas e assume que suas zonas estão em ordem da esquerda para a direita. O Zone delay trata zonas do canvas e zonas DMX como grupos separados ao calcular os padrões.
{% endhint %}

* **Delay mode**
  1. No delay - use este modo em chase mode
  2. Delay - o modo padrão, atrasa o tempo de cada zona
  3. Delay with re-trigger - reinicia o clip do começo a cada passo do padrão. Isso funciona bem com _Chase mode_.
* **Chase mode** - com chase mode ativado, cada zona é ligada e desligada como em um efeito de chase tradicional. Ajuste a aparência do chase usando as configurações _Fade in, Hold,_ e _Fade out_. Essas configurações são definidas como uma proporção do valor de zone delay; portanto, um valor de 1 teria a mesma duração especificada em _Zone delay_. É um pouco difícil de explicar, então minha sugestão é você testar por conta própria.

{% hint style="info" %}
O Zone delay também é aplicado a qualquer efeito ativo. Por exemplo, um efeito de flash também será atrasado entre as zonas, assim como a animação dentro do próprio clip.
{% endhint %}

Quando um clip tem qualquer tipo de _Zone delay_, você verá um ícone de três pontos no canto superior direito do clip. Esses pontos são animados para mostrar o estilo de _Zone delay_ daquele clip. Veja [O que são os pequenos ícones nos botões de clip?](what-are-the-small-icons-on-the-clip-buttons.md) para mais detalhes.

<figure><img src="../.gitbook/assets/Screenshot 2025-01-21 at 10.00.14.png" alt=""><figcaption><p>O símbolo de três pontos que indica que um clip tem zone delay e mostra seu modo</p></figcaption></figure>

{% hint style="info" %}
Zone delay é uma configuração de cada clip; não é global. Ele faz parte do design criativo de um clip.
{% endhint %}
