---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clip-editor/clip-editor-intro
---

# 🟩 Uvod u Clip Editor

Clip Editor svestran je način za izradu laserskog sadržaja i nalazi se u središtu Liberation. Jednostavne stvari možete izraditi lako, a istovremeno je dovoljno fleksibilan za iznimno napredne i složene efekte.

{% hint style="info" %}
Editor temeljen na node strukturi bio je prvi dio Liberation koji je napravljen! Nastao je iz razgovora s Robom Stanleyjem na laserskom susretu u UK-u 2018. o tome kako bi izgledao „objektno orijentirani” dizajner laserskog sadržaja.

Iako djeluje jednostavno, riječ je o prilično složenom sustavu za izgradnju, ali početkom 2019. imao sam funkcionalni demo koji je dokazao koncept — i tako je započelo cijelo ovo putovanje!
{% endhint %}

To je vizualni editor temeljen na node strukturi (ili [arhitekturi node grafa](https://en.wikipedia.org/wiki/Node_graph_architecture#Node_graph)) koji će vam biti poznat ako ste koristili proizvode kao što su TouchDesigner, MaxMSP ili VVVV. Ipak, Clip Editor je malo drukčiji i nešto jednostavniji jer je posebno dizajniran za vektorsku grafiku.

Clip Editor možete otvoriti desnim klikom na gumb Clip i odabirom _EDIT CLIP_. Ili desnim klikom na prazan gumb Clip i odabirom _CREATE AND EDIT CLIP_.

### Pregled

U Clip Editor vidjet ćete:

* gumbe za **Creator** i **Operator node** na vrhu
* gumbe za **Oscillator node** s lijeve strane
* pretpregled sadržaja u panelu s desne strane, a ako kliknete na node, vidjet ćete i drugi pretpregled koji prikazuje sadržaj na samom node
* sve nodes i veze za Clip koji uređujete (ako je riječ o novom Clip, ovo će biti prazno)
* panel Clip Editor s različitim opcijama

Dok uređujete, u pozadini ćete vidjeti i kako Clip izgleda u 3D vizualizatoru.

{% hint style="info" %}
Ako u 3D vizualizatoru ne vidite nikakav izlaz, možda trebate upotrijebiti gumbe za zone kako biste uključili željene zones. Također provjerite je li omogućena opcija _Preview to lasers_; više o tome pogledajte u odjeljku [Panel Clip Editor](clip-editor-intro.md#clip-editor-panel) u nastavku.
{% endhint %}

### Izrada Clip

Obično počinjete s jednim ili više [Creator nodes](creator-nodes.md), a zatim slijeva nadesno povezujete [Operator nodes](operator-nodes/) koji obrađuju sadržaj. Kada približite Creator i/ili Operator nodes, primijetit ćete da se automatski povezuju. Možete ih ponovno razdvojiti povlačenjem kako biste prekinuli vezu.

### Dodavanje nodes u Clip

Kliknite i povucite jedan od gumba za node na vrhu ili s lijeve strane u prazan prostor unutar Clip Editor.

### Podešavanje postavki za node

Kliknite gumb s ikonom zupčanika (gore desno na node) kako biste otvorili panel svojstava za taj node.

### Omogućavanje i onemogućavanje node

Kliknite gumb s ikonom napajanja (gore lijevo na node) kako biste omogućili ili onemogućili node. Node će se zatamniti kako bi se pokazalo da trenutačno nije aktivan. Imajte na umu da sadržaj i dalje prolazi kroz Operator čak i kada je onemogućen, ali node ne utječe na sadržaj.

### Povezivanje nodes

Sadržaj se stvara pomoću Creator node i prosljeđuje se kroz nodes slijeva nadesno; svaki Operator na neki način utječe na sadržaj i prosljeđuje ga sljedećem Operator. Ono što ostane na kraju putanje sadržaj je za Clip. Creators i Operators automatski se povezuju kada ih približite. Da biste ih razdvojili, ponovno ih povucite jedan od drugoga.

{% hint style="info" %}
U ulaz sljedećeg node možete povezati više od jednog node. To je korisno za kombiniranje više dijelova sadržaja.
{% endhint %}

### Svojstva i priključci za node

Svaki node na dnu ima niz priključaka, a svaki od njih predstavlja neko svojstvo unutar node, primjerice svjetlinu, položaj, skaliranje, rotaciju itd.

[Oscilator nodes](oscillators/) mogu se povezati s tim priključcima odozdo i upotrebljavaju se za animiranje tih postavki. Oscillator nodes imaju izlaz na vrhu; kliknite i povucite kako biste izvukli vezu, a zatim je ispustite u jedan od priključaka svojstava na drugim nodes.

### Oscillator nodes

Oscillator nodes služe za mijenjanje svojstava tijekom vremena. Obično predstavljaju valne oblike, kao što su pilasti ili sinusni val, ali neki Oscillator nodes kao izvor koriste vanjske ulaze (primjerice razinu ulaza mikrofona).

{% hint style="info" %}
Ako ste ikada koristili analogni sintesajzer, bit će vam poznat koncept oscilatora, koji se često upotrebljavaju za stvaranje valnih oblika ili podešavanje zvuka tijekom vremena. Oscillators u Liberation rade sličan posao.

**Zanimljivost:** naziv _Liberation_ nadahnut je Moog Liberationom, sintesajzerom tipa „keytar” predstavljenim 1980., koji su proslavili Herbie Hancock, Jean-Michel Jarre pa čak i James Brown!
{% endhint %}

Oscillators uvijek imaju postavke _range_ koje određuju minimalnu i maksimalnu vrijednost svojstva koje se podešava. A _Wave Oscillators_ uvijek imaju postavku _duration_ koja određuje koliko brzo Oscillator mijenja vrijednost. Više informacija potražite u odjeljku [Valni oscilatori](oscillators/wave-oscillators.md).

### Panel Clip Editor

* Timer — na vrhu panela vidjet ćete trenutačno vrijeme za Clip dok se izvodi
* _RETRIGGER_ — ponovno pokreće Clip od početka; posebno korisno ako se Clip ne ponavlja u petlji
* _Preview to lasers_ — kada je ovo označeno, 3D vizualizator ažurirat će se dok uređujete ovaj Clip. Ako to isključite, vidjet ćete Clips koji se izvode izvan editora. Ovo je globalna postavka, nije zasebna za svaki Clip.
* _UNDO/REDO_ — za sam Clip Editor. Također je mapirano na `Cmd / Ctrl + Z` i `Cmd / Ctrl + Shift + Z`.
* _SAVE CLIP_ — sprema vaše izmjene, ali vas upozorava na prepisivanje
* _SAVE AS A COPY_ — sprema vaš Clip u sljedeći dostupni utor u Clip Deck. To postaje nova pozicija za vaš Clip i sva sljedeća spremanja bit će na tom novom mjestu.
* _EXIT EDITOR_ — zatvara Clip Editor. Ako imate nespremljene promjene, prikazat će se panel za potvrdu.
