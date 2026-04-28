---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/hardware/compatible-lasers-and-controllers-dacs
---

# ✅ Lasers e controladores compatíveis (DACs)

### Quais lasers são compatíveis com o Liberation?

Se o seu laser tiver uma entrada ILDA padrão, você pode usá-lo com o Liberation (junto com um controlador de laser compatível, como o Ether Dream ou o Helios DAC - [veja a lista completa abaixo](compatible-lasers-and-controllers-dacs.md#compatible-laser-controllers)).

<figure><img src="../.gitbook/assets/helios-dac.png" alt="" width="563"><figcaption><p>O Helios DAC - a opção mais barata para uso doméstico</p></figcaption></figure>

Você não precisa de um controlador externo nem de uma entrada ILDA se:

* Seu laser tiver Ether Dream instalado internamente, ou;
* Você tiver um LaserCube da Wicked Lasers, ou;
* Você tiver um equipamento X-Laser com Mercury integrado, ou;
* Você tiver um laser Laser Animation Sollinger com controlador AVB integrado (atualmente em teste somente no macOS)

{% hint style="info" %}
**O que é um controlador de laser?**

Um controlador de laser (ou DAC) é um dispositivo de hardware que recebe os dados digitais do Liberation e os converte nos sinais analógicos necessários para controlar os scanners e a saída do seu laser. (Daí DAC: Digital to Analog Converter, ou conversor digital-analógico.)

O controlador se conecta ao seu computador via USB ou por uma rede de computadores padrão; ele pode ser um dispositivo externo ou estar instalado dentro do laser.

Se for externo, você o conecta ao laser pela conexão ILDA. ILDA é um padrão da indústria que usa um conector “D” antigo de 25 pinos. Pegue um cabo ILDA, conecte uma ponta ao controlador e a outra ao laser.
{% endhint %}

<figure><img src="../.gitbook/assets/etherdream-ilda.png" alt="" width="375"><figcaption><p>A saída ILDA em um Ether Dream externo</p></figcaption></figure>

<figure><img src="../.gitbook/assets/opt-laser-rear.jpg" alt="" width="317"><figcaption><p>O painel traseiro de um laser mostrando as várias conexões, incluindo a entrada ILDA</p></figcaption></figure>

<figure><img src="../.gitbook/assets/ilda-cable.jpg" alt="" width="375"><figcaption><p>Um cabo ILDA padrão</p></figcaption></figure>

### Qual controlador é melhor para mim?

Se você é usuário doméstico ou faz shows pequenos com 4 lasers ou menos, próximos ao computador, controladores USB como o **Helios DAC** são a opção **mais acessível**.

DACs de rede, como o **Ether Dream**, são a **melhor opção para profissionais** de laser que não se importam em configurar uma rede e querem controlar um grande número de lasers; todos os grandes shows com Liberation até agora foram executados com Ether Dreams.

Se você tem um **LaserCube**, não precisa de um controlador de laser separado - o Liberation é compatível com todos os LaserCubes. Os modelos mais antigos se conectam com um cabo USB, e os modelos mais novos se conectam pela rede.

Se você é profissional e procura a opção mais fácil, considere unidades X-Laser com Mercury integrado ou lasers Laser Animation Sollinger que usam AVB.

### Controladores de laser compatíveis

#### Ether Dream (rede)

O [Ether Dream](https://ether-dream.com) existe há mais de dez anos e atualmente está na versão 4 (embora o Liberation também funcione com Ether Dream versões 1, 2 e 3). Eles são extremamente confiáveis.

Você se conecta a eles por uma rede padrão. Eles podem ser comprados como unidades independentes ou, melhor ainda, podem ser instalados dentro dos lasers.

#### Helios (USB)

[Helios](https://bitlasers.com/helios-laser-dac/) é a melhor opção para iniciantes e é mais barato que os Ether Dreams, mas, como se conecta por USB, não é recomendado para cabos muito longos. Além disso, você pode ter problemas de dados USB e drivers quando conectar mais de 4 unidades (especialmente no Windows).

Mas, se você só quer controlar alguns lasers em casa, é a opção mais barata e simples.

#### Mercury (integrado a unidades X-Laser)

[**Mercury**](https://x-laser.com/pages/mercury-laser-control-system) é o poderoso sistema de controle de laser DMX da X-Laser, projetado para designers de iluminação que querem controlar lasers diretamente a partir de uma mesa de iluminação tradicional. Com a atualização de firmware mais recente, o Mercury também inclui **emulação de Ether Dream**, o que significa que agora funciona perfeitamente com o Liberation - além de qualquer outro software compatível com Ether Dream.

#### AVB (integrado a unidades Laser Animation Sollinger)

**AVB** é um protocolo aberto baseado em rede para streaming de áudio e dados de alto desempenho e baixa latência. Muitos projetores LaserAnimation Sollinger incluem suporte a AVB diretamente no hardware, o que permite que o Liberation se conecte a eles pela rede sem a necessidade de DACs externos. O suporte a AVB no Liberation atualmente é **somente para macOS e está em teste**, e requer **dispositivos de rede compatíveis com AVB**. Quando configurado corretamente, oferece um fluxo de trabalho mais simples, menos dispositivos externos e confiabilidade robusta para shows profissionais. I

#### Controladores que terão suporte no futuro:

* [IDN](http://www.ilda-digital.com) (um protocolo de rede aberto da ILDA, que pode ser implementado por qualquer fabricante)

### Sugestões de cabeamento

Para o melhor desempenho, mantenha os DACs USB próximos ao computador e conecte-os aos lasers usando cabos ILDA mais longos. (Mas tome cuidado, pois cabos ILDA podem agir como um gancho durante a desmontagem!)

Se você estiver usando Ether Dreams, ainda pode mantê-los todos juntos e conectá-los aos lasers usando cabos ILDA longos, ou pode montá-los próximos aos lasers e usar cabos de rede mais longos.

A configuração ideal é ter Ether Dreams (ou outros controladores) instalados diretamente dentro dos seus lasers (Rob, da Stanwax Laser, faz isso para você no Reino Unido)
