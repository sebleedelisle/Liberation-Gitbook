---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clip-editor/operator-nodes/midi-notes
---

# 🟩 MIDI notes

## MIDI notes

Tworzy efekty w stylu „laserowej harfy”, w których przychodzące nuty MIDI wyzwalają wiązki lub kształty w określonym zakresie. Węzeł używa zawartości, którą do niego podasz, jako _źródła_ dla każdej nuty — podaj punkt, a otrzymasz rząd punktów. Podaj kształt, na przykład okrąg, a otrzymasz rząd okręgów; bardziej złożone kształty zostaną powielone w taki sam sposób.

Interfejs MIDI, którego ma nasłuchiwać Liberation, możesz wybrać w **Liberation → Settings** (`Cmd / Ctrl + ,`)

* **midi channel** – kanał MIDI, którego należy nasłuchiwać (0 = wszystkie kanały, 1–16 = konkretny kanał)
* **width** – całkowita szerokość, na której rozłożone są nuty.
* **midi note min / max** – najniższa i najwyższa wartość nuty MIDI w zakresie.
* **ignore out of range notes** – filtruje wszystkie nuty poza ustawionym zakresem. Jeśli ta opcja jest wyłączona, nuty spoza zakresu są „przycinane” do najbliższej dostępnej nuty (wysokie nuty wyzwalają górną granicę zakresu, niskie nuty — dolną).
* **auto extend range** – automatycznie rozszerza zakres, jeśli zostaną zagrane nuty spoza niego.

{% hint style="info" %}
Nie masz pewności, jaki zakres nut otrzymujesz? Włącz **auto extend range**, ustaw **midi note min** bardzo wysoko, a **midi note max** bardzo nisko, a następnie zagraj swoje nuty. System przechwyci je wszystkie i rozszerzy zakres za Ciebie. Gdy masz już wszystko, po prostu wyłącz **auto extend range**, aby zablokować ustawienie.
{% endhint %}

* **leave all notes visible** – tworzy wiązki lub kształty dla wszystkich nut w zakresie, niezależnie od tego, czy są aktualnie odtwarzane, dając efekt „laserowej harfy”.
* **hit colour** – kolor pojawiający się po wyzwoleniu nuty.
* **hit colour hold time** – czas, przez jaki kolor uderzenia pozostaje przy pełnej jasności przed rozpoczęciem zanikania. Wartość jest podawana w sekundach (0–1). _100% = 1 sekunda._
* **hit colour decay time** – czas, w jakim kolor uderzenia zanika po czasie podtrzymania. Wartość jest podawana w sekundach (0–1). _100% = 1 sekunda._

{% hint style="info" %}
Jeśli Twoja zawartość jest już czysto biała, ustawienie koloru uderzenia na biały nic nie zmieni. Aby uzyskać najlepszy efekt, użyj nasyconego koloru dla zawartości i ustaw kolor uderzenia na biały — daje to bardzo przyjemny efekt błysku po wyzwoleniu nut.
{% endhint %}

* **note off fade out time** – czas, w jakim nuta zanika po zwolnieniu. Wartość jest podawana w sekundach (0–1). _100% = 1 sekunda._
* **hit scale factor** – stopień powiększenia nuty po wyzwoleniu (np. 2 = podwójny rozmiar).
* **hit scale hold time** – czas, przez jaki nuta pozostaje powiększona przed powrotem do rozmiaru początkowego. Wartość jest podawana w sekundach (0–1). _100% = 1 sekunda._
* **hit scale decay time** – czas, w jakim nuta wraca do pierwotnego rozmiaru. Wartość jest podawana w sekundach (0–1). _100% = 1 sekunda._
* **note off shrink time** – czas, w jakim nuta wraca do pierwotnego rozmiaru po zwolnieniu. Wartość jest podawana w sekundach (0–1). _100% = 1 sekunda._ (Nie działa, gdy włączone jest **leave all notes visible**.)

{% hint style="info" %}
Skalowanie — pamiętaj, że jeśli Twoja zawartość to pojedynczy punkt, skalowanie nie będzie miało żadnego efektu!
{% endhint %}
