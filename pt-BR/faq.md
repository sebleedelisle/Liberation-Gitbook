---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/faq
---

# ✅ FAQ

## Hardware

#### **O Liberation roda no Windows?**

Sim — o Liberation tem suporte completo a **Windows 10 e 11 (64-bit)**, com exatamente os mesmos recursos da versão para Mac. Todas as versões são lançadas simultaneamente para as duas plataformas.

#### **O Liberation roda no Mac?**

Sim — o Liberation tem suporte completo a **Mac (macOS 12 Monterey e posterior)**, com paridade total de recursos em relação à versão para Windows. Todas as atualizações são lançadas juntas.

#### **Qual é a configuração mínima necessária?**

Depende de quantos lasers você quer controlar. Se você vai usar apenas alguns lasers, uma máquina mais simples deve ser suficiente. Qualquer Mac com Apple Silicon roda muito bem e deve conseguir controlar até 100 lasers. Se você vai executar shows complexos e críticos, recomendamos usar a melhor máquina que estiver ao seu alcance.

#### **Quantos lasers posso controlar com o Liberation?**

O Liberation pode operar muitos lasers em um único computador. Ele já foi testado com mais de 100 controladores de laser, então a resposta depende de:

* CPU do seu computador
* velocidade da rede
* tipo da sua assinatura

#### **Quais controladores MIDI posso usar?**

O Liberation foi projetado e otimizado em torno do popular controlador MIDI APC40 Mk2. Ele também funciona com o APC40 Mk1. Veja [Controle ao vivo com o APC40](midi-control/live-control-with-the-apc40.md "mention")

Liberation também tem suporte ao APC Mini e ao MIDI Fighter Twister. O APC40 Mk2 ainda é o controlador de referência mais completo.

Também existe o sistema MIDI Send/Receive, que oferece controle MIDI adicional. Veja [MIDI Send/Receive](midi-control/midi-send-receive.md "mention")

Veja [Controle MIDI](midi-control/ "mention") para mais informações.

#### **Posso usar qualquer controlador MIDI?**

Para outros controladores, use o sistema MIDI Send/Receive ou um tradutor MIDI que consiga enviar as mensagens MIDI padrão do Liberation. Procure no [fórum](https://forum.liberationlaser.com) orientações sobre essa configuração, mas, na prática, o APC40 Mk2 ainda é a melhor opção para a maioria dos shows ao vivo.

## Controladores de laser

#### **Quais controladores de laser são compatíveis com o Liberation?**

* [Ether Dream (recomendado)](https://ether-dream.com)
* [Helios DAC](https://bitlasers.com/helios-laser-dac/)
* [Mercury by X-Laser](https://x-laser.com/pages/mercury-laser-control-system) (talvez você precise atualizar o firmware)
* LaserCube USB (e LaserDock)
* Protocolo de rede LaserCube (com conexão cabeada)
* AVB, usado por [LASollinger lasers](https://laseranimation.com/en/) (atualmente apenas macOS, em testes)

Veja [Lasers e controladores compatíveis (DACs)](hardware/compatible-lasers-and-controllers-dacs.md "mention") para mais informações

#### **Por que vocês não dão suporte a controladores de laser de \[outra marca]?**

Para incentivar uma maior interoperabilidade entre software e hardware, o Liberation só dará suporte a DACs que tenham um protocolo de comunicação publicado. Acredito que esse seja o melhor caminho para o setor de laser.

#### **Como posso saber se meu laser pode ser usado com o Liberation?**

Se o seu laser tiver um dos itens abaixo, você pode usá-lo com o Liberation:

* Uma **entrada ILDA** externa — um conector D de 25 pinos, usado com um controlador externo compatível.
* Um **Ether Dream** instalado internamente.
* Qualquer **LaserCube** (funciona tanto com LaserCube USB quanto Wi-Fi).
* Uma **unidade X-Laser com sistema Mercury integrado** (em modo Ether Dream).
* Um **projetor LaserAnimation Sollinger com AVB integrado** (somente macOS, requer dispositivos de rede compatíveis com AVB, atualmente em testes).

Veja [Lasers e controladores compatíveis (DACs)](hardware/compatible-lasers-and-controllers-dacs.md "mention") para mais informações

#### **Posso usar o Liberation com meu LaserCube?**

Sim, o Liberation funciona diretamente com qualquer LaserCube. Veja [LaserCube](hardware/lasercube.md "mention")

## Licenças

#### **Qual é o preço de uma licença?**

Veja a página da [shop](https://liberationlaser.com/shop) para consultar os preços atuais.

#### **Quais são as limitações entre os níveis de licença?**

Veja a página da [shop](https://liberationlaser.com/shop) para consultar as opções de licença atuais.

Observe que você pode configurar, pré-visualizar e criar shows com quantos lasers quiser em **todos** os níveis, inclusive no gratuito, e não há nenhuma outra limitação além do número de lasers que você pode _armar_. Todos os outros recursos do Liberation estão disponíveis para todos.

#### **Posso fazer upgrade para um novo nível?**

Você pode fazer upgrade para um nível superior a qualquer momento. Você receberá um reembolso parcial pelo tempo restante da sua licença atual, e seu novo plano começará imediatamente. Veja [Faça upgrade / downgrade da sua licença](installation/upgrade-downgrade-your-license.md "mention")

#### **Posso fazer downgrade da minha licença?**

Você pode fazer downgrade a qualquer momento, mas a alteração entrará em vigor ao final do período da sua licença atual. Veja [Faça upgrade / downgrade da sua licença](installation/upgrade-downgrade-your-license.md "mention")

#### **Como autorizo meu computador com a minha licença?**

Depois de comprar uma licença, você pode autorizar o computador dentro do próprio software Liberation. Você verá um botão _Authorise_ na tela _About_, que solicitará que você faça login no site. Siga as instruções na tela para concluir o processo de autorização. Veja [Autorização e desautorização](installation/authorising-and-de-authorising.md "mention")

#### **Com que frequência preciso conectar meu computador à internet?**

Sempre que a licença for renovada, você precisará conectar o Liberation à internet para atualizar a licença interna. Para um pagamento recorrente mensal, será necessário conectar uma vez por mês.

#### **O que acontece se eu não conseguir conectar meu computador à internet após a renovação?**

O Liberation dará um período de tolerância de 7 dias após a renovação da sua licença para você se conectar à internet e atualizar a licença interna. Depois desse período, o Liberation voltará para o modo _Free_.

#### **O que acontece se meu cartão de crédito expirar?**

Você receberá uma notificação por e-mail do nosso provedor de pagamento e precisará atualizar o seu método de pagamento. Faça login no site e use o link _Update payment details_ na página de assinaturas.

#### **Como cancelo minha licença recorrente?**

Faça login no site, abra a página _Your subscriptions_, selecione a assinatura que deseja cancelar e clique no link _Cancel Subscription_. Você poderá continuar usando o Liberation pelo restante do período da licença.

#### **Em quantos computadores posso instalar o Liberation?**

Você pode instalar o Liberation em quantos computadores quiser. As autorizações de licença só são necessárias para habilitar a saída de laser / DMX, e o nível da sua licença determina quantos computadores podem ser autorizados para saída ao mesmo tempo. Veja [Como funciona o licenciamento](installation/how-licensing-works.md "mention")

#### **Como movo minha licença de um computador para outro?**

* Abra o Liberation no computador que você não quer mais usar
* Verifique se você está conectado à internet e clique no botão _De-authorise this computer_ na tela _About_
* Agora abra o Liberation no novo computador
* Clique no botão _Authorise this computer_ na tela _About_.
* O site será aberto; faça login e siga as instruções na tela para concluir a autorização

Você também pode desautorizar remotamente um computador ao qual não tem mais acesso (com algumas limitações). Veja [Autorização e desautorização](installation/authorising-and-de-authorising.md "mention")

#### **Posso desautorizar o Liberation em um computador que foi perdido ou roubado?**

Você pode desautorizar o computador pelo site. Se a instalação do Liberation não ficou online desde a sua última renovação, isso pode ser feito imediatamente.

Caso contrário, a desautorização entrará em vigor quando a assinatura for renovada ou quando o computador se conectar à internet, o que ocorrer primeiro. Se você precisar reautorizar um novo computador com urgência, entre em contato com o suporte.

### Usando o Liberation

#### A configuração padrão tem 8 lasers — como altero isso?

Veja [Configurando seu projeto](setting-up/setting-up-your-project.md "mention") e [Adicionar / remover lasers](setting-up/adding-removing-lasers.md "mention")

#### Posso copiar as configurações de zona de um laser para os outros?

Sim! Veja [Copiar zonas entre lasers](output-view/copy-zones-between-lasers.md "mention")

#### Posso digitar um número em vez de usar um slider?

Sim. Clique no slider com `Cmd / Ctrl` pressionado e você poderá inserir o valor usando o teclado.

#### **Como sincronizo o Liberation com a música?**

Ele tem um sistema inteligente de "tap tempo" que funciona como você esperaria, mas você também pode usar um clock MIDI externo ou Ableton Link. Veja [Tempo / sincronização](tempo-synchronisation.md "mention"). A timeline pode ser sincronizada com timecode LTC/SMPTE recebido por qualquer interface de áudio. Veja [Timecode](timecode.md "mention").

#### Quais configurações preciso ajustar para obter a melhor saída do laser?

A configuração principal é _Colour Shift_, que compensa o pequeno atraso entre o movimento dos espelhos e a alteração de brilho dos lasers. Se os pontos/feixes do seu laser tiverem pequenas "caudas", você precisará ajustar isso. (Veja as fotos na página [Painel de configurações de saída do laser](setting-up/laser-settings.md "mention") para um exemplo de "caudas")

Você também pode tentar alterar a velocidade dos scanners: mais lenta se seus scanners forem básicos, ou mais rápida se forem bons. Mas **use com cautela, pois você pode danificar seus scanners se forçá-los demais.**

Também existem algumas predefinições de scanner. A opção padrão é conservadora e adequada para a maioria das necessidades de feixes de laser. Mas há outras predefinições para scanners melhores, e também predefinições ajustadas para gráficos.

Para mais informações, veja [Painel de configurações de saída do laser](setting-up/laser-settings.md "mention"); e, para informações sobre como criar suas próprias predefinições, veja [◼️ Predefinições de scanner e perfis de renderização](advanced/scanner-presets.md "mention") (avançado, em andamento)

Você também pode corrigir o balanço de cor usando as configurações de _Colour calibration_. Veja [Calibração de cores](advanced/colour-calibration.md "mention")(técnica avançada)

#### O que a configuração _Latency(ms)_ faz?

Essa é a latência de frame, ou o tempo máximo entre um frame ser gerado e, em seguida, enviado para um laser. Você não deve precisar ajustá-la, mas, se estiver tendo problemas de rede, pode tentar aumentá-la. Veja [Configuração de latência](setting-up/latency-setting.md "mention") para mais detalhes.

### Clips

#### Como ajusto zonas e configurações de um clip sem executá-lo?

Clique com `Alt / Option` para torná-lo o _Clip selecionado no momento_, mas sem ativá-lo. Veja também [Iniciar / parar clips](clips/starting-stopping-clips.md "mention")

#### Como copio clips?

Clique e arraste mantendo a tecla `Alt / Option` pressionada. Veja também [Organizando seu Clip Deck](clips/organising-your-clip-deck.md "mention")

#### Como excluo clips?

Clique neles e arraste-os para fora do clip deck. Veja também [Organizando seu Clip Deck](clips/organising-your-clip-deck.md "mention")

#### Como faço seleção múltipla, excluo, combino clip decks etc.?

Veja [Organizando seu Clip Deck](clips/organising-your-clip-deck.md "mention")

#### O que indicam o pequeno símbolo de microfone e outros ícones no clip?

Eles servem para mostrar que um clip recebe entrada de som ou MIDI, e os 3 pontos indicam que há um atraso de zona. Veja [O que são os pequenos ícones nos botões de clip?](clips/what-are-the-small-icons-on-the-clip-buttons.md "mention")
