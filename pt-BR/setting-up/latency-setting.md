---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/setting-up/latency-setting
---

# ✅ Configuração de latência

No painel _Settings_ (_Liberation->Settings_ ou CMD/CTRL ,), você verá um controle deslizante chamado _Latency(ms)._ (Em versões mais antigas do Liberation, isso ficava no painel Laser Overview)

{% hint style="info" %}
A configuração padrão de latência de 150 ms deve funcionar bem na maioria dos casos, mas, se você estiver tendo problemas de rede, talvez seja melhor tentar aumentá-la.
{% endhint %}

### A explicação complicada

Esta configuração de "latência de frame" é o tempo máximo entre o Liberation criar um frame e o laser começar a reproduzi-lo. Se você aumentar esse valor, talvez perceba um pequeno atraso entre o Liberation e a saída do laser.

O benefício de uma latência de frame maior é que o Liberation consegue preencher os buffers dos controladores laser com conteúdo o mais rápido possível; se houver congestionamento na rede, é menos provável que o controlador fique sem pontos.

Normalmente, isso se aplica apenas a DACs de rede, e uma configuração de 100 ms deve ser um bom equilíbrio entre velocidade e proteção contra atrasos na rede. Se você tiver uma rede realmente forte, deve conseguir reduzir para 50 ms.&#x20;
