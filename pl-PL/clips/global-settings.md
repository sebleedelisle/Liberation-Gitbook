---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clips/global-settings
---

# 🟩 Transformacje globalne

Oprócz transformacji klipu (shift x/y, scale x/y) dostępne są Global Transformations, które mają zastosowanie do każdego uruchamianego klipu. Otwórz panel _Global Transformations_, aby je zobaczyć. (Ten panel zwykle znajduje się na karcie obok _Clip Settings_).

Domyślnie wszystkie te ustawienia zostaną zresetowane, gdy nie będzie już odtwarzany żaden klip. To zachowanie resetowania można wyłączyć przyciskiem _AUTO RESET_ na dole panelu _Global Transformations_.

{% hint style="info" %}
Pamiętaj, że Global Transformations nie wpływają na nic w Canvas, a jedynie na strefy Beam i DMX.
{% endhint %}

### Scale X/Y

Skala pozioma i pionowa. Te wartości są ze sobą powiązane, chyba że naciśniesz `Shift`. Domyślnie są też przypisane do pokręteł APC40 Device Control 4 i 8 oraz widoczne w kontekstowym panelu Parameters po prawej stronie Clip Deck.

### Shift X/Y

Przesunięcie poziome i pionowe. Przesuwa całą zawartość w poziomie / pionie.

### Spin

Obraca całą zawartość wokół środka. Wartość dodatnia obraca zgodnie z ruchem wskazówek zegara, a wartość ujemna przeciwnie do ruchu wskazówek zegara. Zobaczysz, że to ustawienie wpływa na transformację _Rotation_. Domyślnie jest przypisane do pokrętła APC40 Device Control 3 i widoczne w kontekstowym panelu Parameters po prawej stronie Clip Deck.

### Spin 3D

Obraca całą zawartość wokół osi Y (czyli pionowej linii pośrodku). Zobaczysz, że to ustawienie wpływa na transformację _Rotation3D_. Domyślnie jest przypisane do pokrętła APC40 Device Control 7 i widoczne w kontekstowym panelu Parameters po prawej stronie Clip Deck.

### Rotation

Obrót wokół środka, wartość w stopniach.

### Rotation 3D

Obrót wokół osi Y (czyli pionowej linii pośrodku), wartość w stopniach.

### Auto reset

Gdy ta opcja jest włączona, wszystkie Global Transformations zostaną zresetowane, gdy tylko wszystkie aktualnie uruchomione klipy zostaną dezaktywowane. Dzięki temu masz pewność, że przy następnym uruchomieniu klipu nic Cię nie zaskoczy!
