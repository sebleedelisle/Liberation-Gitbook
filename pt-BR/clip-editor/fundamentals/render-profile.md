---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clip-editor/fundamentals/render-profile
---

# 🟩 Render Profile

Há uma configuração _Render Profile_ em cada nó _Creator_, e ela determina como as formas são desenhadas (ou _renderizadas_) pelos lasers.

**Para a maioria dos usos, a configuração&#x20;**_**DEFAULT**_**&#x20;é perfeitamente adequada**. Mas, se você estiver trabalhando com gráficos ou conteúdo complexo, talvez queira ter mais controle sobre como cada forma é renderizada.

{% hint style="info" %}
Ao contrário da maioria dos softwares de laser, o Liberation gera um fluxo de pontos em tempo real, logo antes de enviá-lo aos controladores de laser. Isso economiza muito espaço em disco: os clips têm apenas alguns kB, em vez de MB de fluxos de pontos pré-renderizados.

Isso também significa que você pode ajustar o mesmo conteúdo para diferentes tipos de scanner, laser por laser, sem precisar alterar os próprios clips.

Para mais detalhes, consulte [◼️ Como o Liberation gera conteúdo laser](../../advanced/how-liberation-generates-laser-content.md)
{% endhint %}

Há três _Render Profiles_ predefinidos: _DEFAULT_, _FAST_ e _DETAIL._

_**DEFAULT**_ - um bom perfil geral, ideal para a maioria das situações

_**FAST** -_ se o seu clip tiver muito conteúdo e parte dele for composta apenas por pontos simples e linhas retas, você pode ter menos cintilação ao escolher esta opção.

_**DETAIL**_ - se você estiver desenhando algo que precisa de cantos nítidos, use esta opção. Mas lembre-se de que seus scanners se moverão mais lentamente, deixando a saída com mais cintilação.

{% hint style="info" %}
No clip editor, você pode atribuir creators a diferentes render profiles, mas cada laser processará esses perfis de acordo com as respectivas configurações de scanner. Consulte [◼️ Predefinições de scanner e perfis de renderização](../../advanced/scanner-presets.md)
{% endhint %}
