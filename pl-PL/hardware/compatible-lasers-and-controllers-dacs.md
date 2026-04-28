---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/hardware/compatible-lasers-and-controllers-dacs
---

# ✅ Zgodne lasery i kontrolery (DAC)

### Które lasery są zgodne z Liberation?

Jeśli laser ma standardowe wejście ILDA, możesz używać go z Liberation wraz ze zgodnym kontrolerem laserowym, takim jak Ether Dream lub Helios DAC — [pełna lista znajduje się poniżej](compatible-lasers-and-controllers-dacs.md#compatible-laser-controllers).

<figure><img src="../.gitbook/assets/helios-dac.png" alt="" width="563"><figcaption><p>Helios DAC — najtańsza opcja do użytku domowego</p></figcaption></figure>

Nie potrzebujesz zewnętrznego kontrolera ani wejścia ILDA, jeśli:

* Laser ma wbudowany Ether Dream, lub;
* Masz LaserCube od Wicked Lasers, lub;
* Masz urządzenie X-Laser z wbudowanym Mercury, lub;
* Masz laser Laser Animation Sollinger z wbudowanym kontrolerem AVB (obecnie w testach tylko na macOS)

{% hint style="info" %}
**Czym jest kontroler laserowy?**

Kontroler laserowy (lub DAC) to urządzenie sprzętowe, które odbiera dane cyfrowe z Liberation i konwertuje je na sygnały analogowe wymagane do sterowania skanerami oraz wyjściem lasera. (Stąd DAC: Digital to Analog Converter, czyli konwerter cyfrowo-analogowy).

Kontroler łączy się z komputerem przez USB albo przez standardową sieć komputerową. Może być urządzeniem zewnętrznym albo może być wbudowany w laser.

Jeśli jest zewnętrzny, podłączasz go do lasera przez złącze ILDA. ILDA to standard branżowy korzystający z klasycznego 25-pinowego złącza „D”. Wystarczy kabel ILDA: jeden koniec podłącz do kontrolera, a drugi do lasera.
{% endhint %}

<figure><img src="../.gitbook/assets/etherdream-ilda.png" alt="" width="375"><figcaption><p>Wyjście ILDA w zewnętrznym Ether Dream</p></figcaption></figure>

<figure><img src="../.gitbook/assets/opt-laser-rear.jpg" alt="" width="317"><figcaption><p>Tylny panel lasera z różnymi złączami, w tym wejściem ILDA</p></figcaption></figure>

<figure><img src="../.gitbook/assets/ilda-cable.jpg" alt="" width="375"><figcaption><p>Standardowy kabel ILDA</p></figcaption></figure>

### Który kontroler będzie dla mnie najlepszy?

Jeśli używasz systemu w domu albo prowadzisz małe pokazy z maksymalnie 4 laserami znajdującymi się blisko komputera, kontrolery USB, takie jak **Helios DAC**, są **najbardziej przystępną cenowo** opcją.

Sieciowe DAC, takie jak **Ether Dream**, to **najlepszy wybór dla profesjonalnych** laserystów, którzy mogą skonfigurować sieć i chcą obsługiwać dużą liczbę laserów. Wszystkie duże pokazy Liberation do tej pory były realizowane na Ether Dream.

Jeśli masz **LaserCube**, nie potrzebujesz osobnego kontrolera laserowego — Liberation jest zgodny ze wszystkimi LaserCube. Starsze modele łączą się kablem USB, a nowsze modele przez sieć.

Jeśli jesteś profesjonalistą i szukasz najprostszego rozwiązania, rozważ urządzenia X-Laser z wbudowanym Mercury albo lasery Laser Animation Sollinger korzystające z AVB.

### Zgodne kontrolery laserowe

#### Ether Dream (sieć)

[Ether Dream](https://ether-dream.com) jest dostępny od ponad dziesięciu lat i obecnie występuje w wersji 4 (Liberation działa również z Ether Dream w wersjach 1, 2 i 3). To wyjątkowo niezawodne urządzenia.

Łączysz się z nimi przez standardową sieć. Można je kupić jako samodzielne jednostki albo — jeszcze lepiej — zamontować wewnątrz laserów.

#### Helios (USB)

[Helios](https://bitlasers.com/helios-laser-dac/) to najlepsza opcja dla początkujących. Jest tańszy niż Ether Dream, ale ponieważ łączy się przez USB, nie jest zalecany przy długich odcinkach kabli. Po podłączeniu więcej niż 4 urządzeń mogą też pojawić się problemy z transmisją danych USB i sterownikami, szczególnie w systemie Windows.

Jeśli jednak chcesz uruchomić w domu tylko kilka laserów, to najtańsza i najprostsza opcja.

#### Mercury (wbudowany w urządzenia X-Laser)

[**Mercury**](https://x-laser.com/pages/mercury-laser-control-system) to rozbudowany system sterowania laserami przez DMX firmy X-Laser, zaprojektowany dla realizatorów oświetlenia, którzy chcą obsługiwać lasery bezpośrednio z tradycyjnej konsolety oświetleniowej. Dzięki najnowszej aktualizacji firmware Mercury zawiera także **emulację Ether Dream**, co oznacza, że działa teraz płynnie z Liberation — a także z każdym innym oprogramowaniem obsługującym Ether Dream.

#### AVB (wbudowany w urządzenia Laser Animation Sollinger)

**AVB** to otwarty protokół sieciowy do przesyłania dźwięku i danych o wysokiej wydajności oraz niskim opóźnieniu. Wiele projektorów LaserAnimation Sollinger ma obsługę AVB wbudowaną bezpośrednio w sprzęt, co pozwala Liberation łączyć się z nimi przez sieć bez potrzeby używania zewnętrznych DAC. Obsługa AVB w Liberation jest obecnie **dostępna tylko na macOS i znajduje się w fazie testów**. Wymaga też **zgodnych urządzeń sieciowych obsługujących AVB**. Przy poprawnej konfiguracji zapewnia prostszy przepływ pracy, mniej urządzeń zewnętrznych i wysoką niezawodność podczas profesjonalnych pokazów. I

#### Kontrolery, które będą obsługiwane w przyszłości:

* [IDN](http://www.ilda-digital.com) (otwarty protokół sieciowy od ILDA, możliwy do wdrożenia przez dowolnego producenta)

### Sugestie dotyczące okablowania

Aby uzyskać najlepszą wydajność, trzymaj DAC USB blisko komputera i podłączaj je do laserów dłuższymi kablami ILDA. (Uważaj jednak, bo podczas demontażu kable ILDA potrafią zachowywać się jak hak zaczepny!)

Jeśli używasz Ether Dream, możesz nadal trzymać wszystkie kontrolery razem i łączyć je z laserami długimi kablami ILDA. Możesz też zamontować je blisko laserów i użyć dłuższych kabli sieciowych.

Idealna konfiguracja to Ether Dream (lub inne kontrolery) zamontowane bezpośrednio wewnątrz laserów. W Wielkiej Brytanii może to dla Ciebie zrobić Rob ze Stanwax Laser.
