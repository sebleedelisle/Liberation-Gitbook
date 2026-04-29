---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/hardware/lasercube
---

# ✅ LaserCube

<figure><img src="../.gitbook/assets/main-image-4.jpg.webp" alt=""><figcaption><p>Imagem promocional do LaserCube, cortesia da Wicked Lasers</p></figcaption></figure>

O [LaserCube](https://www.laseros.com/lasercube/) da Wicked Lasers é uma unidade laser extremamente compacta, alimentada por bateria, disponível em várias configurações de potência. Ele é popular entre hobbistas por causa do app de smartphone fácil de usar, mas os modelos recentes já têm capacidade suficiente para uso em shows profissionais.

O app para celular (chamado LaserOS, também disponível para desktop) é gratuito, muito divertido para experimentar e bom o bastante para a maioria dos usuários. Mas, se você está operando shows maiores com vários lasers, precisa de algo mais especializado e potente — e é aí que entra o Liberation.

### Como conectar a um LaserCube

Os primeiros LaserCubes são controlados por USB, mas os modelos atuais têm um controlador de rede integrado. Esses cubos controlados por rede são conhecidos como "LaserCube Wifi". O Liberation é compatível com os dois tipos de LaserCube\*, seja por USB ou em uma rede.

\*(O suporte ao protocolo de rede do LaserCube foi introduzido na versão 0.7.3)

### USB LaserCube

Conecte seu LaserCube ao computador com um cabo micro USB e procure por ele no painel _Controller Assignment_ (veja [Atribuição de controladores](../setting-up/controller-assignment.md)). Se ele não aparecer automaticamente, pressione o botão _REFRESH_.

### Network LaserCube "Wifi"

{% hint style="danger" %}
Embora os cubos "Wifi" tenham sido projetados para operar em uma rede sem fio, isso não é recomendado, e você provavelmente terá quedas e falhas. Em vez disso, use a porta RJ45 para conectar seu LaserCube a uma rede cabeada, da mesma forma que faria com Ether Dreams.
{% endhint %}

Conecte seu LaserCube à sua rede cabeada.

Coloque seu LaserCube no modo "LAN Client" e verifique se há um roteador na rede. O LaserCube receberá um endereço IP do roteador e então deverá aparecer no painel _Controller Assignment_. (Veja [Atribuição de controladores](../setting-up/controller-assignment.md)).

{% hint style="info" %}
É possível configurar uma rede sem roteador e atribuir endereços IP fixos a todos os dispositivos, e isso é muito comum na indústria de eventos. Pessoalmente, prefiro adicionar um roteador à rede e recomendo essa opção para qualquer pessoa com menos experiência em redes.

O roteador atribui dinamicamente um endereço IP a tudo; considero isso mais simples e menos sujeito a erros.
{% endhint %}

{% hint style="danger" %}
Ao contrário do Ether Dream, _**LaserCubes NÃO APAGAM O LASER**_ se encontrarem um buffer under-run, pacote perdido ou outros dados corrompidos/incorretos.

Em vez disso, eles simplesmente continuam de onde pararam e, em alguns casos, isso pode fazer com que um feixe ativo atravesse áreas que não estão dentro de zonas e, pior ainda, corte através de máscaras de software.

Estou conversando com os designers/desenvolvedores do LaserCube e espero que isso seja resolvido no futuro com uma atualização de firmware, mas, enquanto isso, você deve garantir que todas as áreas onde não quer que o laser chegue estejam fisicamente mascaradas.

Para ser justo, você provavelmente deveria fazer isso de qualquer forma, mas eu mesmo uso máscaras de software para proteger câmeras e projetores. Então, esteja ciente de que fazer isso usando o protocolo de rede do LaserCube é mais perigoso do que com o Ether Dream (que entra em um modo de parada de segurança assim que ocorre qualquer erro ou falta de dados).

Além disso, eu já disse isso, mas **use uma conexão cabeada com seu LaserCube**. Wifi não vai dar conta e deixará esse problema ainda pior.
{% endhint %}
