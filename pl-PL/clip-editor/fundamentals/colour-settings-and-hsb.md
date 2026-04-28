---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clip-editor/fundamentals/colour-settings-and-hsb
---

# 🟩 Ustawienia koloru i HSB

Kolor w Liberation jest definiowany jako HSB, a nie RGB. Na początku może to być mniej znane, ale po krótkim przyzwyczajeniu ten system okazuje się dużo bardziej intuicyjny.

{% hint style="info" %}
Jeśli wolisz używać RGB, możesz kliknąć kwadrat koloru w dowolnym ustawieniu koloru. Otworzy to panel edytora koloru, w którym dostępne są opcje RGB i HSB.
{% endhint %}

### HSB — Hue, Saturation i Brightness

#### Hue

Odcień koloru ma zakres od 0 do 255. 0 oznacza czerwony, a wraz ze zwiększaniem wartości przechodzisz przez wszystkie odcienie tęczy: pomarańczowy, żółty, zielony, cyjan, niebieski, fioletowy, magentę, a następnie z powrotem do czerwonego przy 255.

Ponieważ jest to pętla, możesz użyć fali trójkątnej, aby cyklicznie przechodzić przez wszystkie kolory.

#### Saturation

To ustawienie reguluje nasycenie, czyli intensywność koloru. Innymi słowy, określa, jak bardzo jest _kolorowy_, i ma zakres od 0 do 255. Ustaw _Saturation_ na 0, aby uzyskać odcienie szarości, lub na 255, aby uzyskać pełne kolory tęczy. Wartości pośrodku dadzą pastelowe, wypłowiałe kolory.

{% hint style="info" %}
Przepraszam moich znajomych z USA za dodatkową samogłoskę w słowie „colour”. Liberation powstaje w Anglii, więc domyślnie używany jest brytyjski angielski. W przyszłości mam nadzieję udostępnić tłumaczenia na francuski, hiszpański, niemiecki, włoski, chiński uproszczony i tak — nawet amerykański angielski. :innocent:
{% endhint %}

#### Brightness

Prawdopodobnie najprostsze do zrozumienia: 0 oznacza całkowitą czerń, a 255 pełną jasność.

### Przykłady użycia

#### Cykl tęczy:

Ustaw _Brightness_ i _Saturation_ na 255. Podłącz oscylator _Sawtooth_ do gniazda _Hue_ i ustaw jego zakres od 0 do 255.

#### Pulsująca jasność:

Podłącz oscylator _Sawtooth_ do gniazda _Brightness_ i ustaw jego zakres od 255 do 0. Możesz dodatkowo dostosować wartości clamp min i max, aby sprawdzić czas trwania zmiany. Następnie użyj funkcji easing, aby jeszcze dokładniej dopracować animację.

#### Mocny błysk / stroboskop:

Wybierz kolor za pomocą _Hue_ i _Saturation_ albo klikając próbnik koloru. Podłącz oscylator _Square Wave_ do gniazda _Brightness_ i ustaw jego zakres od 255 do 0.

#### Przechodzenie przez niestandardowy zakres odcieni:

Ustaw _Brightness_ i _Saturation_ na 255. Podłącz oscylator _Triangle Wave_ do gniazda _Hue_ i ustaw jego zakres:

* dla przejścia od niebieskiego do cyjanu użyj zakresu od 70 do 128
* dla przejścia od czerwonego do żółtego użyj zakresu od 0 do 40
* dla przejścia od czerwonego do magenty użyj zakresu od 255 do 220
