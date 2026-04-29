---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/loading-and-saving
---

# 🟩 Carregar e salvar

O Liberation salva constantemente seu estado no disco. Assim, se houver uma queda de energia ou algum problema no sistema, ele será iniciado exatamente de onde parou. Você não deve perder suas zonas, linhas do tempo ou outros conteúdos.

Ainda assim, você pode exportar sua configuração para backup e para transferi-la para outro computador.

### Importar/Exportar projeto

O arquivo de projeto armazena quase tudo na sua configuração atual, incluindo:

* Tudo o que está detalhado em [Carregar e salvar](loading-and-saving.md#laser-settings-import-export) abaixo
* Clips, efeitos e configurações de grupos
* Todas as suas linhas do tempo (sem incluir mídia de áudio e vídeo)
* Configuração de ArtNet
* Configurações de envio/recebimento MIDI
* Configurações de tempo / sincronização

Atualmente, ele não salva nem carrega:

* Configurações de entrada de som e MIDI usadas no node MIDI notes e no Sound Input Oscillator (ele _salva_ as configurações de envio/recebimento MIDI, assim como a entrada de som de timecode)
* Escala da interface
* Mídia para imagens-guia do Canvas
* Mídia de som e vídeo para linhas do tempo
* Fontes usadas no node Text

{% hint style="danger" %}
Arquivos de som e vídeo na linha do tempo não são salvos com arquivos de projeto. Portanto, salve-os separadamente se quiser transferi-los para outro computador. Veja [Carregar e salvar](loading-and-saving.md#important-note-about-timeline-media-files)
{% endhint %}

### Importar / Exportar configurações de laser

* Configurações de laser para todos os lasers
* Zonas de feixe
* Áreas-alvo do Canvas
* Zonas DMX
* Atribuição de controladores de laser (e aliases de qualquer controlador que você tenha renomeado)
* Configurações e presets de calibração de scanner e cor dos lasers
* Configurações e presets do 3D Visualiser

### Importar / Exportar Clip Deck

* Todos os clips e suas atribuições de zona, configurações e parâmetros
* Todas as configurações de grupo, flash mode, tempos de fade in/out etc.

Atualmente, ele não salva nem carrega:

* Todos os efeitos e seus parâmetros e configurações

{% hint style="info" %}
**Carregar clips de um arquivo de projeto sem carregar o projeto inteiro**

Para importar apenas os clips de um projeto, selecione _**Clips->Import Clip Deck**_ e, em vez de selecionar um arquivo de clip deck (.cpdk), escolha um arquivo de projeto.
{% endhint %}

### Acrescentar Clip Deck

Você pode adicionar clips de um arquivo de clip deck exportado ao seu projeto atual usando _Append Clip Deck_. Os clips são adicionados ao final do seu clip deck atual, mas os efeitos e as configurações de grupo dentro do arquivo não são importados.

### Exportar clips selecionados

Todos os clips selecionados no momento serão exportados para um arquivo. Configurações de grupo e efeitos não serão salvos, apenas os clips. Observe que clips ativos em execução no momento não são exportados, a menos que também estejam selecionados.

{% hint style="info" %}
Use Option/Alt - shift - click nos clips para selecioná-los (ou use o laço). Você identifica quais clips estão selecionados pelo contorno branco espesso ao redor deles. Veja [Iniciar / parar clips](clips/starting-stopping-clips.md)
{% endhint %}

### Importar / Exportar efeitos

Carrega e salva todos os efeitos junto com suas configurações de grupo e parâmetros.

{% hint style="info" %}
**Carregar efeitos de um arquivo de projeto sem carregar o projeto inteiro**

Para importar apenas os efeitos de um projeto, selecione _**Effects->Import Effects**_ e, em vez de selecionar um arquivo de efeitos (.efts), escolha um arquivo de projeto.
{% endhint %}

### Exportar linha do tempo

Exporte um arquivo de linha do tempo com uma ou mais linhas do tempo. Observe que o clipdeck sempre é incluído nos arquivos de linha do tempo exportados (embora você possa escolher quais clips importar de volta; veja [Carregar e salvar](loading-and-saving.md#timeline-import) abaixo)

Se houver mais de uma linha do tempo no seu arquivo de projeto, um painel será aberto para você selecionar quais linhas do tempo deseja exportar.

{% hint style="danger" %}
Arquivos de som e vídeo na linha do tempo não são salvos com arquivos de linha do tempo. Portanto, salve-os separadamente se quiser transferir seu conteúdo para outro computador. Veja [Carregar e salvar](loading-and-saving.md#important-note-about-timeline-media-files)
{% endhint %}

### Importar linha do tempo

Importe uma ou mais linhas do tempo a partir de um único arquivo de linha do tempo. Depois que você selecionar o arquivo de linha do tempo, um painel será aberto com várias opções de importação.

Se o arquivo de linha do tempo tiver mais de uma linha do tempo, todas serão listadas. Marque as que você deseja incluir.

* Replace existing timelines\
  Exclui todas as suas linhas do tempo atuais e as substitui pelas importadas
* Import used clips only\
  Importa apenas os clips usados e organiza os clips em grupos, um para cada linha do tempo. Se esta opção não estiver selecionada, o clip deck inteiro do arquivo de linha do tempo será acrescentado aos seus clips existentes.
* Replace existing clip deck\
  Substitui seu clip deck atual pelos clips no arquivo de linha do tempo. Disponível somente se _Replace existing timelines_ estiver selecionado.

{% hint style="info" %}
**Carregar linhas do tempo de um arquivo de projeto sem carregar o projeto inteiro**

Para importar apenas as linhas do tempo de um projeto, selecione _**Timeline->Import Timeline(s)**_ e, em vez de selecionar um arquivo de linha do tempo (.ltml), escolha um arquivo de projeto.
{% endhint %}

### Importar / exportar DMX / ArtNet

Salva e carrega os nodes ArtNet, junto com seus endereços IP. Também inclui as zonas DMX e todos os seus presets DMX.

### Observação importante sobre arquivos de mídia da linha do tempo

Arquivos de som e vídeo **não são** exportados atualmente com o arquivo de linha do tempo. Portanto, se você precisar mover conteúdo para outro computador, inclua esses arquivos.

{% hint style="info" %}
**Como uma linha do tempo procura arquivos de mídia**

Quando a linha do tempo é carregada, ela procura na mesma pasta do arquivo de linha do tempo (ou de projeto) e pesquisa dentro dela e de todas as subpastas. Então, desde que os arquivos estejam na mesma pasta ou em uma subpasta (como _/videos_ ou _/sound_), eles serão encontrados durante o carregamento.
{% endhint %}
