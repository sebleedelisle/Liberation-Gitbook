---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/appendix-articles/scanner-specifications-and-liberation
---

# 🟩 Especificações de scanners e o Liberation

### A realidade confusa das especificações de scanners

Taxas de pontos e especificações de scanners podem ser um pouco confusas. Você verá com frequência especificações como 30kpps @ 8º ou 50kpps @ 4º, mas nem sempre é óbvio o que esses números realmente representam.

{% hint style="info" %}
Aviso - eu não sou especialista em hardware de scanners, mas tenho anos de experiência prática fazendo scanners de qualidades muito diferentes terem uma boa aparência por meio de software e geração de fluxo de pontos, em vez de ajuste de hardware. Isto se baseia nessa experiência.
{% endhint %}

#### **De onde esses números vêm**

Termos como “30K” e “50K” são abreviações baseadas em como os scanners são avaliados usando o padrão de teste ILDA nessas taxas de pontos, sob condições específicas.

Quando um scanner é anunciado como algo do tipo: _30Kpps @ 8°_, isso realmente significa:

> “Este scanner consegue reproduzir o padrão de teste ILDA a 30.000 pontos/s em um ângulo de varredura de 8°, quando ajustado corretamente.”

Não é uma medição abrangente nem totalmente padronizada do desempenho no mundo real. Na verdade, originalmente ele nem foi criado como um benchmark - era usado para um **procedimento de ajuste**. Você executa um padrão conhecido a uma taxa de pontos fixa (por exemplo, 30.000 pontos/s) e ajusta o amortecimento e o ganho até que ele fique correto.

Ainda assim, é a referência mais usada que temos, e pode dar uma boa ideia da qualidade dos scanners, pelo menos com fabricantes confiáveis. Já com os _menos confiáveis_...

#### Se você quiser testar os scanners conforme a classificação deles

{% hint style="danger" %}
**Esta é uma técnica avançada e você pode danificar seus scanners se não tiver cuidado. Não é recomendada a menos que você saiba o que está fazendo.**
{% endhint %}

Você precisará encontrar um software que consiga gerar o [ILDA Test Pattern](https://ilda.com/technical.htm?r=7950) - acho que o LaserShowGen talvez consiga fazer isso - e ajustar o tamanho da saída para corresponder ao ângulo de varredura especificado (por exemplo, 8°). Consulte a documentação da ILDA para orientações sobre como analisar a saída.

#### Por que talvez não seja um bom benchmark

Bem, antes de tudo, seu padrão de teste pode aparecer incorretamente mesmo que seus scanners sejam bons, porque eles não estão ajustados de uma forma otimizada para esse teste.

Ele pode ser um guia geral útil para diferenciar scanners "bons" de "ruins", mas às vezes os fabricantes tratam essas especificações de forma bem flexível.

#### Então, como escolho um bom scanner?

Acho que o principal é garantir que eles sejam fabricados por um fabricante confiável. Fabricantes caros de scanners de ponta, como Cambridge Technology (CT), Eye Magic (EMS) e ScannerMAX (uma subsidiária da Pangolin), são sempre bons e não tem erro. Mas quando um par de scanners custa por volta de US$1000, para muitos de nós que estamos começando isso é mais caro do que os próprios lasers!

Então, na maior parte do tempo, usei fabricantes chineses. Os scanners Dragon Tiger (DT) são decentes e acessíveis, e acho que a LightSpace os utiliza. Muitos outros fabricantes (incluindo OPT e Able em alguns modelos) também usam sistemas baseados em DT.

Os Phenix Technology (PT) geralmente ficam em uma categoria inferior, mas, sinceramente, provavelmente são suficientes para a maioria das coisas.

**Se seus scanners não têm marca, aí sim provavelmente é hora de se preocupar com qualidade!**

#### Como o Liberation ajuda

Bem, antes de tudo, para a maioria das coisas você não precisa de scanners realmente caros! DT de 30kpps acessíveis, ou até PT, vão dar conta. As configurações padrão de scanner são propositalmente conservadoras e, na maior parte dos casos, _você não deve precisar ajustá-las_ (com exceção de _Scanner sync_).

Mesmo que você tenha scanners melhores, não há motivo para forçá-los mais do que o necessário. Isso prolongará bastante a vida útil deles.

#### O que é um "fluxo de pontos"?

Você provavelmente já ouviu esse termo antes - é a forma como controlamos o caminho dos scanners.

Um fluxo de pontos é uma lista de posições X/Y, cada uma com uma cor. Para desenhar algo como uma linha branca, você envia uma sequência de pontos ao longo dessa linha, todos definidos como branco. Os scanners então se movem de ponto a ponto em uma taxa fixa - a taxa de pontos por segundo (PPS) - e o feixe traça a forma.

#### Como isso funciona em softwares de laser tradicionais

Softwares de laser tradicionais armazenam um fluxo de pontos para cada cue. Em cues animados, isso normalmente significa um fluxo de pontos separado para cada quadro. O ponto principal é que tudo é completamente predeterminado. Como resultado, aumentar a taxa de pontos faz os scanners se moverem mais rápido pelos mesmos dados predefinidos.

{% hint style="info" %}
Em softwares mais antigos, essa abordagem era necessária - os computadores simplesmente não eram rápidos o suficiente para gerar fluxos de pontos em tempo real. É por isso que normalmente existe um editor de cue separado, usado para pré-gerar os dados de cada quadro da animação.

Isso também explica por que o conteúdo pode ocupar gigabytes de espaço. Na prática, você está armazenando grandes formas de onda não compactadas em taxas de amostragem bem altas.
{% endhint %}

#### Por que "taxa de pontos" é menos significativa no Liberation

O Liberation gera o fluxo de pontos em tempo real, o que nos dá uma enorme flexibilidade. Observe a configuração "Scanner speed" no painel Laser Settings. Ela permite acelerar e desacelerar os scanners, mas, o mais importante, **não** altera a taxa de pontos (PPS) subjacente.

#### Espere, o quê? Como assim?

Eu sei, parece estranho no começo.

Como o Liberation gera o fluxo de pontos em tempo real, ele consegue ajustar esse fluxo. Quanto mais espaçados os pontos estiverem, mais rápido os scanners se movem. Quanto mais próximos eles estiverem, mais devagar os scanners se movem.

{% hint style="info" %}
Nas versões recentes do Liberation, a _taxa de pontos_ real (nas configurações avançadas) não afeta a velocidade dos scanners. Em vez disso, o renderizador ajusta a distribuição dos pontos para corresponder à taxa de pontos selecionada, mantendo o movimento dos scanners inalterado.

Isso afeta a "resolução" do caminho de pontos, mas essa diferença é mais relevante para gráficos (e pode ajudar em um ajuste mais fino da configuração _scanner sync_).
{% endhint %}

#### Ótimo! Então o que tudo isso realmente significa?

Boa pergunta. Aqui vão minhas dicas:

* Evite scanners sem marca. Se você puder usar scanners mais rápidos, use - no mínimo 30KPPS.
* Na maioria dos casos, scanners DT30 são suficientes, e scanners PT30 provavelmente funcionam bem em lasers mais baratos.
* Se você estiver trabalhando com gráficos, na maioria dos casos mais lasers serão melhores do que scanners mais rápidos.
* Quando você chegar a setups de nível mais alto, qualquer uma das marcas de ponta estabelecidas será adequada.
* Se você só conseguir os scanners sem marca mais baratos, as configurações padrão do Liberation são bem conservadoras e você provavelmente terá resultados aceitáveis para trabalho básico com feixes. Se houver dificuldade, reduza a configuração **Speed** (mas não altere a taxa de pontos!).

#### E o ILDA Test Pattern?

…continua sendo muito útil como ferramenta de calibração e referência, mas nunca foi criado como um benchmark abrangente e pode ser usado de forma incorreta ou interpretado de maneira flexível pelos fabricantes.
