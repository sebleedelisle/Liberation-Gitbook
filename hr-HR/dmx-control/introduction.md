---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/dmx-control/introduction
---

# ✅ Uvod

Liberation uključuje fleksibilan i snažan DMX sustav koji omogućuje izradu svjetlosnih efekata i upravljanje laserima kompatibilnima s DMX-om putem Art-Net. Osmišljen je tako da olakša sinkronizaciju rasvjete s laserskim showom — bez potrebe za zasebnim rasvjetnim pultom.

{% hint style="info" %}
**Što je Art-Net i kako je povezan s DMX-om?**

**DMX** je sustav koji se već godinama koristi za upravljanje rasvjetom, laserima, dimnim strojevima i drugim scenskim efektima. Upravljačke signale šalje posebnim kabelima, najčešće s XLR priključcima, a svaki uređaj prati određeni skup kanala kako bi znao što treba raditi.

**Art-Net** je noviji način slanja istih DMX podataka preko obične računalne mreže. Umjesto posebnih kabela, sve se šalje preko Etherneta, kao internetski ili lokalni mrežni promet.

U Liberation se sav DMX izlaz šalje putem Art-Net. Možete ga koristiti za izravno upravljanje uređajima kompatibilnima s Art-Net ili možete priključiti **Art-Net čvor** — malu kutiju koja pretvara Art-Net natrag u standardni DMX. To znači da i dalje možete upravljati tradicionalnom DMX rasvjetom i efektima, čak i ako sami ne podržavaju Art-Net.
{% endhint %}

Možete ga koristiti i za upravljanje raznom scenskom opremom, kao što su dimni strojevi, uređaji za maglicu, CO₂ mlaznice, uređaji za hladne iskre i drugo. Ako oprema podržava DMX, možete je postaviti kao DMX zone i pokretati izravno iz Liberation, zajedno s laserskim sadržajem.

DMX uređaji dodaju se kao **DMX zone**, koje se prikazuju na popisu zone zajedno s vašim laser beam zone i ciljanim područjima za Canvas. Svaka DMX zone koristi **DMX preset**, koji Liberation govori kako mapirati svojstva iz vaših laserskih Clips — poput položaja, boje i svjetline — u vrijednosti DMX kanala.

Kada Clip pošaljete u DMX zone, Liberation uzima prvi element u tom Clip i pretvara njegova svojstva prema odabranom presetu. Tako je jednostavno upravljati rasvjetom i DMX efektima izravno iz istih Clips koje već koristite za lasere.

#### Liberation na Glastonburyju

<figure><img src="../.gitbook/assets/show-arcadia-spider-2023.jpg" alt=""><figcaption></figcaption></figure>

Prvi pravi test DMX sustava u Liberation bio je na Glastonburyju 2023., gdje je Reach Lasers postavio ukupno 90 izvora zraka kao dio pozornice Arcadia “spider”.

18 lasera upravljano je internim Ether Dream uređajima, a dodatnih 12 beam barova sa 6 glava upravljano je putem Art-Net i DMX.
