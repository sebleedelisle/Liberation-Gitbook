---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clips/zone-delay-chase
---

# 🟩 Zone delay / chase

Wszyscy się zgodzimy, że więcej laserów to więcej zabawy, ale jeśli wszystkie robią dokładnie to samo, tracisz sporo możliwości twórczych.

System zone delay to prosta, ale skuteczna metoda wprowadzania różnorodności między strefami. Pozwala w pełni wykorzystać konfigurację z wieloma laserami. Można go też użyć do stworzenia bardziej tradycyjnego efektu chase.

#### Jak to działa

_Zone delay_ dodaje opóźnienie do taktowania klipu w kolejnych strefach, tworząc rodzaj przejścia przez strefy.

Bardzo skuteczne jest dodanie zone delay do już odtwarzanego klipu — użyj odpowiedniej kontrolki na APC40, aby regulować poziom i wzór. (Zobacz [Referencja APC40](../reference/apc40-reference.md "mention")). Możesz też użyć panelu _Clip Settings_.

Ustawienia zone delay:

* **Zone delay** — steruje wielkością opóźnienia stosowanego do każdej strefy, mierzoną w nutach 1/64.
* **Pattern** — wybiera kolejność stref
  * Left to right
  * Right to left
  * Inside to outside
  * Outside to inside

{% hint style="info" %}
Pattern działa na numerach stref i zakłada, że strefy są ustawione kolejno od lewej do prawej. Przy obliczaniu wzorów zone delay traktuje strefy canvas i strefy DMX jako osobne grupy.
{% endhint %}

* **Delay mode**
  1. No delay — używaj tego w trybie chase
  2. Delay — tryb domyślny, opóźnia taktowanie każdej strefy
  3. Delay with re-trigger — resetuje klip do początku za każdym razem w kolejnych krokach wzoru. Dobrze działa z _Chase mode_.
* **Chase mode** — gdy chase mode jest włączony, każda strefa jest włączana i wyłączana jak w tradycyjnym efekcie chase. Wygląd chase dostosujesz ustawieniami _Fade in, Hold,_ i _Fade out_. Te ustawienia są określane jako proporcja wartości zone delay, więc wartość 1 oznacza taki sam czas jak podany w _Zone delay_. Trudno to krótko wyjaśnić, więc najlepiej po prostu wypróbować samodzielnie.

{% hint style="info" %}
Zone delay jest stosowany także do wszystkich aktywnych efektów. Na przykład efekt migania zostanie opóźniony między strefami tak samo jak animacja w samym klipie.
{% endhint %}

Gdy klip ma dowolny rodzaj _Zone delay_, w prawym górnym rogu klipu zobaczysz ikonę trzech kropek. Kropki są animowane, aby pokazać styl _Zone delay_ dla tego klipu. Więcej szczegółów znajdziesz w [Co oznaczają małe ikony na przyciskach klipów?](what-are-the-small-icons-on-the-clip-buttons.md "mention").

<figure><img src="../.gitbook/assets/Screenshot 2025-01-21 at 10.00.14.png" alt=""><figcaption><p>Symbol trzech kropek wskazujący, że klip ma zone delay, oraz pokazujący jego tryb</p></figcaption></figure>

{% hint style="info" %}
Zone delay to ustawienie przypisane do każdego klipu. Nie jest globalne — stanowi część kreatywnego projektu klipu.
{% endhint %}
