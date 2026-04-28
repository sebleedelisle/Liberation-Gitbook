---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/using-liberation-with-capture
---

# 🟩 Usando o Liberation com o Capture

O Liberation oferece suporte ao [Capture](https://capture.se) como visualizador externo (a partir da versão 1.0.3). Se você já usa o Capture no seu fluxo de trabalho, pode usá-lo para visualizar a saída laser ao vivo do Liberation na sua cena 3D.

### Como funciona

Não há nenhum processo especial de conexão nem vinculação manual necessária.

Desde que:

* O Liberation e o Capture estejam na mesma rede
* Seu firewall permita a conexão

…qualquer laser configurado no Liberation aparecerá automaticamente dentro do Capture como fonte de mídia. Você não precisa configurar endereços IP nem ativar nada especial — ele simplesmente aparece.

### Visualizando lasers dentro do Capture

Todos os lasers configurados no Liberation aparecerão no Capture como fontes de mídia disponíveis.

Para realmente ver a saída:

* O laser precisa estar armado no Liberation
* A fonte precisa estar anexada a um fixture de laser dentro do Capture

Depois de armado, o Capture visualizará o fluxo de saída ao vivo do Liberation. Se um laser for desarmado no Liberation, ele continuará visível no Capture como fonte, mas não emitirá nada.

Consulte a documentação em [capture.se](https://www.capture.se/) para mais instruções e suporte sobre como configurar lasers no Capture. <br>

### Limites da licença e lasers armados

As conexões com o Capture são tratadas exatamente da mesma forma que saídas físicas de laser.

Isso significa que:

* Você só pode armar a quantidade de lasers permitida pelo seu nível de licença
* Somente lasers armados enviarão dados ativamente para o Capture

### Preciso do Capture?

Não.

O Liberation inclui um 3D Visualiser integrado, que está sempre disponível e não depende do seu nível de licença. Você pode criar e pré-visualizar shows diretamente dentro do Liberation, sem nenhum software externo.

O Capture é apenas uma opção adicional se você já o utiliza para iluminação ou design de shows.

### Solução de problemas

Se os lasers não aparecerem no Capture:

* Verifique se os dois aplicativos estão na mesma rede
* Verifique as configurações do seu firewall
* Certifique-se de que o laser esteja armado no Liberation
