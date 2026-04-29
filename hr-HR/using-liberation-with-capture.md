---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/using-liberation-with-capture
---

# 🟩 Upotreba programa Liberation s programom Capture

Liberation podržava [Capture](https://capture.se) kao vanjski vizualizator (od verzije 1.0.3 nadalje). Ako već koristite Capture u svom radnom procesu, možete ga upotrijebiti za vizualizaciju živog laserskog izlaza iz Liberation u svojoj 3D sceni.

### Kako radi

Nije potreban poseban postupak povezivanja ni ručno spajanje.

Sve dok su:

* Liberation i Capture na istoj mreži
* vatrozid dopušta vezu

…svi laseri koje ste postavili u Liberation automatski će se pojaviti u Capture kao medijski izvori. Ne morate konfigurirati IP adrese niti omogućavati posebne postavke — jednostavno će se prikazati.

### Prikaz lasera u Capture

Svi konfigurirani laseri u Liberation pojavit će se u Capture kao dostupni medijski izvori.

Da biste stvarno vidjeli izlaz:

* laser mora imati status armed u Liberation
* izvor mora biti dodijeljen laserskom rasvjetnom tijelu u Capture

Nakon što laser ima status armed, Capture će vizualizirati živi izlazni tok iz Liberation. Ako laser u Liberation ima status disarmed, i dalje će biti vidljiv u Capture kao izvor, ali neće ništa izlaziti.

Više uputa i podrške za postavljanje lasera u Capture potražite u dokumentaciji na [capture.se](https://www.capture.se/). <br>

### Ograničenja licence i laseri sa statusom armed

Veze prema Capture tretiraju se potpuno jednako kao fizički laserski izlazi.

To znači:

* u status armed možete postaviti samo onoliko lasera koliko dopušta vaša razina licence
* samo laseri sa statusom armed aktivno će slati podatke u Capture

### Trebam li Capture?

Ne.

Liberation uključuje ugrađeni 3D vizualizator, koji je uvijek dostupan i ne ovisi o razini licence. Možete dizajnirati i pregledavati showove izravno u Liberation, bez vanjskog softvera.

Capture je samo dodatna opcija ako ga već koristite za rasvjetu ili dizajn showa.

### Rješavanje problema

Ako se laseri ne prikazuju u Capture:

* provjerite jesu li obje aplikacije na istoj mreži
* provjerite postavke vatrozida
* provjerite ima li laser status armed u Liberation
