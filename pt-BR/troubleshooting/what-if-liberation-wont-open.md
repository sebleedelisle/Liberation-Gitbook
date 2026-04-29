---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/troubleshooting/what-if-liberation-wont-open
---

# ✅ E se o Liberation não abrir?

É raro, mas às vezes o Liberation pode não iniciar ou pode travar logo depois de abrir. Isso quase sempre acontece porque um dos arquivos de configuração locais foi corrompido — geralmente depois de uma falha do sistema ou de algo inesperado no seu computador.

Felizmente, é fácil resolver redefinindo suas configurações locais. Veja como fazer isso no macOS e no Windows.

> **Importante**
>
> * Feche o Liberation antes de fazer qualquer coisa.
> * Estas etapas afetam apenas configurações locais, logs e caches. Sua licença e sua conta estão seguras.

***

#### Onde encontrar a pasta de trabalho

Cada versão do Liberation tem sua própria pasta de trabalho. Por exemplo, se você estiver usando a versão 1.0.0, o nome da pasta será 1.0.0.

* **macOS**: `~/Library/Application Support/Liberation/1.0.0`
* **Windows**: `AppData\Local\Liberation\1.0.0`

**Como abrir a pasta rapidamente**

**macOS**

1. No Finder, pressione **Shift + Cmd + G**.
2.  Cole este caminho e pressione **Enter**:

    ```
    ~/Library/Application Support/Liberation
    ```
3. Abra a pasta correspondente ao número da sua versão, por exemplo `1.0.0`.

**Windows**

1.  Pressione **Win + R**, cole isto e pressione **Enter**:

    ```
    %LOCALAPPDATA%\Liberation
    ```
2. Abra a pasta correspondente ao número da sua versão, por exemplo `1.0.0`.

> **Dica para Windows**: se você navegar pelo Explorador de Arquivos, habilite os itens ocultos: **View > Show > Hidden items**.

***

#### Etapa 1 – Redefina com segurança seu arquivo de configurações

Dentro da pasta da sua versão, abra:

```
data/liberation/
```

Dentro da pasta liberation, você deve encontrar um arquivo chamado `settings.json`. Exclua esse arquivo.

* **Exemplo no macOS**: `~/Library/Application Support/Liberation/1.0.0/data/liberation/settings.json`
* **Exemplo no Windows**: `%LOCALAPPDATA%\Liberation\1.0.0\data\liberation\settings.json`

Agora tente iniciar o Liberation. Se ele abrir, está tudo resolvido.

***

#### Etapa 2 – Verifique se há um Clip problemático

Se o Liberation travou enquanto você editava um Clip, é possível que algo nesse arquivo de Clip esteja causando o problema.

Na mesma pasta do arquivo settings.json, você deve encontrar um arquivo chamado `clipEdit.json`

Faça backup desse arquivo em um local seguro (por exemplo, na sua Área de Trabalho) e depois exclua-o da pasta de trabalho do Liberation.

Tente iniciar o Liberation novamente. Se ele agora abrir normalmente, envie o arquivo de backup por e-mail para [**info@liberationlaser.com**](mailto:info@liberationlaser.com) para que possamos investigar o que causou o problema.

***

#### Etapa 3 - Faça backup e depois exclua a pasta de trabalho inteira

Se a Etapa 1 e a Etapa 2 não ajudaram:

1. **Faça backup** da pasta inteira da versão:
   * macOS: clique com o botão direito na pasta `1.0.0` e escolha **Compress** para criar um zip, ou copie-a para um local seguro, como a Área de Trabalho.
   * Windows: clique com o botão direito na pasta `1.0.0` e escolha **Send to > Compressed (zipped) folder**, ou copie-a para um local seguro, como a Área de Trabalho.
2. Depois de fazer o backup, **exclua** a pasta `1.0.0` original do local de trabalho do Liberation.
3. Inicie o Liberation novamente. Ele recriará uma nova pasta de trabalho.

Se o Liberation agora abrir, siga para a Etapa 4.

***

#### Etapa 4 - Envie o backup para nós

Isso nos ajuda a identificar o que causou o problema para que possamos evitá-lo em versões futuras.

Compacte seu **backup** da Etapa 3, se ainda não tiver feito isso, e envie-o por e-mail para que possamos diagnosticar a causa.

* **Para**: [info@liberationlaser.com](mailto:info@liberationlaser.com)
* **Assunto**: Liberation start-up fix - working folder backup
* **Corpo**: inclua:
  * Sistema operacional e versão (por exemplo, macOS 14.6 ou Windows 11 23H2)
  * Versão do Liberation (por exemplo, 1.0.0)
  * Qual etapa resolveu o problema, se alguma resolveu (Etapa 1, Etapa 2 ou Etapa 3)
  * Uma breve descrição do que aconteceu antes de o problema começar
* **Anexo**: o backup compactado da sua pasta de trabalho `1.0.0`.

> Se o zip for grande demais para e-mail, envie-o para um drive na nuvem e compartilhe um link.

***

#### Ainda não inicia depois da Etapa 3?

Se o Liberation ainda não abrir depois de excluir a pasta de trabalho:

* Reinicie o computador e tente novamente.
* Desative temporariamente antivírus ou ferramentas de segurança que possam bloquear novas pastas e tente iniciar novamente.
* Reinstale a versão mais recente do Liberation por cima da instalação existente.
* Se nada disso funcionar, entre em contato com o suporte em [**info@liberationlaser.com**](mailto:info@liberationlaser.com) com os detalhes e quaisquer logs de travamento da subpasta `logs`, se ela existir.

***

#### Resumo

1. Exclua `data/liberation/settings.json` na pasta de trabalho versionada.
2. Se você estava editando um Clip, faça backup e depois exclua `data/liberation/clipEdit.json`.
3. Se ainda não abrir, faça backup e depois exclua a pasta `1.0.0` inteira (ou a pasta da sua versão).
4. Se a Etapa 3 resolver (ou se não resolver), compacte o backup e envie-o para [**info@liberationlaser.com**](mailto:info@liberationlaser.com) com seu sistema operacional e a versão do Liberation.
