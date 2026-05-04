---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/advanced/colour-calibration
---

# 🟩 Kalibracija boja

Kalibracija boja osigurava da crveni, zeleni i plavi laseri vašeg projektora emitiraju svjetlo glatko i predvidljivo na svim razinama svjetline. Različiti projektori mogu imati nelinearne krivulje svjetline, što znači da 50% crvene može izgledati znatno svjetlije ili tamnije od polovice intenziteta 100% crvene. Kalibracija to ispravlja kako bi se boje čisto miješale, gradijenti izgledali glatko, a bijela bila uravnotežena.

#### Zagrijavanje projektora

Laserske diode mijenjaju ponašanje dok se zagrijavaju. Prije kalibracije uvijek pustite da se projektor stabilizira:

* Projicirajte svijetli kadar, primjerice **White rectangle test pattern (11)**, najmanje **15–20 minuta**.
* Time osiguravate da će balans boja koji postavite ostati dosljedan tijekom nastupa.

#### Kako radi kalibracijski test

Za kalibraciju upotrijebite test pattern (pogledajte [Testni uzorci](../output-view/test-patterns.md "mention"))

* **5** – Crvena
* **6** – Zelena
* **7** – Plava
* **8** – Bijela

Svaki od njih prikazuje četiri pokretne linije. Na svjetlinu u laserskom sustavu ne utječe samo razina snage, nego i vrijeme koje zraka provede na jednom mjestu. Kad se skeneri kreću brže, zraka provodi manje vremena na svakoj točki i izgleda tamnije.

Kako bi se to uzelo u obzir, testni uzorci zajedno skaliraju i svjetlinu i brzinu:

* **Gornja linija** – 100% svjetline pri punoj brzini
* **Druga linija** – 75% svjetline pri 75% brzine
* **Treća linija** – 50% svjetline pri 50% brzine
* **Četvrta linija** – 25% svjetline pri 25% brzine

Budući da se zajedno skaliraju i svjetlina _i brzina_, sve bi linije trebale izgledati jednako svijetlo. Ako jedna linija izgleda svjetlije ili tamnije, prilagodite odgovarajući klizač dok se ne izjednače.

Svaki testni uzorak ima i petu liniju na **0% svjetline**, koja ne bi trebala biti vidljiva. Ona se koristi za korekciju lasera koji ne emitiraju svjetlo na vrlo niskim razinama. Ako laser pri niskoj svjetlini ostaje nevidljiv, postupno povećavajte **postavku 0%** dok linija ne postane tek vidljiva, a zatim je malo smanjite dok ponovno ne nestane. Cilj je pronaći prag na kojem se laser počinje paliti, a zatim ostati neposredno ispod njega - kako bi prijelazi svjetline počinjali prirodno, bez odsijecanja donjeg raspona.

#### Upotreba panela Colour Calibration

Panel vam daje neovisne kontrole za svaki kanal (crveni, zeleni, plavi) na razinama 100, 75, 50, 25 i 0%.

1. **Odaberite test pattern** (počnite s crvenom).
2. **Prilagodite klizače** tako da linije 100, 75, 50 i 25% izgledaju jednako svijetlo.
3. **Fino podesite klizač 0%** ako je linija za “isključeno” još uvijek blago vidljiva.
4. **Ponovite za zelenu i plavu.**
5. Prebacite se na **White test pattern (8)**. Sve četiri linije trebale bi izgledati jednako, a bijela bi trebala djelovati neutralno (bez obojenog tona).

#### Podešavanje balansa bijele

Ovaj sustav možete upotrijebiti i za podešavanje **balansa bijele**. Nakon što kalibrirate svaki kanal zasebno, prebacite se na **White test pattern (8)**. Ako izlaz izgleda obojeno (na primjer previše zeleno ili previše plavo), prilagodite relativne razine crvenog, zelenog i plavog kanala dok linije ne postanu neutralno bijele. Čak i ako se vaši laseri znatno razlikuju po snazi, kalibracija će ih ipak pomoći približiti jedne drugima i proizvesti čišću, uravnoteženiju mješavinu boja.

#### Spremanje kalibracije

* Upotrijebite **Store** za prepisivanje trenutačne zadane postavke.
* Upotrijebite **Store As** za izradu nove zadane postavke (korisno ako radite s više lasera).
