---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/dmx-control/introduction
---

# ✅ Wprowadzenie

Liberation zawiera elastyczny i wydajny system DMX, który pozwala tworzyć efekty świetlne i sterować laserami zgodnymi z DMX przez Art-Net. Został zaprojektowany tak, aby łatwo utrzymać oświetlenie w synchronizacji z pokazem laserowym — bez potrzeby używania osobnej konsolety oświetleniowej.

{% hint style="info" %}
**Czym jest Art-Net i jak ma się do DMX?**

**DMX** to system używany od lat do sterowania światłami, laserami, wytwornicami dymu i innymi efektami scenicznymi. Przesyła sygnały sterujące specjalnymi kablami (zwykle ze złączami XLR), a każde urządzenie nasłuchuje określonego zestawu kanałów, aby wiedzieć, co ma robić.

**Art-Net** to nowszy sposób przesyłania tych samych danych DMX przez standardową sieć komputerową. Zamiast specjalnych kabli wszystko jest przesyłane przez Ethernet, podobnie jak ruch internetowy lub lokalny.

W Liberation cały sygnał wyjściowy DMX jest wysyłany za pomocą Art-Net. Możesz używać go do bezpośredniego sterowania urządzeniami zgodnymi z Art-Net albo podłączyć **węzeł Art-Net** — niewielkie urządzenie, które konwertuje Art-Net z powrotem na standardowy sygnał DMX. Dzięki temu nadal możesz sterować tradycyjnymi światłami i efektami DMX, nawet jeśli same nie obsługują Art-Net.
{% endhint %}

Możesz też używać go do sterowania różnego rodzaju sprzętem scenicznym, takim jak wytwornice dymu, hazery, wyrzutnie CO₂, maszyny do zimnych iskier i wiele innych. Jeśli urządzenie obsługuje DMX, możesz skonfigurować je jako strefę DMX i wyzwalać bezpośrednio z Liberation, razem z treściami laserowymi.

Urządzenia DMX są dodawane jako **strefy DMX**, które pojawiają się na liście stref obok stref wiązek laserowych i obszarów docelowych Canvas. Każda strefa DMX używa **presetu DMX**, który informuje Liberation, jak mapować właściwości z Clipów laserowych — takie jak pozycja, kolor i jasność — na wartości kanałów DMX.

Gdy wysyłasz Clip do strefy DMX, Liberation sprawdza pierwszy element w Clipie i konwertuje jego właściwości zgodnie z presetem. Dzięki temu możesz łatwo sterować światłami i efektami DMX bezpośrednio z tych samych Clipów, których używasz już do laserów.

#### Liberation na Glastonbury

<figure><img src="../.gitbook/assets/show-arcadia-spider-2023.jpg" alt=""><figcaption></figcaption></figure>

Pierwszym prawdziwym testem systemu DMX w Liberation był Glastonbury 2023, gdzie Reach Lasers zainstalowało łącznie 90 źródeł wiązek jako część sceny Arcadia „spider”.

18 laserów sterowano za pomocą wewnętrznych Ether Dreams, a kolejne 12 sześciogłowicowych listew z wiązkami sterowano przez Art-Net i DMX.
