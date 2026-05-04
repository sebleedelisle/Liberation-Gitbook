---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/midi-control/midi-send-receive
---

# 🟩 MIDI Send/Receive

System MIDI Send/Receive jest niezależny od elementów sterujących APC40 i służy do przesyłania danych MIDI do Liberation oraz z Liberation. Funkcje takie jak uruchamianie i zatrzymywanie klipów, regulacja ustawień globalnych, efektów oraz parametrów klipów mają przypisane polecenia MIDI.

{% hint style="info" %}
System MIDI Send/Receive powstał początkowo, zanim Liberation miał jakąkolwiek funkcjonalność Timeline. Było to obejście pozwalające nagrywać i odtwarzać show w oprogramowaniu muzycznym, takim jak Logic Pro czy Cubase.

Daje on bezpośrednią kontrolę nad klipami, efektami i ustawieniami, niezależnie od położenia przewijania widoku i Clip Deck. Bardziej systemowe funkcje sterowania na żywo, takie jak tap tempo, przypisywanie stref oraz uzbrajanie/rozbrajanie, nie są zaimplementowane.
{% endhint %}

### Ustawienia MIDI Send/Receive

Otwórz panel _MIDI Send/Receive_ (z menu _View -> MIDI Send/Receive_). Zobaczysz opcje _SEND, RECEIVE,_ lub _BOTH_ dla wysyłania i odbierania, a także możliwość wyboru interfejsów MIDI, których chcesz używać.

{% hint style="danger" %}
Używaj ustawienia _BOTH_ ostrożnie. Urządzenia i oprogramowanie MIDI mogą być skonfigurowane tak, aby odsyłać dane, które otrzymują. Może to spowodować pętlę sprzężenia zwrotnego danych MIDI, a to nie jest dobre!
{% endhint %}

### Mapowanie MIDI

Zobacz [Domyślne mapowanie wysyłania/odbioru MIDI](../reference/midi-send-receive-default-mapping.md "mention")

Planuję w przyszłości dodać znacznie bardziej konfigurowalne mapowanie MIDI, ale na razie możesz używać aplikacji takich jak [BOME](https://www.bome.com/products/miditranslator) i [Chetaigne](http://benjamin.kuperberg.fr/chataigne/en), aby tłumaczyć komunikaty między Liberation a własnym sprzętem.
