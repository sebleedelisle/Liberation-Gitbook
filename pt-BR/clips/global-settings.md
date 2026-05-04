---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clips/global-settings
---

# 🟩 Transformações globais

Além das transformações de Clip (shift x/y, scale x/y), há as Global Transformations, que se aplicam a todos os Clips que você executa. Abra o painel _Global Transformations_ para vê-las. (Esse painel normalmente fica em uma aba ao lado de _Clip Settings_).

Por padrão, todas essas configurações serão redefinidas assim que não houver mais nenhum Clip em execução. Esse comportamento de redefinição pode ser desativado com o botão _AUTO RESET_ na parte inferior do painel _Global Transformations_.

{% hint style="info" %}
Observe que as Global Transformations não afetam nada no Canvas, apenas zonas Beam e DMX
{% endhint %}

### Scale X/Y

Escala horizontal e vertical. Esses valores ficam vinculados entre si, a menos que você pressione `Shift`. Por padrão, eles também são mapeados para os knobs 4 e 8 de Device Control do APC40 e aparecem no painel contextual Parameters à direita do Clip Deck.

### Shift X/Y

Deslocamento horizontal e vertical. Move tudo horizontalmente / verticalmente.

### Spin

Gira todo o conteúdo ao redor do centro. Um valor positivo gira no sentido horário; um valor negativo gira no sentido anti-horário. Você verá que essa configuração afeta a transformação _Rotation_. Por padrão, ela é mapeada para o knob 3 de Device Control do APC40 e aparece no painel contextual Parameters à direita do Clip Deck.

### Spin 3D

Gira todo o conteúdo ao redor do eixo Y (que é uma linha vertical no centro). Você verá que essa configuração afeta a transformação _Rotation3D_. Por padrão, ela é mapeada para o knob 7 de Device Control do APC40 e aparece no painel contextual Parameters à direita do Clip Deck.

### Rotation

Uma rotação ao redor do centro, com valor em graus.

### Rotation 3D

Uma rotação ao redor do eixo Y (que é uma linha vertical no centro), com valor em graus.

### Auto reset

Quando ativado, isso redefinirá todas as Global Transformations assim que todos os Clips em execução forem desativados. Assim, você pode ter certeza de que não terá surpresas na próxima vez que executar um Clip!
