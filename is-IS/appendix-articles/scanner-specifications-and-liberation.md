---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/appendix-articles/scanner-specifications-and-liberation
---

# 🟩 Tæknilýsingar skanna og Liberation

### Flókinn veruleiki tæknilýsinga skanna

Punktahraði og tæknilýsingar skanna geta verið svolítið ruglingsleg. Þú sérð oft gildi eins og 30kpps @ 8º eða 50kpps @ 4º, en það er ekki alltaf augljóst hvað þessar tölur þýða í raun.

{% hint style="info" %}
Fyrirvari - ég er ekki sérfræðingur í vélbúnaði skanna, en ég hef margra ára reynslu af því að láta skanna af mjög mismunandi gæðum líta vel út með hugbúnaði og myndun punktastraums, frekar en með vélbúnaðarstillingum. Þetta byggist á þeirri reynslu.
{% endhint %}

#### **Hvaðan þessar tölur koma**

Hugtök eins og „30K“ og „50K“ eru styttingar sem byggjast á því hvernig skannar eru metnir með ILDA test pattern við þessi punktahraðagildi og við ákveðnar aðstæður.

Þegar skanni er gefinn upp sem til dæmis: _30Kpps @ 8°_ þýðir það í raun:

> „Þessi skanni getur endurgert ILDA test pattern við 30.000 punkta/sek. með 8° skönnunarhorni, þegar hann er rétt stilltur.“

Þetta er ekki heildstæð eða fullstöðluð mæling á raunverulegri frammistöðu. Í raun var þetta upphaflega alls ekki hannað sem viðmiðunarpróf - heldur notað í **stillingarferli**. Þú keyrir þekkt mynstur við fastan punktahraða (t.d. 30.000 punkta/sek.) og stillir dempun og mögnun þar til það lítur rétt út.

Samt er þetta enn algengasta viðmiðið sem við höfum, og það getur gefið góða hugmynd um gæði skannanna, að minnsta kosti hjá virtum framleiðendum. Hjá _síður traustum_ framleiðendum er þetta þó annað mál...

#### Ef þú vilt prófa skannana samkvæmt uppgefnum gildum

{% hint style="danger" %}
**Þetta er háþróuð aðferð og þú getur skemmt skannana ef þú ferð ekki varlega. Ekki er mælt með þessu nema þú vitir hvað þú ert að gera.**
{% endhint %}

Þú þarft að finna hugbúnað sem getur sent út [ILDA Test Pattern](https://ilda.com/technical.htm?r=7950) - ég held að LaserShowGen geti mögulega gert það - og stilla stærð úttaksins þannig að hún passi við uppgefið skönnunarhorn (t.d. 8°). Sjá ILDA-skjölin fyrir leiðbeiningar um hvernig á að greina úttakið.

#### Af hverju þetta er ekki endilega gott viðmið

Fyrst og fremst getur test pattern birst rangt jafnvel þótt skannarnir séu góðir, einfaldlega vegna þess að þeir eru ekki stilltir sérstaklega fyrir það.

Þetta getur verið gagnlegt almennt viðmið fyrir „góða“ á móti „slæmum“ skönnum, en framleiðendur geta stundum farið ansi frjálslega með þessar tæknilýsingar.

#### Hvernig vel ég þá góðan skanna?

Ég myndi fyrst og fremst tryggja að þeir komi frá virtum framleiðanda. Dýrir hágæðaframleiðendur skanna eins og Cambridge Technology (CT), Eye Magic (EMS) og ScannerMAX (dótturfélag Pangolin) eru alltaf góðir kostir og þar er erfitt að fara úrskeiðis. En þegar par af skönnum kostar um $1000 er það, fyrir mörg okkar sem erum að byrja, dýrara en laserarnir sjálfir!

Þess vegna hef ég aðallega notað kínverska framleiðendur. Dragon Tiger (DT) skannar eru ágætir og á viðráðanlegu verði, og ég held að LightSpace noti þá. Margir aðrir framleiðendur (þar á meðal OPT og Able í sumum gerðum) nota líka kerfi sem byggja á DT.

Phenix Technology (PT) eru almennt í lægri flokki, en satt að segja duga þeir líklega vel fyrir flest.

**Ef skannarnir eru ómerktir er það líklega þá sem þú ættir að hafa áhyggjur af gæðunum!**

#### Hvernig Liberation hjálpar

Í fyrsta lagi þarftu yfirleitt alls ekki mjög dýra skanna! DT með 30kpps á viðráðanlegu verði, eða jafnvel PT, duga vel. Sjálfgefnar stillingar skanna eru viljandi varfærnar og að mestu leyti _ættirðu ekki að þurfa að breyta þeim_ (fyrir utan _Scanner sync_).

Jafnvel þótt þú sért með betri skanna er engin ástæða til að keyra þá meira en þörf er á. Það lengir endingartíma þeirra verulega.

#### Hvað er „punktastraumur“?

Þú hefur líklega heyrt þetta hugtak áður - þetta er leiðin sem við notum til að stjórna ferli skannanna.

Punktastraumur er listi af X/Y-stöðum, hver með lit. Til að teikna til dæmis hvíta línu sendirðu röð punkta eftir línunni, alla stillta á hvítt. Skannarnir færast síðan frá punkti til punkts á föstum hraða - punktum á sekúndu (PPS) - og geislinn teiknar formið.

#### Hvernig þetta virkar í hefðbundnum laserhugbúnaði

Hefðbundinn laserhugbúnaður geymir punktastraum fyrir hvert cue. Fyrir hreyfimynduð cue þýðir það yfirleitt sérstakan punktastraum fyrir hvern ramma. Aðalatriðið er að allt er fyrirfram ákveðið. Þar af leiðandi lætur hærri punktahraði skannana fara hraðar í gegnum sömu fyrirfram skilgreindu gögnin.

{% hint style="info" %}
Í eldri hugbúnaði var þessi aðferð nauðsynleg - tölvur voru einfaldlega ekki nógu hraðar til að búa til punktastrauma í rauntíma. Þess vegna er yfirleitt sérstakur cue-ritill sem er notaður til að búa gögnin til fyrirfram fyrir hvern ramma hreyfimyndarinnar.

Þetta útskýrir líka af hverju efni getur tekið gígabæt af plássi. Í raun ertu að geyma stór, óþjöppuð bylgjuform með nokkuð háum sýnatökutíðnum.
{% endhint %}

#### Af hverju „punktahraði“ skiptir minna máli í Liberation

Liberation býr til punktastrauminn í rauntíma, sem gefur okkur gríðarlegan sveigjanleika. Taktu eftir stillingunni "Scanner speed" í Laser Settings spjaldinu. Hún gerir okkur kleift að hraða á og hægja á skönnunum, en mikilvægt er að hún breytir **ekki** undirliggjandi punktahraða (PPS).

#### Bíddu, hvað? Hvernig?

Ég veit, þetta hljómar undarlega í fyrstu.

Þar sem Liberation býr til punktastrauminn í rauntíma getur það lagað punktastrauminn til. Því dreifðari sem punktarnir eru, því hraðar hreyfast skannarnir. Því nær sem þeir eru hver öðrum, því hægar hreyfast skannarnir.

{% hint style="info" %}
Í nýlegum útgáfum af Liberation hefur raunverulegur _punktahraði_ (í ítarlegum stillingum) engin áhrif á hraða skannanna. Í staðinn aðlagar teiknikerfið dreifingu punktanna að völdum punktahraða, en heldur hreyfingu skannanna óbreyttri.

Þetta hefur áhrif á „upplausn“ punktaleiðarinnar, en það skiptir aðallega máli fyrir grafík (og getur hjálpað við fínstillingu á _Scanner sync_).
{% endhint %}

#### Frábært! Hvað þýðir þetta þá í raun?

Góð spurning. Hér eru mín ráð:

* Forðastu ómerkta skanna. Ef þú getur fengið hraðari skanna, gerðu það - að lágmarki 30KPPS.
* Í flestum tilfellum eru DT30 skannar fínir, og PT30 skannar eru líklega í lagi í ódýrari laserum.
* Ef þú ert að vinna með grafík eru fleiri laserar í flestum tilfellum betri en hraðari skannar.
* Þegar þú ert kominn í hágæðauppsetningar eru allir rótgrónu hágæðaframleiðendurnir góðir kostir.
* Ef þú getur aðeins fengið ódýrustu ómerktu skannana eru sjálfgefnar stillingar Liberation nokkuð varfærnar og þú færð líklega ásættanlega niðurstöðu fyrir einfalda geislavinnu. Ef kerfið á í erfiðleikum skaltu lækka **Speed** stillinguna (en ekki breyta punktahraðanum!).

#### Og ILDA Test Pattern?

…er enn mjög gagnlegt sem kvörðunar- og viðmiðunartæki, en það var aldrei hannað sem heildstætt viðmiðunarpróf og framleiðendur geta misnotað það eða túlkað það frjálslega.
