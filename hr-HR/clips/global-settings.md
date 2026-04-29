---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clips/global-settings
---

# 🟩 Globalne transformacije

Osim transformacija za Clip (shift x/y, scale x/y), postoje i Globalne transformacije koje se primjenjuju na svaki Clip koji pokrenete. Otvorite panel _Global Transformations_ da biste ih vidjeli. (Taj je panel obično u kartici uz _Clip Settings_).

Prema zadanim postavkama, sve će se te postavke resetirati čim više nema aktivnih Clips. To automatsko resetiranje možete isključiti gumbom _AUTO RESET_ pri dnu panela _Global Transformations_.

{% hint style="info" %}
Imajte na umu da Globalne transformacije ne utječu ni na što u Canvas, nego samo na beam zone i DMX zone
{% endhint %}

### Scale X/Y

Horizontalno i vertikalno skaliranje. Te su vrijednosti povezane osim ako pritisnete `Shift`. Prema zadanim postavkama, mapirane su i na APC40 Device Control knob 4 i 8 te se prikazuju u panelu desno od Clip Deck.

### Shift X/Y

Horizontalni i vertikalni pomak. Pomiče sve horizontalno/vertikalno.

### Spin

Okreće sav sadržaj oko središta. Pozitivna vrijednost okreće u smjeru kazaljke na satu, a negativna vrijednost u suprotnom smjeru. Vidjet ćete da ova postavka utječe na transformaciju _Rotation_. Prema zadanim postavkama mapirana je na APC40 Device Control knob 3 i prikazuje se u panelu desno od Clip Deck.

### Spin 3D

Okreće sav sadržaj oko osi Y (to je vertikalna linija u središtu). Vidjet ćete da ova postavka utječe na transformaciju _Rotation3D_. Prema zadanim postavkama mapirana je na APC40 Device Control knob 7 i prikazuje se u panelu desno od Clip Deck.

### Rotation

Rotacija oko središta, vrijednost u stupnjevima.

### Rotation 3D

Rotacija oko osi Y (to je vertikalna linija u središtu), vrijednost u stupnjevima.

### Auto reset

Kada je uključeno, ova će opcija resetirati sve Globalne transformacije čim se deaktiviraju svi trenutačno pokrenuti Clips. Tako možete biti sigurni da vas sljedeći put kad pokrenete Clip neće dočekati nikakva iznenađenja!
