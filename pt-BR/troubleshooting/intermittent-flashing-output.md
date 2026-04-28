---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/troubleshooting/intermittent-flashing-output
---

# ✅ Saída intermitente / piscando

Abra o painel _Laser Overview_ e observe a luz de conexão ao lado do laser com o qual você está tendo problema.

**Se a luz de conexão NÃO estiver constantemente verde:**\
Então você tem um problema de rede ou de desempenho da CPU:

**Desempenho da rede -**

* Verifique se você não está conectado a uma rede wifi. Você deve sempre usar uma conexão cabeada. Garanta que o seu sistema operacional esteja priorizando a rede cabeada em vez do wifi ou desative o wifi se não tiver certeza
* verifique seu adaptador de rede — e teste outro adaptador USB-C
* Usuários de Windows — verifiquem / atualizem os drivers de rede e executem as ferramentas adequadas de teste de rede
* verifique todo o cabeamento, switches e roteadores. Troque e teste cada cabo de forma metódica.
* reinicie todos os seus equipamentos de rede, incluindo switches, roteadores e cada Ether Dream.

**Desempenho da CPU**

Se você estiver usando um computador antigo ou com especificações baixas, ele pode ser lento demais para executar o Liberation. Verifique o indicador de taxa de quadros no lado direito da barra de ícones.

Há dois números ali: a taxa de quadros real e a taxa de quadros alvo. Se a taxa de quadros real cair abaixo de 30, você poderá ter problemas.

As ações a seguir podem ajudar:

* remova lasers não utilizados; por exemplo, se você tiver apenas um laser conectado, exclua os outros.
* Mude para a visualização Output ou Canvas
* Feche todos os outros programas, verifique as configurações do firewall de rede, feche antivírus, Dropbox etc.
* Reduza a resolução da sua tela e diminua o tamanho da janela do Liberation

Se nada disso funcionar, considere atualizar seu computador.

***

**Se a luz de conexão ESTIVER constantemente verde:**

Então provavelmente é um problema de hardware. Isso está fora do escopo deste manual, mas você pode tentar as seguintes ações:

* Desative o sistema SFS (Scan Fail Safety). Alguns lasers têm uma função que desativa a saída se os scanners pararem de se mover, ou seja, se estiverem produzindo um feixe estático forte. Esses sistemas podem ser um pouco cautelosos demais / pouco confiáveis.

{% hint style="danger" %}
Tenha extremo cuidado ao desativar o sistema scan fail safety. Feixes estáticos fortes podem causar queimaduras! Certifique-se de ter um botão de parada e um extintor de incêndio à mão.
{% endhint %}

* Verifique os cabos e sistemas de interlock
* Verifique todo o cabeamento entre o controlador e o laser.

Um [ILDA Gem](https://shop.stanwaxlaser.co.uk/ilda-gem-pocket-2020-718-p.asp) pode ser uma ferramenta inestimável para solucionar problemas com lasers.
