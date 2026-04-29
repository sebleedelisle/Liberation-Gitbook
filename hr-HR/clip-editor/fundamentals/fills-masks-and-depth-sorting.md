---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clip-editor/fundamentals/fills-masks-and-depth-sorting
---

# 🟩 Ispune, masks i razvrstavanje po dubini

### Linije, ispune i masks

Primijetit ćete da neki nodes tipa Creator imaju opciju _Fill state_; možete ih crtati kao liniju (obris), kao mask (koja prekriva sadržaj ispod) ili oboje.

Kada oblik renderirate kao mask, ponaša se kao da je ispunjen crnom bojom i prekriva sve što se nalazi ispod njega.

{% hint style="info" %}
Crtanje linije (ili _stroke_) laserom dovoljno je jednostavno: laserskim snopom prijeđete od početka linije do kraja linije. I to je vaša linija!

Ispunjeni oblici su teži. Ako želite oblik ispunjen bojom, mogli biste ručno napraviti šrafuru crtanjem linija i popunjavanjem, ali Liberation to ne može učiniti automatski (još). Čak i kada bismo to radili, i dalje biste vidjeli druge linije ispod kako se probijaju kroz ispunu.

Ono što možemo učiniti jest ispuniti oblike _crnom_. Ispod haube, Liberation izvodi sve izračune potrebne za uklanjanje sadržaja koji se nalazi ispod oblika ispunjenog crnom bojom. Vjerujte, to je pipav posao!

Ali radi vrlo dobro i stvara dojam oblika ispunjenog crnom bojom.
{% endhint %}

### Razvrstavanje po dubini

Budući da neki oblici mogu _prekrivati_ druge oblike, Liberation ih mora razvrstati prema dubini. Prema zadanim postavkama, elementi se razvrstavaju po dubini prema svojem položaju na z-osi. Ako su na istom položaju na z-osi, razvrstavaju se prema redoslijedu slojeva, koji se može promijeniti pomoću gumba _MOVE TO FRONT_ i _MOVE TO BACK_ u svakom Creator.
