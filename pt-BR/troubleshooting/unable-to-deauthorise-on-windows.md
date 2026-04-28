---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/troubleshooting/unable-to-deauthorise-on-windows
---

# ✅ Não consegue desautorizar no Windows?

#### Não consegue desautorizar no Windows?

Se você não conseguir desautorizar um computador no Windows, primeiro verifique se está desautorizando a licença usando a mesma versão do Liberation que a autorizou originalmente, antes de autorizá-la novamente em uma versão diferente.

Se isso não funcionar e você estiver usando uma versão anterior à 1.0, o problema provavelmente está relacionado à forma como builds mais antigos do Liberation para Windows identificavam o computador. Nessas versões, o sistema usado para gerar o ID da máquina era menos confiável e, em alguns casos, o ID podia mudar entre reinicializações, mesmo que nenhum hardware tivesse sido alterado de forma evidente.

Se você estiver preso tentando desautorizar e não tiver trocado de versão, entre em contato pelo e-mail support@liberationlaser.com e poderemos desautorizar a máquina manualmente para você.

**Por que isso acontece**

Nas primeiras builds do Liberation para Windows (anteriores à 1.0), usamos o método de sistema recomendado pelo Windows para gerar um ID de máquina. Infelizmente, ele se mostrou inconsistente em algumas situações. Por isso, o sistema de licenciamento foi reescrito na versão 1.0 para usar uma combinação de métodos mais robusta, que agora funciona de forma confiável.

Como resultado, o ID do computador usado por versões mais antigas do Liberation pode ser diferente do usado pelas versões atuais. Se o ID já tiver mudado, a desautorização precisa ser feita manualmente pelo suporte.

***
