---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/dmx-control/dmx-zones
---

# ◼️ Zonas DMX

As DMX zones são zonas de Output do Liberation que enviam Art-Net/DMX em vez de pontos de laser. Elas aparecem junto com beam zones e canvas zones, então os Clips podem ser atribuídos a elas no mesmo fluxo de seleção de zone.

Abra **DMX Zones** pelo menu, ou use a seção DMX em Laser Overview, para gerenciá-las.

* **ADD DMX ZONE** - cria uma nova DMX zone.
* **ARM** - habilita a saída DMX para essa zone. Uma DMX zone que não está armada zera os canais mapeados.
* **Node** - seleciona o número do node Art-Net.
* **Universe** - seleciona o universo Art-Net. O valor exibido começa em 1, portanto Universe 1 é o primeiro universo.
* **Address** - define o endereço inicial do fixture. O valor exibido também começa em 1.
* **Preset** - escolhe o preset DMX que mapeia o conteúdo do Clip para canais DMX.
* **Edit DMX zone settings** (ícone de lápis) - abre as configurações da zone, como encaminhamento manual de zone e orientação do fixture.
* **Edit DMX profile/channel mapping** (ícone de controles deslizantes) - abre o editor de preset/canais DMX.
* **Delete** - remove a DMX zone.

### Limites de armamento

O número de DMX zones que podem ficar armadas ao mesmo tempo depende do nível da sua licença. Se o seu nível não permitir saída DMX, ou se você já tiver armado o número máximo de DMX zones, o botão **ARM** das zones adicionais fica desativado e mostra um ícone de proibido ao passar o cursor sobre ele.

Desarme outra DMX zone, ou use um nível de licença com um limite de DMX maior, antes de armar mais zones.
