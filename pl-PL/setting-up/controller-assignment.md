---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/setting-up/controller-assignment
---

# ✅ Przypisywanie kontrolerów

Po skonfigurowaniu laserów w Liberation możesz przypisać każdy z nich do rzeczywistego kontrolera laserowego. (Zobacz [Zgodne lasery i kontrolery (DAC)](../hardware/compatible-lasers-and-controllers-dacs.md "mention"), aby sprawdzić, jakiego sprzętu możesz użyć). Kontrolery będą podłączone przez USB albo przez sieć.

* Otwórz panel _Controller Assignment_ z menu _View -> Controller Assignment_. (Alternatywnie możesz użyć przycisku _ASSIGN LASER CONTROLLERS_ w panelu _Laser Overview_.)

<figure><img src="../.gitbook/assets/Screenshot 2024-12-31 at 14.30.18.png" alt="Controller Assignment panel"><figcaption></figcaption></figure>

* Panel jest podzielony na dwie części: po lewej znajduje się lista laserów, a po prawej lista dostępnych kontrolerów. Jeśli nie widzisz swojego kontrolera laserowego na liście, naciśnij przycisk _REFRESH_. Jeśli problem nadal występuje, zobacz [Rozwiązywanie problemów](../troubleshooting/ "mention").
* Aby przypisać kontroler do lasera, kliknij go po prawej stronie i przeciągnij do wolnego slotu lasera po lewej. Dzięki temu Liberation wie, którego kontrolera użyć dla danego lasera. (Jeśli zmienisz zdanie, możesz swobodnie przeciągać kontrolery w górę i w dół, z jednego lasera na inny.)

<figure><img src="../.gitbook/assets/Screenshot 2024-12-31 at 14.33.23.png" alt="List of controllers" width="375"><figcaption></figcaption></figure>

* Zielony kwadrat obok kontrolera oznacza, że Liberation pomyślnie się z nim połączył.

<figure><img src="../.gitbook/assets/controller-assignment-laser-list" alt="" width="338"><figcaption><p>Ether Dream i Helios DAC przypisane odpowiednio do laserów 2 i 3</p></figcaption></figure>

{% hint style="info" %}
Pamiętaj, że przy każdym połączeniu z kontrolerem laser zostanie automatycznie rozbrojony.
{% endhint %}

* Pomarańczowy kwadrat 🟧 oznacza, że kontroler ma okresowe problemy z połączeniem. Zwykle wynika to z problemu z siecią — zobacz [Rozwiązywanie problemów](../troubleshooting/ "mention").
* Czerwony kwadrat 🟥 oznacza, że nie można połączyć się z kontrolerem — zobacz [Rozwiązywanie problemów](../troubleshooting/ "mention").
* Przycisk _disconnect button_ (X) rozłącza kontroler, ale nie usuwa go z przypisania do lasera. Następnie możesz użyć przycisku _reconnect button_ (ikona odświeżania), aby połączyć go ponownie, albo kliknąć jeszcze raz _disconnect button_, aby usunąć przypisanie.
* _Funkcja zaawansowana:_ Otwórz panel analityki kontrolera, klikając przycisk wyglądający jak wykres. To funkcja zaawansowana, która pokazuje szczegółowe informacje o strumieniu danych i może pomóc w rozwiązywaniu problemów. (Ta opcja może nie być dostępna dla niektórych typów kontrolerów).
* Możesz użyć przycisku _rename button_ (ołówek), aby zmienić nazwę tego kontrolera na dowolną. Warto nadać mu nazwę, która ułatwia skojarzenie go z konkretnym sprzętem. Jeśli kontroler jest wbudowany w laser, możesz nazwać go odpowiednio, np. _LaserCube Ultra #1_ albo _Triton T5 #3._ Te nazwy zostaną zapisane w Twojej instalacji Liberation i będą od tej pory widoczne; może to bardzo ułatwić szybkie rozpoznawanie laserów.

{% hint style="info" %}
Wskazówka — **kliknij dwukrotnie** kontroler po prawej stronie, aby automatycznie przypisać go do następnego dostępnego lasera po lewej. To może naprawdę zaoszczędzić czas, jeśli masz do przypisania dużo laserów!
{% endhint %}

Przycisków _DISCONNECT ALL_ i _RECONNECT ALL_ możesz użyć do szybkiego zresetowania wszystkich połączeń. Jest to przydatne, gdy występują problemy z siecią.
