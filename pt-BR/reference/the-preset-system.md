---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/reference/the-preset-system
---

# ✅ O sistema de Presets

O sistema de Presets aparece em vários lugares do Liberation sempre que é necessário armazenar várias configurações selecionáveis a partir de uma lista de _presets_.

Atualmente, esse sistema é usado para:

* Configurações de scanner
* Configurações de calibração de cor
* Configurações de câmera do 3D visualiser
* Configurações de laser do 3D visualiser
* Perfis DMX

Então, se você ajustar as configurações de scanner para seus novos scanners CT6210, pode salvar isso como um preset, chamá-lo de "CT6210", e ele ficará disponível na lista de presets sempre que você precisar no futuro, além de aparecer no menu suspenso.

Todos os presets são salvos junto com o seu projeto (ou configurações de laser), esteja você usando eles ou não. Portanto, sempre que você carregar um desses arquivos, todos os presets contidos nele serão adicionados aos seus presets existentes. Se um dos presets carregados tiver o mesmo nome de um preset existente, ele substituirá o preset existente.

Você também pode importar e exportar arquivos de preset usando o botão load/save (ícone de disquete) ao lado da lista suspensa de presets. Isso abre uma janela pop-up com botões de importação/exportação e também a opção de excluir um ou mais dos seus presets.

<figure><img src="../.gitbook/assets/scanner-settings-presets.png" alt=""><figcaption><p>O menu pop-up que abre quando você clica no ícone load/save</p></figcaption></figure>

Se você editar um preset, por exemplo a configuração de scanner chamada _Default_, observe que os outros lasers não serão atualizados automaticamente. Em vez disso, cada uma das configurações de scanner deles passará a aparecer como _Default(edited)_. Para atualizar isso para o novo preset _Default_, selecione-o novamente na lista suspensa.

{% hint style="info" %}
Se você tiver muitos lasers e quiser atualizar as configurações de scanner de todos eles, use o sistema _COPY LASER SETTINGS_. Consulte [copy-laser-settings.md](../setting-up/copy-laser-settings.md)
{% endhint %}

Se você excluir um preset que está sendo usado em outro lugar, a configuração não será perdida; em vez disso, ela aparecerá como _(deleted)._
