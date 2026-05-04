---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/midi-control/live-control-with-the-apc40
---

# 🟩 Kontrolery MIDI do pracy na żywo

<figure><img src="../.gitbook/assets/qs-apc40.jpeg" alt=""><figcaption></figcaption></figure>

### **Kontroler APC40**

To domyślny kontroler sprzętowy dla Liberation; jest zdecydowanie zalecany i można śmiało powiedzieć, że Liberation od samego początku projektowano z myślą o tym sprzęcie. Gdy tylko podłączysz APC40, Liberation automatycznie się z nim połączy.

{% hint style="warning" %}
_O nie! Wtyczka USB została odłączona w połowie pokazu!_

Bez paniki — po prostu podłącz ją ponownie. Liberation automatycznie wznowi połączenie, bez żadnych problemów.
{% endhint %}

### APC40 Mark 1 czy Mark 2?

Krótko mówiąc, zalecany jest Mark 2, ponieważ ma przyciski w pełnym kolorze, które lepiej odpowiadają interfejsowi Clip Deck w Liberation. Wersja Mark 1 też zadziała w razie potrzeby, ale będzie nieco mniej intuicyjna, ponieważ układ różni się trochę od tego, co widać na ekranie, a przyciski mogą świecić tylko na czerwono, pomarańczowo lub zielono, więc nie będą odpowiadać kolorom klipów.

{% hint style="info" %}
Oryginalny APC40 Mark 1 pojawił się w 2009 roku (!) i niektórzy nadal go preferują ze względu na metalową obudowę oraz solidną, konsolową konstrukcję. Zaktualizowany Mark 2 pojawił się w 2014 roku i choć został wycofany z produkcji w 2024 roku, ze względu na zapotrzebowanie ze strony artystów wizualnych (Resolume itd.) oraz laseristów wraca do produkcji w 2025 roku.
{% endhint %}

Pełną listę elementów sterujących dostępnych na APC40 znajdziesz w [Referencja APC40](../reference/apc40-reference.md "mention")

### APC Mini

Liberation 1.0.3 zawiera także profil APC Mini. Mapuje siatkę 8x5 dla Clips, przyciski zone, elementy sterujące odwróceniem X/Y dla zone, przyciski grup, zatrzymanie wszystkich Clips, przechodzenie między stronami Clips, przechodzenie między stronami zones, tap tempo, reset taktu oraz korektę tempa. Suwaki sterują poziomami efektów, a suwaki z wciśniętym Shift sterują parametrami efektów. Ostatni suwak steruje Global Brightness.

### MIDI Fighter Twister

Profil MIDI Fighter Twister jest przeznaczony raczej do sterowania opartego głównie na enkoderach niż do uruchamiania Clips. Jeden rząd enkoderów steruje parametrem 1 w slotach efektów 1-8, a kolejny rząd podąża za ośmioma kontekstowymi elementami sterującymi w panelu Parameters, w tym za clip shift, opóźnieniem zone, globalnym spin/scale oraz wygaszaniem grup.
