---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clips/clip-settings
---

# ✅ Configurações do Clip

### Painel Clip settings

<figure><img src="../.gitbook/assets/clip-settings-clip-settings-panel" alt="" width="357"><figcaption><p>O painel Clip settings</p></figcaption></figure>

Altere o tamanho de saída do Clip usando _Scale X_ e _Scale Y_. Eles ficam vinculados, a menos que você pressione a tecla _SHIFT_.

Altere a posição horizontal e vertical do Clip usando _Shift X_ e _Shift Y_.

_Zone Delay/Chase_ é um recurso tão divertido que ganhou uma seção própria. [zone-delay-chase.md](zone-delay-chase.md)

### Bloqueio de Clips

Se um Clip estiver bloqueado, ele não pode ser movido nem excluído. Para bloquear um Clip, use a caixa de seleção _Locked_ no menu de clique com o botão direito. No painel Clip settings, você encontra mais algumas opções.

* _UNLOCK ALL -_ desbloqueia todos os Clips no Clip Deck.
* _AUTO-LOCK_ - quando _Auto-Lock_ está ativado, qualquer Clip reproduzido automaticamente (pela timeline ou pelo sistema de gravação/reprodução MIDI) será bloqueado. Isso é útil se você programou um show no Logic Pro (ou similar) e não quer editar acidentalmente os Clips usados no show.
* _LOCKED CLIPS ZONES_ - se esta opção estiver ativada, você não poderá alterar as zonas de nenhum Clip bloqueado.
* _LOCKED CLIPS PARAMS_ - se esta opção estiver ativada, você não poderá alterar os parâmetros (scale, shift etc.) de nenhum Clip bloqueado.

### Menu de clique com o botão direito

Se você clicar com o botão direito em um Clip, aparecerá um menu com algumas opções para esse Clip. Consulte [clip-editor-intro.md](../clip-editor/clip-editor-intro.md), [clip-settings.md](clip-settings.md) e [groups.md](groups.md) para saber mais sobre os primeiros itens desse menu.

<figure><img src="../.gitbook/assets/Screenshot 2025-01-14 at 11.22.48.png" alt="" width="322"><figcaption><p>O menu de clique com o botão direito de Clip settings</p></figcaption></figure>

### Retrigger

Por padrão, os Clips são configurados como _retrigger_. Isso significa que, independentemente de quando você acioná-lo, o Clip começará a rodar a partir daquele momento. Então, se você iniciá-lo atrasado, a animação do Clip também ficará um pouco atrasada e fora do tempo.

{% hint style="info" %}
Se você usar _Tap Tempo_ enquanto um Clip com retrigger estiver rodando, o sistema vai “quantizar” o Clip para ficar no tempo, mesmo que você não tenha iniciado exatamente no beat.
{% endhint %}

Se _Retrigger_ não estiver ativado, o Clip sempre ficará no tempo — é como se ele tivesse sido iniciado exatamente no começo do relógio. Isso é útil quando você está perfeitamente sincronizado com a música por meio de um sinal de clock externo.

{% hint style="info" %}
Os Clips muitas vezes são criados para rodar em loop para sempre, mas você pode configurá-los de modo que rodem apenas uma vez ou algumas vezes. Mantenha esses Clips configurados como _retrigger_; caso contrário, eles não serão reiniciados!
{% endhint %}

### Tempo de transição de entrada/saída (fade)

Os Clips podem ser configurados para fazer fade in e fade out com uma duração medida em segundos. Por padrão, o tempo de fade será herdado das configurações do grupo (e pode ser alterado clicando com o botão direito no botão do grupo).

Se você quiser uma duração de fade diferente da do grupo do Clip, primeiro desative o botão _USE GROUP DEFAULT_ e depois ajuste os controles deslizantes _In time_ e _Out time_ do Clip.
