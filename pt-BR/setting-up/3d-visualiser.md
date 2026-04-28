---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/setting-up/3d-visualiser
---

# ✅ 3D Visualiser

### Introdução

O 3D Visualiser do Liberation é um recurso extremamente útil: você pode criar e ajustar seus shows sem precisar de nenhum laser! Para mim, ele se mostrou uma ferramenta indispensável, especialmente em configurações mais complexas com um grande número de lasers.

### Navegando pelo espaço 3D

<figure><img src="../.gitbook/assets/White.png" alt=""><figcaption><p>A visualização do 3D Visualiser</p></figcaption></figure>

* Clique e arraste para girar a visualização ao redor do ponto de órbita
* Use a roda do mouse para se mover para trás e para frente em direção ao ponto de órbita
* Clique e arraste mantendo a tecla shift pressionada para mover a câmera lateralmente (strafe) para a esquerda, direita, para cima e para baixo ao longo do plano XY
* Dê um clique duplo em qualquer lugar do visualiser para redefinir a posição da câmera

### Configurações

Abra o painel _3D Visualiser Settings_ pelo menu _Window_.

<figure><img src="../.gitbook/assets/Screenshot 2025-01-22 at 10.33.17.png" alt="" width="375"><figcaption><p>O painel 3D Visualiser Settings</p></figcaption></figure>

* **Visualiser size** - altera o tamanho do visualiser em relação ao restante do app
* **Brightness Adjustment** - altera o brilho com que os lasers aparecem
* **Show laser numbers** - renderiza o número correspondente acima de cada laser
* **Show zone names** - renderiza os nomes das zonas correspondentes abaixo de cada laser

### Configurações de câmera

Estas configurações se referem principalmente à câmera virtual no espaço 3D. Você verá um menu suspenso com presets para essas configurações, que podem ser salvos e carregados novamente.

* **Camera distance -** A câmera está sempre apontada para seu _Orbit point_. A distância da câmera define o quanto ela fica afastada desse ponto. Você também pode ajustar essa configuração usando a roda de rolagem do mouse.
* **FOV -** Field of view: determina o ângulo de visão da câmera / o quanto ela está aproximada.
* **Orbit position** - descreve a rotação atual ao redor do ponto de órbita. O primeiro valor é a rotação em torno do eixo X (pitch) e o segundo valor é a rotação em torno do eixo Y (yaw).
* **Orbit centre point** - a posição do ponto de órbita no espaço 3D, x, y, z.
* **Grid height** - a altura da grade em relação ao "chão" (ou seja, onde y = 0).

### Configurações de conteúdo

Estas configurações determinam onde os lasers (e o Canvas) são posicionados dentro do ambiente 3D. Você verá um menu suspenso com presets para essas configurações, que podem ser salvos e carregados novamente.

#### Lasers

Cada laser tem seu próprio grupo de configurações, que você pode expandir usando o pequeno triângulo branco.

<figure><img src="../.gitbook/assets/Camera Visualiser Laser Settings.png" alt="" width="375"><figcaption><p>Configurações de laser do 3D visualiser</p></figcaption></figure>

* **3D Position** - a posição x, y e z do laser.
* **3D Orientation** - a rotação do laser em torno de cada um dos eixos x, y e z.
* **Flip X / Flip Y** - inverte a saída virtual do laser. OBSERVAÇÃO: isso não deveria ser necessário; é melhor usar as configurações de flip / orientação do laser para corrigir qualquer inconsistência com seu hardware.
* **Output Range horizontal / vertical** - relacionado ao ângulo mínimo / máximo dos scanners do seu laser. 60º é o padrão, mas você pode ajustar esse valor se seus lasers forem diferentes.

#### Canvas

Se você estiver usando o sistema Canvas, também pode optar por incluir a imagem do Canvas na visualização 3D. Ative a caixa de seleção para renderizar o Canvas e use as configurações de posição, orientação e escala para determinar como ele aparece na sua visualização 3D.

<figure><img src="../.gitbook/assets/Camera Visualiser Canva Settings.png" alt="" width="375"><figcaption><p>Configurações de Canvas do 3D visualiser</p></figcaption></figure>

{% hint style="info" %}
Está vendo lasers "fantasmas"? O 3D Visualiser é relativamente independente da configuração de lasers, e é possível ter mais lasers no visualiser do que você tem no Liberation. Quando você adiciona um laser ao seu projeto, um novo objeto de laser dentro do visualiser também é adicionado. Mas, se você excluir um laser, ainda permanecerá um objeto de laser "fantasma" no visualiser.

Para remover todos os lasers fantasmas, clique no botão _Remove extra 3D laser objects_ (na parte inferior do painel de configurações do 3D Visualiser).

<img src="../.gitbook/assets/Remove extra 3D laser.png" alt="" data-size="original">
{% endhint %}
