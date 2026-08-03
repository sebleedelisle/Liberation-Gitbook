---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/faq
---

# ✅ Perguntas frequentes

## Hardware

#### **Liberation roda no Windows?**

Sim — o Liberation tem suporte completo a **Windows 10 e 11 (64 bits)**, com exatamente os mesmos recursos da versão para Mac. Todas as versões são lançadas simultaneamente para as duas plataformas.

#### **Liberation roda no Mac?**

Sim — o Liberation tem suporte completo a **Mac (macOS 12 Monterey ou posterior)**, com todos os recursos da versão para Windows. Todas as atualizações são lançadas juntas.

#### **Qual é a configuração mínima necessária?**

Depende de quantos lasers você quer controlar. Se você estiver usando apenas alguns lasers, uma máquina com especificações mais simples será suficiente. Qualquer Mac com Apple Silicon funciona muito bem e deve conseguir controlar até 100 lasers. Se você estiver executando shows complexos e críticos, recomendamos a melhor máquina que couber no seu orçamento.

#### **Quantos lasers posso controlar com o Liberation?**

O Liberation pode operar muitos e muitos lasers em um único computador. Ele já foi testado com mais de 100 lasers, então a resposta depende de:

* CPU do seu computador
* velocidade da rede
* nível da sua licença

#### **Quais controladores MIDI posso usar?**

O Liberation foi projetado e otimizado em torno do popular controlador MIDI APC40 Mk2. Ele também funciona com o APC40 Mk1. Consulte [Controladores MIDI ao vivo](midi-control/live-control-with-the-apc40.md)

O Liberation também tem suporte a APC Mini e MIDI Fighter Twister. O APC40 Mk2 ainda é o controlador de referência mais completo.

Também existe o sistema MIDI Send/Receive, que oferece controle MIDI adicional. Consulte [MIDI Send/Receive](midi-control/midi-send-receive.md)

Consulte [Controle MIDI](midi-control/) para mais informações.

#### **Posso usar qualquer controlador MIDI?**

Para outros controladores, use o sistema MIDI Send/Receive ou um tradutor MIDI que consiga enviar as mensagens MIDI padrão do Liberation. Procure orientações sobre essa configuração no [fórum](https://forum.liberationlaser.com), mas, na prática, o APC40 Mk2 ainda é a melhor opção para a maioria dos shows ao vivo.

## Controladores de laser

#### **Quais controladores de laser são compatíveis com o Liberation?**

* [Ether Dream (recomendado)](https://ether-dream.com)
* [Helios DAC](https://bitlasers.com/helios-laser-dac/)
* [Mercury by X-Laser](https://x-laser.com/pages/mercury-laser-control-system) (talvez você precise atualizar o firmware)
* LaserCube USB (e LaserDock)
* Protocolo de rede do LaserCube (com conexão cabeada)
* AVB usado por [lasers LASollinger](https://laseranimation.com/en/) (atualmente apenas em teste no macOS)

Consulte [Lasers e controladores compatíveis (DACs)](hardware/compatible-lasers-and-controllers-dacs.md) para mais informações

#### **Por que vocês não têm suporte a controladores de laser de \[outra marca]?**

Para incentivar uma maior interoperabilidade entre software e hardware, o Liberation só terá suporte a DACs que tenham um protocolo de comunicação publicado. Acredito que esse seja o melhor caminho para o setor de laser.

#### **Como posso saber se meu laser pode ser usado com o Liberation?**

Se o seu laser tiver um dos itens abaixo, você pode usá-lo com o Liberation:

* Uma **entrada ILDA** externa — um conector D de 25 pinos, usado com um controlador externo compatível.
* Um **Ether Dream** instalado internamente.
* Qualquer **LaserCube** (funciona com LaserCube USB e Wi-Fi).
* Uma **unidade X-Laser com sistema Mercury integrado** (em modo Ether Dream).
* Um **projetor LaserAnimation Sollinger com AVB integrado** (somente macOS, requer dispositivos de rede compatíveis com AVB, atualmente em teste).

Consulte [Lasers e controladores compatíveis (DACs)](hardware/compatible-lasers-and-controllers-dacs.md) para mais informações

#### **Posso usar o Liberation com meu LaserCube?**

Sim, o Liberation funciona diretamente com qualquer LaserCube. Consulte [LaserCube](hardware/lasercube.md)

## Licenças

#### **Qual é o preço de uma licença?**

Consulte a página da [loja](https://liberationlaser.com/shop) para ver os preços atuais.

#### **Quais são as limitações entre os níveis de licença?**

Consulte a página da [loja](https://liberationlaser.com/shop) para ver as opções de licença atuais.

Observe que você pode configurar, pré-visualizar e criar shows com quantos lasers quiser em **todos** os níveis, inclusive no gratuito, e não há nenhuma outra limitação além do número de lasers que você pode _armar_. Todos os outros recursos do Liberation estão disponíveis para todos.

#### **Posso fazer upgrade para um novo nível?**

Você pode fazer upgrade para um nível mais alto a qualquer momento. Você receberá um reembolso parcial pelo tempo restante do seu período pago atual, e seu novo nível de licença começará imediatamente. Consulte [Faça upgrade / downgrade da sua licença](installation/upgrade-downgrade-your-license.md)

#### **Posso fazer downgrade da minha licença?**

Você pode fazer downgrade a qualquer momento, mas a alteração entrará em vigor no final do período pago atual. Consulte [Faça upgrade / downgrade da sua licença](installation/upgrade-downgrade-your-license.md)

#### **Posso pausar os pagamentos da minha licença?**

Sim. A licença pode ser pausada na próxima data de assinatura e reiniciada a qualquer momento. Isso é útil se você começa e interrompe o uso periodicamente, e não precisa inserir novamente os dados do cartão. Consulte [Pausar ou cancelar pagamentos](installation/cancel-your-subscription.md)

#### **Como cancelo minha licença definitivamente?**

Você pode cancelar sua licença recorrente a qualquer momento, e ela será desativada automaticamente no final do período pago atual. Consulte [Pausar ou cancelar pagamentos](installation/cancel-your-subscription.md)

#### **Por que o Liberation usa assinatura?**

A versão curta é que isso mantém o Liberation sustentável, em desenvolvimento ativo e justo, ao mesmo tempo em que permite que todos abram, editem, salvem, pratiquem e pré-visualizem shows sem pagar.

Escrevi mais sobre a lógica por trás disso aqui: [Por que o Liberation usa assinatura](https://liberationlaser.com/articles/why-a-subscription).

#### **Posso obter uma licença perpétua ou de longo prazo para minha instalação / produção em turnê?**

Licenças pré-pagas anuais (ou até plurianuais) estão disponíveis para instalações permanentes e produções em turnê. Envie um e-mail para [billing@liberationlaser.com](mailto:billing@liberationlaser.com) se quiser configurar uma.

Licenças perpétuas não estão disponíveis no momento. Para mais contexto, consulte [Por que o Liberation usa assinatura](https://liberationlaser.com/articles/why-a-subscription).

#### **Como autorizo meu computador com a minha licença?**

Depois de comprar uma licença, você pode autorizar o computador dentro do próprio software Liberation. Você verá um botão _Authorise_ na tela _About_, que solicitará que você faça login no site. Siga as instruções na tela para concluir o processo de autorização. Consulte [Autorizar e desautorizar](installation/authorising-and-de-authorising.md)

#### **Com que frequência preciso conectar meu computador à internet?**

Toda vez que uma licença paga recorrente for renovada com sucesso, você precisará conectar o Liberation à internet para atualizar a licença interna. Portanto, para uma licença mensal com renovação automática, será necessário conectar todos os meses.

#### **O que acontece se eu não conseguir conectar meu computador à internet após o próximo pagamento?**

Para licenças pagas recorrentes mensais, o Liberation normalmente oferece um período de carência de 7 dias após a renovação da sua licença paga para que você se conecte à internet e atualize a licença interna. Depois desse período, o Liberation voltará ao modo _Free_.

#### **O que acontece se meu cartão de crédito expirar?**

Você receberá uma notificação por e-mail do nosso provedor de pagamentos e precisará atualizar os dados do cartão. Faça login no site e use _UPDATE CARD DETAILS_ na página da licença, ou _Update_ em _Billing and payments_. Você deve fazer isso dentro do período de carência para evitar perder o acesso aos recursos pagos.

#### **Em quantos computadores posso instalar o Liberation?**

Você pode instalar o Liberation em quantos computadores quiser. As autorizações de licença são necessárias apenas para habilitar a saída de laser/DMX, e o nível da sua licença determina quantos computadores podem ser autorizados para saída ao mesmo tempo. Consulte [Como funciona o licenciamento](installation/how-licensing-works.md)

#### **Como faço para mover minha licença de um computador para outro?**

* Abra o Liberation no computador que você não quer mais usar
* Verifique se você está conectado à internet e clique no botão _De-authorise this computer_ na tela _About_
* Agora abra o Liberation no novo computador
* Clique no botão _Authorise this computer_ na tela _About_.
* O site será aberto; faça login e siga as instruções na tela para concluir a autorização

Você também pode desautorizar remotamente um computador ao qual não tem mais acesso (com algumas limitações). Consulte [Autorizar e desautorizar](installation/authorising-and-de-authorising.md)

#### **Posso desautorizar o Liberation em um computador que foi perdido ou roubado?**

Você pode desautorizar o computador pelo site. Se a instalação do Liberation não ficou online desde a última atualização da licença, isso pode ser feito imediatamente.

Caso contrário, a desautorização entrará em vigor na próxima atualização da licença ou quando o computador se conectar à internet, o que ocorrer primeiro. Se você precisar reautorizar um novo computador com urgência, entre em contato com o suporte.

### Usando o Liberation

#### A configuração padrão tem 8 lasers — como altero isso?

Consulte [Configurar seu projeto](setting-up/setting-up-your-project.md) e [Adicionar/remover lasers](setting-up/adding-removing-lasers.md)

#### Posso copiar as configurações de zone de um laser para os outros?

Sim! Consulte [Copiar zones entre lasers](output-view/copy-zones-between-lasers.md)

#### Posso digitar um número em vez de usar um controle deslizante?

Sim. Clique no controle deslizante com `Cmd / Ctrl` pressionado e você poderá inserir o valor usando o teclado.

#### **Como sincronizo o Liberation com música?**

Ele tem um sistema inteligente de "tap tempo" que funciona como você esperaria, mas você também pode usar um clock MIDI externo ou Ableton Link. Consulte [Tempo/sincronização](tempo-synchronisation.md). A timeline pode ser sincronizada com timecode LTC/SMPTE recebido por qualquer interface de áudio. Consulte [Timecode](timecode.md).

#### Quais configurações preciso ajustar para obter a melhor saída do laser?

A principal configuração é _Scanner Sync_, que compensa o pequeno atraso entre o movimento dos espelhos e a alteração de brilho dos lasers. Se os pontos/feixes do seu laser tiverem pequenas "caudas", você precisará ajustar isso. (Veja as fotos na página [Painel Laser output settings](setting-up/laser-settings.md) para um exemplo de "caudas")

Você também pode tentar alterar a velocidade dos scanners: mais lenta se seus scanners forem básicos, ou mais rápida se forem bons. Mas **use com cautela, pois você pode danificar os scanners se forçar demais.**

Também existem algumas configurações predefinidas de scanner. A opção padrão é conservadora e adequada para a maioria das necessidades de feixes de laser. Mas há outros presets para scanners melhores, e também presets ajustados para gráficos.

Para mais informações, consulte [Painel Laser output settings](setting-up/laser-settings.md); para informações sobre como criar seus próprios presets, consulte [◼️ Presets de scanner e perfis de renderização](advanced/scanner-presets.md) (avançado, em andamento)

Você também pode corrigir o equilíbrio de cores usando as configurações de _Colour calibration_. Consulte [Calibração de cores](advanced/colour-calibration.md) (técnica avançada)

#### O que a configuração _Latency(ms)_ faz?

Esta é a latência de quadro, ou o tempo máximo entre um quadro ser gerado e depois enviado para um laser. Você não deve precisar ajustá-la, mas, se estiver com problemas de rede, pode tentar aumentá-la. Consulte [Configuração de latência](setting-up/latency-setting.md) para mais detalhes.

### Clips

#### Como ajusto zones e configurações de um Clip sem executá-lo?

Clique com `Alt / Option` pressionado para torná-lo o _Clip atualmente selecionado_, mas sem ativá-lo. Consulte também [Iniciar/parar Clips](clips/starting-stopping-clips.md)

#### Como copio Clips?

Clique e arraste mantendo a tecla `Alt / Option` pressionada. Consulte também [Organizando seu Clip Deck](clips/organising-your-clip-deck.md)

#### Como excluo Clips?

Clique neles e arraste-os para fora do Clip Deck. Consulte também [Organizando seu Clip Deck](clips/organising-your-clip-deck.md)

#### Como faço seleção múltipla, excluo, combino Clip Decks etc.?

Consulte [Organizando seu Clip Deck](clips/organising-your-clip-deck.md)

#### O que significam o pequeno símbolo de microfone e outros ícones no Clip?

Eles indicam que um Clip recebe entrada de som ou MIDI, e os 3 pontos indicam que há um atraso de zone. Consulte [O que são os pequenos ícones nos botões de Clip?](clips/what-are-the-small-icons-on-the-clip-buttons.md)
