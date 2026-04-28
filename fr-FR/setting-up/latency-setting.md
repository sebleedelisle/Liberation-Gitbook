---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/setting-up/latency-setting
---

# ✅ Paramètre de latence

Dans le panneau _Settings_ (_Liberation->Settings_ ou CMD/CTRL ,), vous verrez un curseur intitulé _Latency(ms)._ (Dans les anciennes versions de Liberation, il se trouvait dans le panneau Laser Overview)

{% hint style="info" %}
Le réglage de latence par défaut de 150 ms convient dans la plupart des cas, mais si vous rencontrez des problèmes réseau, vous pouvez essayer de l’augmenter.
{% endhint %}

### L’explication détaillée

Ce réglage de « latence d’image » correspond au délai maximal entre le moment où Liberation crée une image et le moment où le laser commence à la projeter. Si vous augmentez cette valeur, vous pourrez remarquer un léger décalage entre Liberation et la sortie de votre laser.

L’avantage d’une latence d’image plus longue est que Liberation peut remplir dès que possible les buffers des contrôleurs laser avec du contenu ; en cas de congestion sur le réseau, le contrôleur risque moins de manquer de points.

Cela s’applique généralement uniquement aux DAC réseau, et un réglage de 100 ms devrait offrir un bon équilibre entre réactivité et protection contre les retards réseau. Si votre réseau est vraiment performant, vous devriez pouvoir réduire cette valeur à 50 ms.&#x20;
