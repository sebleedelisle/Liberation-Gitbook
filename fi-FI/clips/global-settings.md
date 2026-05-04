---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clips/global-settings
---

# 🟩 Globaalit muunnokset

Klippikohtaisten muunnosten (shift x/y, scale x/y) lisäksi käytössä on Global Transformations, jotka vaikuttavat kaikkiin käynnistämiisi klippeihin. Avaa _Global Transformations_ -paneeli nähdäksesi ne. (Tämä paneeli on yleensä välilehdellä _Clip Settings_ -paneelin vieressä.)

Oletuksena kaikki nämä asetukset nollataan heti, kun yhtään klippiä ei enää ole toistossa. Tämän nollaustoiminnon voi poistaa käytöstä _Global Transformations_ -paneelin alareunassa olevalla _AUTO RESET_ -painikkeella.

{% hint style="info" %}
Huomaa, että Global Transformations eivät vaikuta mihinkään Canvasissa, vaan ainoastaan Beam- ja DMX-alueisiin.
{% endhint %}

### Scale X/Y

Vaaka- ja pystysuuntainen skaalaus. Nämä arvot on lukittu yhteen, ellet paina `Shift`. Oletuksena ne on myös määritetty APC40 Device Control -säätimiin 4 ja 8, ja ne näkyvät Clip Deckin oikealla puolella olevassa kontekstikohtaisessa Parameters-paneelissa.

### Shift X/Y

Vaaka- ja pystysuuntainen siirto. Siirtää kaiken vaakasuunnassa / pystysuunnassa.

### Spin

Pyörittää kaiken sisällön keskikohdan ympäri. Positiivinen arvo pyörittää myötäpäivään, negatiivinen arvo vastapäivään. Huomaat, että tämä asetus vaikuttaa _Rotation_-muunnokseen. Oletuksena tämä on määritetty APC40 Device Control -säätimeen 3, ja se näkyy Clip Deckin oikealla puolella olevassa kontekstikohtaisessa Parameters-paneelissa.

### Spin 3D

Pyörittää kaiken sisällön Y-akselin ympäri (pystysuora viiva keskellä). Huomaat, että tämä asetus vaikuttaa _Rotation3D_-muunnokseen. Oletuksena tämä on määritetty APC40 Device Control -säätimeen 7, ja se näkyy Clip Deckin oikealla puolella olevassa kontekstikohtaisessa Parameters-paneelissa.

### Rotation

Kierto keskikohdan ympäri, arvo asteina.

### Rotation 3D

Kierto Y-akselin ympäri (pystysuora viiva keskellä), arvo asteina.

### Auto reset

Kun tämä on käytössä, kaikki Global Transformations nollataan heti, kun kaikki sillä hetkellä käynnissä olevat klipit poistetaan käytöstä. Näin voit olla varma, ettei seuraavalla kerralla klippiä käynnistäessä tule yllätyksiä!
