# ✅ Painel de configurações Laser output

Abra o painel de configurações _Laser output_ pelo menu _View -> Laser Output Settings._

<figure><img src="../../.gitbook/assets/Copy Laser Setting in Laser Output.png" alt="" width="326"><figcaption></figcaption></figure>

Isso mostra as configurações do laser selecionado no momento, que você pode alterar:

* pelo botão de número correspondente no painel _Laser overview_
* com uma tecla numérica do seu teclado; as teclas 1 a 0 abrem os lasers 1 a 10
* com a tecla `Tab` para alternar entre os lasers (`Shift + Tab` volta para o anterior).

Na parte superior deste painel, você verá:

* um botão de número — clique nele para armar/desarmar este laser. Ele fica vermelho quando o laser está armado.
* um controle deslizante _Brightness_ somente para este laser. Observe que isso é combinado com o brilho global.
* alternância _Test Pattern_ e seletor de padrão. Isso permite escolher um padrão de teste específico somente para este laser. (Esses controles também aparecem na barra de ferramentas da visualização Output).

### Orientação da saída / correção de espelhamento

Os próximos elementos servem para corrigir a configuração do seu laser para que ele se comporte de forma consistente no Liberation.

* **Flip horizontal / vertical** — estas opções permitem corrigir a saída do seu laser

{% hint style="info" %}
Você não deve precisar alterar as configurações de flip horizontal / vertical, a menos que o laser tenha sido cabeado incorretamente ou tenha botões de flip X/Y na parte traseira que não estejam ajustados corretamente. Se você quiser que a saída fique invertida para um Clip específico, isso pode ser feito no próprio Clip.
{% endhint %}

* **Orientation** — se o laser foi montado de lado ou de cabeça para baixo, você pode corrigir a rotação com esta configuração.
* **Fine position adjustments** — pode ser usado para corrigir deslocamentos/rotações muito pequenos. Foi criado para corrigir desvio/acomodação caso um laser tenha ficado ligado durante a noite ou por longos períodos.

{% hint style="info" %}
Observe que as correções de orientação / espelhamento não alteram nada no 3D Visualiser; elas devem ser usadas para corrigir a saída do laser real para que corresponda ao que está no 3D Visualiser!
{% endhint %}

### Copy laser settings

Veja [#copy-laser-settings](./#copy-laser-settings).

### Scanner settings

<figure><img src="../../.gitbook/assets/Laser output scanner settings.png" alt=""><figcaption></figcaption></figure>

#### **Speed**

A configuração Speed determina a velocidade com que os scanners se movem.

{% hint style="danger" %}
Embora as configurações padrão sejam bastante conservadoras, você ainda pode danificar seus scanners se os acionar rápido demais. Tenha cuidado, especialmente ao aumentar a velocidade.
{% endhint %}

{% hint style="info" %}
Esta configuração Speed não altera a taxa de pontos; em vez disso, ela ajusta o quão espaçados esses pontos ficam. Para mais informações, veja [◼️ Como o Liberation gera conteúdo laser](../../advanced/how-liberation-generates-laser-content.md)
{% endhint %}

#### **Scanner sync (Colour shift / blank shift)**

O feixe muda de cor e liga/desliga enquanto os scanners o movimentam, e essas duas coisas geralmente não ficam perfeitamente sincronizadas entre si. Ajuste esta configuração para alinhá-las novamente.

{% hint style="info" %}
Isso às vezes é conhecido como _blank shift_, mas eu pessoalmente prefiro o termo _scanner sync_ — ele é um pouco mais preciso, pois ajusta o tempo de todas as mudanças de cor em relação ao movimento do scanner.
{% endhint %}

<div><figure><img src="../../.gitbook/assets/Colour shift tails.jpeg" alt="" width="320"><figcaption><p>“Caudas” no laser — Colour shift não configurado corretamente</p></figcaption></figure> <figure><img src="../../.gitbook/assets/Colour shift no tails.jpeg" alt="" width="320"><figcaption><p>Sem “caudas” no laser! Colour shift correto!</p></figcaption></figure></div>

Se você vir pequenas “caudas” na saída do laser, provavelmente o scanner sync precisa de ajuste. Se as caudas continuarem aparecendo de qualquer forma, é provável que você esteja acionando os scanners/drivers do laser mais rápido do que eles conseguem suportar. Tente reduzir a velocidade do scanner.

#### Scanner presets

Use isto para escolher uma configuração de scanner pré-definida. A opção padrão geralmente funciona bem, então você não deve precisar alterar esta configuração, a menos que tenha scanners especialmente ruins (ou bons). Se quiser se aprofundar, veja [◼️ Predefinições de scanner e perfis de renderização](../../advanced/scanner-presets.md)

#### Colour calibration

Você pode usar este sistema para corrigir a curva de brilho e o balanço de branco do seu laser. Veja [Calibração de cores](../../advanced/colour-calibration.md)

#### Advanced settings

Você não deve precisar mexer nisso, mas, se tiver curiosidade, veja [◼️ Configurações avançadas do laser](../../advanced/advanced-laser-settings.md)
