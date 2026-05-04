---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clips/global-settings
---

# 🟩 Globala transformationer

Utöver clip-transformationer (shift x/y, scale x/y) finns Global Transformations som tillämpas på varje clip du kör. Öppna panelen _Global Transformations_ för att se dem. (Den här panelen finns vanligtvis på en flik bredvid _Clip Settings_).

Som standard återställs alla dessa inställningar så snart inga clips längre spelas. Den här automatiska återställningen kan inaktiveras med knappen _AUTO RESET_ längst ned i panelen _Global Transformations_.

{% hint style="info" %}
Observera att Global Transformations inte påverkar något på Canvas, utan bara Beam- och DMX-zoner
{% endhint %}

### Scale X/Y

Horisontell och vertikal skala. Dessa värden är låsta tillsammans om du inte trycker på `Shift`. Som standard är de också mappade till APC40 Device Control-rattarna 4 och 8 och visas i den kontextuella Parameters-panelen till höger om Clip Deck.

### Shift X/Y

Horisontell och vertikal förskjutning. Flyttar allt horisontellt/vertikalt.

### Spin

Snurrar allt innehåll runt mitten. Ett positivt värde snurrar medurs, ett negativt värde snurrar moturs. Du ser att den här inställningen påverkar transformationen _Rotation_. Som standard är den mappad till APC40 Device Control-ratt 3 och visas i den kontextuella Parameters-panelen till höger om Clip Deck.

### Spin 3D

Snurrar allt innehåll runt Y-axeln (som är en vertikal linje i mitten). Du ser att den här inställningen påverkar transformationen _Rotation3D_. Som standard är den mappad till APC40 Device Control-ratt 7 och visas i den kontextuella Parameters-panelen till höger om Clip Deck.

### Rotation

En rotation runt mitten, värde i grader.

### Rotation 3D

En rotation runt Y-axeln (som är en vertikal linje i mitten), värde i grader.

### Auto reset

När detta är aktiverat återställs alla Global Transformations så snart alla clips som körs för tillfället avaktiveras. Då kan du vara säker på att du inte får några överraskningar nästa gång du kör ett clip!
