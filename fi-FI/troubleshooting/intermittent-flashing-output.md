---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/troubleshooting/intermittent-flashing-output
---

# ✅ Katkonainen / vilkkuva lähtö

Avaa _Laser Overview_ -paneeli ja tarkista ongelmia aiheuttavan laserin vieressä oleva yhteysvalo.

**Jos yhteysvalo EI pala jatkuvasti vihreänä:**\
Kyseessä on todennäköisesti joko verkko- tai suorituskykyongelma:

**Verkon suorituskyky –**

* Varmista, ettet ole yhteydessä wifi-verkkoon. Käytä aina langallista yhteyttä. Varmista, että käyttöjärjestelmä priorisoi langallisen verkon wifin sijaan, tai poista wifi käytöstä, jos et ole varma.
* Tarkista verkkosovitin ja kokeile toista USB-C-sovitinta.
* Windows-käyttäjät: tarkista / päivitä verkkoajurit ja suorita sopivat verkon testaustyökalut.
* Tarkista kaikki kaapelointi, kytkimet ja reitittimet. Vaihda ja testaa jokainen kaapeli järjestelmällisesti.
* Käynnistä kaikki verkkolaitteet uudelleen, mukaan lukien kytkimet, reitittimet ja jokainen Ether Dream.

**CPU-suorituskyky**

Jos tietokoneesi on vanha tai teholtaan heikko, se voi olla liian hidas Liberationin käyttöön. Tarkista kuvakepalkin oikeassa reunassa oleva kuvataajuuden ilmaisin.

Siinä näkyy kaksi lukua: todellinen kuvataajuus ja tavoitekuvataajuus. Jos todellinen kuvataajuus laskee alle 30:n, ongelmia voi ilmetä.

Seuraavista toimista voi olla apua:

* Poista käyttämättömät laserit, eli jos käytössä on vain yksi laser, poista muut.
* Vaihda Output- tai Canvas-näkymään.
* Sulje kaikki muut ohjelmat, tarkista verkon palomuuriasetukset ja sulje virustorjunta, Dropbox jne.
* Pienennä näytön resoluutiota ja tee Liberation-ikkunasta pienempi.

Jos mikään näistä ei auta, harkitse tietokoneen päivittämistä.

***

**Jos yhteysvalo PALAA jatkuvasti vihreänä:**

Kyseessä on todennäköisesti laitteisto-ongelma. Tämä ei kuulu tämän ohjekirjan piiriin, mutta voit kokeilla seuraavia toimia:

* Poista SFS (Scan Fail Safety) -järjestelmä käytöstä. Joissakin lasereissa on toiminto, joka poistaa lähdön käytöstä, jos skannerit lakkaavat liikkumasta eli tuottavat voimakkaan staattisen säteen. Ne voivat olla hieman liian varovaisia / epäluotettavia.

{% hint style="danger" %}
Ole erittäin varovainen, kun poistat scan fail safety -järjestelmän käytöstä. Voimakkaat staattiset säteet voivat polttaa! Varmista, että sinulla on hätäpysäytyspainike ja sammutin käden ulottuvilla.
{% endhint %}

* Tarkista turvalukituskaapelit ja -järjestelmät.
* Tarkista kaikki ohjaimen ja laserin väliset kaapelit.

[ILDA Gem](https://shop.stanwaxlaser.co.uk/ilda-gem-pocket-2020-718-p.asp) voi olla korvaamaton työkalu laserongelmien vianmäärityksessä.
