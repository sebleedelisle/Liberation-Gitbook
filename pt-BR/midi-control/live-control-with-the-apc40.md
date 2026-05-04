---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/midi-control/live-control-with-the-apc40
---

# 🟩 Controladores MIDI ao vivo

<figure><img src="../.gitbook/assets/qs-apc40.jpeg" alt=""><figcaption></figcaption></figure>

### **Controlador APC40**

Este é o controlador de hardware padrão para o Liberation; ele é altamente recomendado, e é justo dizer que o Liberation foi projetado em torno desse hardware desde o início. Assim que você conecta o APC40, o Liberation se conecta a ele automaticamente.

{% hint style="warning" %}
_Ah, não! Meu cabo USB foi desconectado no meio de um show!_

Não entre em pânico: basta conectar de novo, e o Liberation vai se reconectar automaticamente, sem drama.
{% endhint %}

### APC40 Mark 1 ou Mark 2?

Resumindo, o Mark 2 é recomendado porque tem botões coloridos que correspondem melhor à interface do Clip Deck do Liberation. A versão Mark 1 funciona se for necessário, mas pode ser um pouco mais confusa, pois o layout é ligeiramente diferente do que aparece na tela, e os botões só podem ficar vermelhos, laranja ou verdes, então não vão corresponder às cores dos Clips.

{% hint style="info" %}
O APC40 Mark 1 original foi lançado em 2009(!), e algumas pessoas ainda o preferem pela construção com corpo de metal e pelo formato robusto, parecido com uma console. O Mark 2 atualizado foi lançado em 2014 e, embora tenha sido descontinuado em 2024, voltará a ser produzido em 2025 devido à demanda de artistas visuais (Resolume etc.) e laseristas.
{% endhint %}

Para ver a lista completa de controles disponíveis no APC40, consulte [Referência do APC40](../reference/apc40-reference.md "mention")

### APC Mini

O Liberation 1.0.3 também inclui um perfil para APC Mini. Ele mapeia a grade 8x5 de Clips, botões de zone, controles de inversão X/Y de zone, botões de grupo, parada de todos os Clips, movimentação de páginas de Clip, movimentação de páginas de zone, tap tempo, reinício de compasso e ajuste fino de tempo. Os faders controlam os níveis dos efeitos, e os faders com shift controlam os parâmetros dos efeitos. O último fader controla o brilho global.

### MIDI Fighter Twister

O perfil MIDI Fighter Twister é voltado para controle com muitos encoders, em vez de disparo de Clips. Uma fileira de encoders controla o parâmetro 1 dos slots de efeito 1 a 8, e outra fileira acompanha os oito controles contextuais do painel Parameters, incluindo deslocamento de Clip, atraso de zone, rotação/escala global e fades de grupo.
