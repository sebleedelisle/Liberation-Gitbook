---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/setting-up/latency-setting
---

# ✅ Ustawienie latencji

W panelu _Settings_ (_Liberation->Settings_ lub CMD/CTRL ,) zobaczysz suwak oznaczony _Latency(ms)._ (W starszych wersjach Liberation znajdował się on w panelu Laser Overview)

{% hint style="info" %}
Domyślne ustawienie latencji 150 ms powinno być odpowiednie w większości przypadków, ale jeśli masz problemy z siecią, warto spróbować je zwiększyć.
{% endhint %}

### Bardziej złożone wyjaśnienie

To ustawienie „latencji klatki” określa maksymalny czas między utworzeniem klatki przez Liberation a rozpoczęciem jej wyświetlania przez laser. Jeśli zwiększysz tę wartość, możesz zauważyć niewielkie opóźnienie między Liberation a wyjściem lasera.

Zaletą dłuższej latencji klatki jest to, że Liberation może jak najszybciej wypełnić bufory kontrolerów laserowych treścią; jeśli w sieci wystąpi przeciążenie, prawdopodobieństwo, że kontrolerowi zabraknie punktów, będzie mniejsze.

Zwykle dotyczy to tylko sieciowych DAC, a ustawienie 100 ms powinno zapewnić dobry kompromis między szybkością a ochroną przed opóźnieniami sieciowymi. Jeśli masz naprawdę stabilną sieć, powinno być możliwe zmniejszenie tej wartości do 50 ms.&#x20;
