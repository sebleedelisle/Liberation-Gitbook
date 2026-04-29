# ✅ Panel ustawień Laser output

Otwórz panel ustawień _Laser output_ z menu _View -> Laser Output Settings._

<figure><img src="../../.gitbook/assets/Copy Laser Setting in Laser Output.png" alt="" width="326"><figcaption></figcaption></figure>

Zobaczysz ustawienia aktualnie wybranego lasera, które możesz zmienić:

* za pomocą jego przycisku z numerem w panelu _Laser overview_
* klawiszem numerycznym na klawiaturze — klawisze od 1 do 0 otwierają lasery 1–10
* klawiszem `Tab`, aby przechodzić kolejno przez lasery (`Shift + Tab` przechodzi wstecz).

U góry tego panelu zobaczysz:

* przycisk z numerem — kliknij go, aby uzbroić/rozbroić ten laser. Gdy laser jest uzbrojony, przycisk jest czerwony.
* suwak _Brightness_ tylko dla tego lasera. Pamiętaj, że ta wartość łączy się z jasnością globalną.
* przełącznik _Test Pattern_ i wybór wzoru. Pozwala to wybrać konkretny wzór testowy tylko dla tego lasera. (Te elementy sterujące są odzwierciedlone na pasku narzędzi widoku Output).

### Orientacja wyjścia / korekcja odbicia lustrzanego

Kolejne elementy służą do skorygowania konfiguracji lasera tak, aby działał spójnie w Liberation.

* **Flip horizontal / vertical** — te opcje pozwalają skorygować wyjście lasera

{% hint style="info" %}
Nie powinno być potrzeby zmiany ustawień Flip horizontal / vertical, chyba że laser został nieprawidłowo okablowany albo ma z tyłu przyciski odwrócenia X/Y, które nie są ustawione poprawnie. Jeśli chcesz odwrócić wyjście dla konkretnego klipu, możesz zrobić to bezpośrednio w ustawieniach tego klipu.
{% endhint %}

* **Orientation** — jeśli laser został zamontowany bokiem lub do góry nogami, możesz skorygować obrót tym ustawieniem.
* **Fine position adjustments** — można ich użyć do skorygowania bardzo niewielkiego przesunięcia lub obrotu. Służą do korekty dryfu/osiadania, jeśli laser był pozostawiony na noc lub na dłuższy czas.

{% hint style="info" %}
Pamiętaj, że korekcje orientacji / odbicia lustrzanego nie zmieniają niczego w 3D Visualiser. Należy ich używać do dopasowania wyjścia rzeczywistego lasera do tego, co widać w 3D Visualiser!
{% endhint %}

### Kopiowanie ustawień lasera

Zobacz [Panel ustawień Laser output](./#copy-laser-settings).

### Ustawienia skanerów

<figure><img src="../../.gitbook/assets/Laser output scanner settings.png" alt=""><figcaption></figcaption></figure>

#### **Speed**

Ustawienie Speed określa, jak szybko poruszają się skanery.

{% hint style="danger" %}
Chociaż ustawienia domyślne są dość zachowawcze, nadal możesz uszkodzić skanery, jeśli będą pracować zbyt szybko. Zachowaj ostrożność, szczególnie podczas zwiększania prędkości.
{% endhint %}

{% hint style="info" %}
To ustawienie prędkości nie zmienia częstotliwości punktów. Zamiast tego reguluje, jak bardzo punkty są od siebie oddalone. Więcej informacji znajdziesz w [◼️ Jak Liberation generuje treści laserowe](../../advanced/how-liberation-generates-laser-content.md)
{% endhint %}

#### **Scanner sync (Colour shift / blank shift)**

Wiązka zmienia kolor oraz włącza się i wyłącza, gdy skanery ją przemieszczają. Te dwie rzeczy zwykle nie są idealnie zsynchronizowane. Dostosuj to ustawienie, aby je wyrównać.

{% hint style="info" %}
Czasami nazywa się to _blank shift_, ale osobiście wolę termin _scanner sync_ — jest nieco dokładniejszy, ponieważ reguluje taktowanie wszystkich zmian koloru względem ruchu skanera.
{% endhint %}

<div><figure><img src="../../.gitbook/assets/Colour shift tails.jpeg" alt="" width="320"><figcaption><p>„Ogonki” lasera — Colour shift nie jest poprawnie ustawiony</p></figcaption></figure> <figure><img src="../../.gitbook/assets/Colour shift no tails.jpeg" alt="" width="320"><figcaption><p>Brak „ogonków” lasera! Colour shift ustawiony poprawnie!</p></figcaption></figure></div>

Jeśli na wyjściu lasera widzisz małe „ogonki”, prawdopodobnie trzeba dostosować Scanner sync. Jeśli ogonki pojawiają się niezależnie od ustawienia, najpewniej sterujesz skanerami lub driverami lasera szybciej, niż są w stanie pracować. Spróbuj zmniejszyć prędkość skanerów.

#### Scanner presets

Użyj tego ustawienia, aby wybrać gotową konfigurację skanerów. Opcja domyślna zwykle jest odpowiednia, więc nie powinno być potrzeby jej zmiany, chyba że masz szczególnie słabe (albo szczególnie dobre) skanery. Jeśli chcesz dowiedzieć się więcej, zobacz [◼️ Presety skanera i profile renderowania](../../advanced/scanner-presets.md)

#### Colour calibration

Ten system pozwala skorygować krzywą jasności i balans bieli lasera. Zobacz [Kalibracja kolorów](../../advanced/colour-calibration.md)

#### Advanced settings

Nie powinno być potrzeby zmieniania tych ustawień, ale jeśli chcesz dowiedzieć się więcej, zobacz [◼️ Zaawansowane ustawienia lasera](../../advanced/advanced-laser-settings.md)
