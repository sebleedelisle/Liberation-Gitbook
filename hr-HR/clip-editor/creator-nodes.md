---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clip-editor/creator-nodes
---

# 🟩 Creator nodes

### <img src="../.gitbook/assets/Creator Point.png" alt="" data-size="line"> Point Creator

Stvara jednu točku / snop.

* **Render profile** - pogledajte [Profil renderiranja](fundamentals/render-profile.md "mention")
* **Colour** - boja točke. Pogledajte [Postavke boje i HSB](fundamentals/colour-settings-and-hsb.md "mention")
* položaj **x** i **y** - pogledajte [Koordinatni sustav](fundamentals/co-ordinate-system.md "mention")
* _MOVE TO FRONT / MOVE TO BACK_ - pogledajte [Ispune, mask elementi i sortiranje po dubini](fundamentals/fills-masks-and-depth-sorting.md "mention")

### <img src="../.gitbook/assets/CreatorLine.png" alt="" data-size="line"> Line Creator

Stvara liniju / plohu.

* **Render profile** - pogledajte [Profil renderiranja](fundamentals/render-profile.md "mention")
* **Size** - duljina linije
* **Colour** - boja linije. Pogledajte [Postavke boje i HSB](fundamentals/colour-settings-and-hsb.md "mention")
* položaj **x** i **y** - pogledajte [Koordinatni sustav](fundamentals/co-ordinate-system.md "mention")
* **rotation** - kut linije, u stupnjevima
* **resolution** - pogledajte [Rezolucija](fundamentals/resolution.md "mention")
* **alignment** - _LEFT / CENTRE / RIGHT -_ određuje početnu točku i središte rotacije linije
* _MOVE TO FRONT / MOVE TO BACK_ - pogledajte [Ispune, mask elementi i sortiranje po dubini](fundamentals/fills-masks-and-depth-sorting.md "mention")

### <img src="../.gitbook/assets/CreatorCircle.png" alt="" data-size="line"> Circle Creator

Stvara krug / stožac.

* **Render profile** - pogledajte [Profil renderiranja](fundamentals/render-profile.md "mention")
* **radius** - polumjer kruga
* **Colour** - boja kruga. Pogledajte [Postavke boje i HSB](fundamentals/colour-settings-and-hsb.md "mention")
* položaj **x** i **y** - pogledajte [Koordinatni sustav](fundamentals/co-ordinate-system.md "mention")
* **resolution** - pogledajte [Rezolucija](fundamentals/resolution.md "mention")
* **Fill state** - pogledajte [Ispune, mask elementi i sortiranje po dubini](fundamentals/fills-masks-and-depth-sorting.md "mention")
* _MOVE TO FRONT / MOVE TO BACK_ - pogledajte [Ispune, mask elementi i sortiranje po dubini](fundamentals/fills-masks-and-depth-sorting.md "mention")

### <img src="../.gitbook/assets/CreatorPoly.png" alt="" data-size="line"> Polygon Creator

Stvara jednakostranični poligon, trokut, kvadrat, peterokut itd.

* **Render profile** - pogledajte [Profil renderiranja](fundamentals/render-profile.md "mention")
* **size** - udaljenost od središta do svakog kuta
* **Colour** - boja poligona. Pogledajte [Postavke boje i HSB](fundamentals/colour-settings-and-hsb.md "mention")
* položaj **x** i **y** - pogledajte [Koordinatni sustav](fundamentals/co-ordinate-system.md "mention")
* **rotation** - zakrenuti kut oblika, u stupnjevima
* **resolution** - pogledajte [Rezolucija](fundamentals/resolution.md "mention")
* **Fill state** - pogledajte [Ispune, mask elementi i sortiranje po dubini](fundamentals/fills-masks-and-depth-sorting.md "mention")
* _MOVE TO FRONT / MOVE TO BACK_ - pogledajte [Ispune, mask elementi i sortiranje po dubini](fundamentals/fills-masks-and-depth-sorting.md "mention")

### <img src="../.gitbook/assets/CreatorShape.png" alt="" data-size="line"> Shape Creator

Učitava SVG datoteku za prilagođene oblike.

{% hint style="warning" %}
Liberation je kompatibilan s formatom _SVGTiny_. Preporučuje se InkScape, ali većina aplikacija za vektorsku grafiku može izvoziti u tom formatu. Prije izvoza obavezno pretvorite sav tekst u oblike. Liberation će renderirati poteze, a po želji može koristiti ispune kao mask elemente. Pazite da linije nisu crne jer se bez modifikatora boje neće prikazati!
{% endhint %}

* **Import SVG** - učitava SVG datoteku s diska.

{% hint style="info" %}
Nakon učitavanja SVG datoteke sadržaj se pretvara i sprema zajedno sa stavkom Clip, pa ne morate zadržati vezu na datoteku, osim ako kasnije želite promijeniti postavke za mask.
{% endhint %}

* **Use fills as masks** - obrađuje svaki ispunjeni oblik kao mask element, tj. kao oblik ispunjen crnom bojom. To će se automatski postaviti ako vaš SVG sadrži ispunjene oblike. Ako nema ispunjenih oblika, bit će onemogućeno. Pogledajte [Ispune, mask elementi i sortiranje po dubini](fundamentals/fills-masks-and-depth-sorting.md "mention")
* **Add outlines to filled shapes** - ako oblici u vašem SVG-u nemaju obris, ne možemo ih nacrtati! Ova opcija dodaje obris (ili _stroke_) svakom ispunjenom obliku. Ako vaš SVG nema nijedan oblik s potezom, postavlja se automatski. Ako nema ispunjenih oblika, onemogućena je.
* **Invert black lines** - ako su sve linije u vašem SVG-u crne, ne možete ih vidjeti! Ova opcija pretvara ih u bijele. Postavlja se automatski ako vaš SVG ima samo crne oblike, ali je onemogućena ako ih nema.
* **Render profile** - pogledajte [Profil renderiranja](fundamentals/render-profile.md "mention")
* **scale** - prilagođava veličinu SVG-a. To se automatski izračunava pri učitavanju SVG-a (kako bi slika bila vidljiva), ali se nakon toga može ručno urediti.
* položaj **x** i **y** - pogledajte [Koordinatni sustav](fundamentals/co-ordinate-system.md "mention")
* **rotation** - zakrenuti kut slike, u stupnjevima
* **resolution** - pogledajte [Rezolucija](fundamentals/resolution.md "mention")
* _MOVE TO FRONT / MOVE TO BACK_ - pogledajte [Ispune, mask elementi i sortiranje po dubini](fundamentals/fills-masks-and-depth-sorting.md "mention")

### <img src="../.gitbook/assets/CreatorAnim.png" alt="" data-size="line"> Anim Creator

Stvara animaciju iz slijeda SVG datoteka.

* **Import SVG Sequence** - odaberite mapu koja sadrži sve SVG datoteke. Imajte na umu da se učitavaju alfanumeričkim redoslijedom.

{% hint style="info" %}
Nakon učitavanja slijeda SVG datoteka sadržaj se pretvara i sprema zajedno sa stavkom Clip, pa ne morate zadržati vezu na datoteke, osim ako kasnije želite promijeniti postavke za mask.
{% endhint %}

* **Use fills as masks** - obrađuje svaki ispunjeni oblik kao mask element, tj. kao oblik ispunjen crnom bojom. To će se automatski postaviti ako bilo koji od vaših SVG-ova sadrži ispunjene oblike. Ako nijedan nema ispunjene oblike, bit će onemogućeno. Pogledajte [Ispune, mask elementi i sortiranje po dubini](fundamentals/fills-masks-and-depth-sorting.md "mention")
* **Add outlines to filled shapes** - ako oblici u vašim SVG-ovima nemaju obrise, ne možemo ih nacrtati! Ova opcija dodaje obris (ili _stroke_) svakom ispunjenom obliku. Ako vaši SVG-ovi nemaju nijedan oblik s potezom, postavlja se automatski. Ako nijedan nema ispunjene oblike, onemogućena je.
* **Invert black lines** - ako su sve linije u vašim SVG-ovima crne, ne možete ih vidjeti! Ova opcija pretvara ih u bijele. Postavlja se automatski ako vaši SVG-ovi imaju samo crne oblike, ali je onemogućena ako ih nema.
* **Render profile** - pogledajte [Profil renderiranja](fundamentals/render-profile.md "mention")
* **scale** - prilagođava veličinu slike.
* položaj **x** i **y** - pogledajte [Koordinatni sustav](fundamentals/co-ordinate-system.md "mention")
* **rotation** - zakrenuti kut slike, u stupnjevima
* **resolution** - pogledajte [Rezolucija](fundamentals/resolution.md "mention")
* **speed** - trajanje cijele animacije, u taktovima.
* **time per frame** - ako je ovo uključeno, trajanje se odnosi na svaki frame, a ne na punu duljinu animacije. Dakle, ako je _speed_ postavljen na ¼, svaki frame trajat će 1 dobu.
* **animation direction** -
  * _FORWARDS_ - animacija se izvodi unaprijed, a zatim se vraća na početak u petlji
  * _BACKWARDS_ - animacija se izvodi unatrag, a zatim se vraća na kraj u petlji
  * _PINGPONG_ - animacija se izvodi unaprijed pa unatrag u petlji
  * _MANUAL_ - trenutačni frame postavlja se postavkom _position manual_
* **position manual** - postavlja trenutačni frame; 0% je prvi frame, 100% je zadnji frame. Može se postaviti ručno ili vanjskim oscilatorom.
* _MOVE TO FRONT / MOVE TO BACK_ - pogledajte [Ispune, mask elementi i sortiranje po dubini](fundamentals/fills-masks-and-depth-sorting.md "mention")

### <img src="../.gitbook/assets/CreatorText.png" alt="" data-size="line"> Text Creator

Stvara tekst pomoću fonta TrueType ili OpenType.

* **Text** - ovdje upišite željeni tekst
* **Font** - odaberite željeni font

{% hint style="info" %}
Za dodavanje više fontova u Liberation kopirajte .ttf ili .otf datoteke u mapu `data/fonts` unutar radne mape Liberation, zatim ponovno pokrenite Liberation.
{% endhint %}

* **Render profile** - pogledajte [Profil renderiranja](fundamentals/render-profile.md "mention")
* **horizontal alignment** - odaberite _LEFT_, _CENTRE_ ili _RIGHT_ za poravnanje teksta.
* **Fill state** - pogledajte [Ispune, mask elementi i sortiranje po dubini](fundamentals/fills-masks-and-depth-sorting.md "mention")
* **size** - veličina teksta
* **monospace** - iscrtava svaki znak jednakom širinom. To je korisno za mjerače vremena i brojače jer se tekst ne pomiče bočno dok se brojevi mijenjaju.
* **character spacing** - podešava razmak između znakova. Povećajte ga za širi prored između znakova ili ga smanjite kako biste tekst zbili.
* **colour -** pogledajte [Postavke boje i HSB](fundamentals/colour-settings-and-hsb.md "mention")
* položaj **x** i **y** - pogledajte [Koordinatni sustav](fundamentals/co-ordinate-system.md "mention")
* **rotation** - zakrenuti kut slike, u stupnjevima
* **resolution** - pogledajte [Rezolucija](fundamentals/resolution.md "mention")
* **reveal** - koristite ovo za postupno otkrivanje teksta, znak po znak. Kada je vrijednost između 0 i 50%, tekst će se postupno pojavljivati slijeva nadesno. Kada je između 50% i 100%, tekst će nestajati slijeva nadesno. Na ovaj priključak možete povezati oscilator za izradu animacija.
* **reveal by word** - kada je uključeno, _reveal_ će raditi riječ po riječ umjesto znak po znak.
* **countdown** - zamjenjuje upisani tekst odbrojavanjem. Kada odbrojavanje dođe do nule, prikazuje se uobičajena vrijednost **Text**.
* **use seconds** - broji u stvarnim sekundama. Kada je ovo isključeno, odbrojavanje se temelji na dobama: dvije dobe računaju se kao jedna sekunda, pa 120bpm odgovara stvarnim sekundama.
* **show minutes/seconds** - prikazuje preostalo vrijeme u minutama i sekundama. Ako je dulje od jednog sata, uključuje i sate.
* **countdown to date/time** - odbrojava do određenog UTC datuma i vremena umjesto odbrojavanja od broja.
* **countdown datetime** - postavlja ciljni UTC datum/vrijeme kada je uključeno **countdown to date/time**.
* **start number** - početni broj kada je **countdown to date/time** isključeno.
* _MOVE TO FRONT / MOVE TO BACK_ - pogledajte [Ispune, mask elementi i sortiranje po dubini](fundamentals/fills-masks-and-depth-sorting.md "mention")

{% hint style="info" %}
Ako je padajući izbornik fontova otvoren, tipke sa strelicama gore i dolje prolaze kroz dostupne fontove.
{% endhint %}
