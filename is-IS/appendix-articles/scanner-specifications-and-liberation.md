---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/appendix-articles/scanner-specifications-and-liberation
---

# 🟩 Forskriftir skanna og Liberation

### Flókinn veruleiki forskrifta skanna

Punktahraði og forskriftir skanna geta verið svolítið ruglingsleg. Þú sérð oft forskriftir eins og 30kpps @ 8º eða 50kpps @ 4º, en það er ekki alltaf augljóst hvað þessar tölur þýða í raun.

{% hint style="info" %}
Fyrirvari - ég er ekki sérfræðingur í skannavélbúnaði, en ég hef margra ára hagnýta reynslu af því að láta skanna af mjög mismunandi gæðum líta vel út með hugbúnaði og myndun punktastraums, frekar en stillingum á vélbúnaði. Þetta byggir á þeirri reynslu.
{% endhint %}

#### **Hvaðan þessar tölur koma**

Hugtök eins og „30K“ og „50K“ eru styttingar sem byggja á því hvernig skannar eru metnir með ILDA-prófunarmynstrinu við þessa punktahraða og við ákveðnar aðstæður.

Þegar skanni er gefinn upp sem eitthvað á borð við: _30Kpps @ 8°_ þýðir það í raun:

> „Þessi skanni getur endurgert ILDA-prófunarmynstrið við 30.000 punkta/sek við 8° skannhorn, þegar hann er rétt stilltur.“

Þetta er ekki yfirgripsmikil eða fullkomlega stöðluð mæling á raunverulegri frammistöðu. Reyndar var þetta upphaflega alls ekki hannað sem viðmiðunarpróf - heldur var það notað í **stillingarferli**. Þú keyrir þekkt mynstur á föstum punktahraða (t.d. 30.000 punkta/sek) og stillir dempun og mögnun þar til það lítur rétt út.

En þetta er samt útbreiddasta viðmiðið sem við höfum, og það getur gefið þér góða hugmynd um gæði skannanna, að minnsta kosti hjá virtum framleiðendum. Hjá _minna virtum_ framleiðendum hins vegar...

#### Ef þú vilt prófa skannana samkvæmt uppgefnum gildum

{% hint style="danger" %}
**Þetta er háþróuð aðferð og þú getur skemmt skannana ef þú ferð ekki varlega. Ekki mælt með þessu nema þú vitir hvað þú ert að gera.**
{% endhint %}

Þú þarft að finna hugbúnað sem getur sent út [ILDA Test Pattern](https://ilda.com/technical.htm?r=7950) - ég held að LaserShowGen geti mögulega gert það - og stilla úttaksstærðina þannig að hún passi við uppgefið skannhorn (t.d. 8°). Sjá ILDA-skjölin fyrir leiðbeiningar um hvernig á að greina úttakið.

#### Af hverju þetta er kannski ekki gott viðmið

Í fyrsta lagi gæti prófunarmynstrið þitt birst rangt jafnvel þótt skannarnir séu góðir, vegna þess að þeir eru ekki stilltir á þann hátt sem hentar prófinu best.

Þetta getur verið gagnleg almenn leiðbeining til að greina á milli „góðra“ og „slæmra“ skanna, en framleiðendur geta stundum farið frjálslega með þessar forskriftir.

#### Hvernig vel ég þá góðan skanna?

Ég held að það mikilvægasta sé einfaldlega að tryggja að þeir séu frá virtum framleiðanda. Dýrir hágæða skannaframleiðendur eins og Cambridge Technology (CT), Eye Magic (EMS) og ScannerMAX (dótturfyrirtæki Pangolin) eru alltaf góðir og þú getur varla farið úrskeiðis með þá. En þegar skannapar kostar um $1000 er það, fyrir mörg okkar sem eru að byrja, dýrara en laserarnir okkar!

Þess vegna hef ég að mestu notað kínverska framleiðendur. Dragon Tiger (DT) skannar eru ágætir og á viðráðanlegu verði, og ég held að LightSpace noti þá. Margir aðrir framleiðendur (þar á meðal OPT og Able í sumum gerðum) nota líka kerfi byggð á DT.

Phenix Technology (PT) eru almennt í lægra gæðaflokki, en satt að segja eru þeir líklega í lagi fyrir flest.

**Ef skannarnir þínir eru ómerktir er það líklega þá sem þú þarft að hafa áhyggjur af gæðunum!**

#### Hvernig Liberation hjálpar

Í fyrsta lagi þarftu yfirleitt ekki mjög dýra skanna! DT 30kpps á viðráðanlegu verði, eða jafnvel PT, duga vel. Sjálfgefnu skannastillingarnar eru vísvitandi hóflegar og að mestu leyti _ættir þú ekki að þurfa að breyta þeim_ (fyrir utan _Scanner sync_).

Jafnvel þótt þú sért með betri skanna er engin ástæða til að keyra þá harðar en þú þarft. Það lengir endingartíma þeirra verulega.

#### Hvað er „point stream“?

Þú hefur líklega heyrt þetta hugtak áður - þetta er hvernig við stjórnum ferli skannanna.

Punktastraumur er listi yfir X/Y-staðsetningar, þar sem hver staðsetning hefur lit. Til að teikna til dæmis hvíta línu sendir þú röð punkta eftir línunni, alla stillta á hvítt. Skannarnir færa sig síðan frá punkti til punkts á föstum hraða - punktum á sekúndu (PPS) - og geislinn teiknar formið.

#### Hvernig þetta virkar í hefðbundnum laserhugbúnaði

Hefðbundinn laserhugbúnaður geymir punktastraum fyrir hvert cue. Fyrir hreyfð cue þýðir það venjulega sérstakan punktastraum fyrir hvern ramma. Aðalatriðið er að allt er algjörlega fyrirframákveðið. Þar af leiðandi lætur aukinn punktahraði skannana fara hraðar í gegnum sömu fyrirfram skilgreindu gögnin.

{% hint style="info" %}
Í eldri hugbúnaði var þessi nálgun nauðsynleg - tölvur voru einfaldlega ekki nógu hraðar til að búa til punktastrauma í rauntíma. Þess vegna er yfirleitt sérstakur cue-ritill sem er notaður til að búa gögnin fyrir hvern ramma hreyfingarinnar til fyrirfram.

Þetta útskýrir líka hvers vegna efni getur tekið gígabæti af plássi. Í raun ertu að geyma stórar, óþjappaðar bylgjulögunarskrár á frekar háum sýnatökutíðnum.
{% endhint %}

#### Af hverju „point rate“ skiptir minna máli í Liberation

Liberation býr punktastrauminn til í rauntíma, sem gefur okkur mjög mikinn sveigjanleika. Taktu eftir stillingunni "Scanner speed" í Laser Settings-spjaldinu. Hún gerir okkur kleift að hraða á og hægja á skönnunum, en mikilvægt er að hún **breytir ekki** undirliggjandi punktahraða (PPS).

#### Bíddu, hvað? Hvernig?

Ég veit, þetta hljómar undarlega í fyrstu.

Vegna þess að Liberation býr punktastrauminn til í rauntíma getur það aðlagað punktastrauminn. Því dreifðari sem punktarnir eru, þeim mun hraðar hreyfast skannarnir. Því þéttari sem þeir eru, þeim mun hægar hreyfast skannarnir.

{% hint style="info" %}
Í nýlegum útgáfum af Liberation hefur raunverulegur _point rate_ (í ítarlegum stillingum) engin áhrif á skannahraða. Í staðinn aðlagar renderer punktadreifinguna að völdum punktahraða, en heldur hreyfingu skannanna óbreyttri.

Þetta hefur vissulega áhrif á „upplausn“ punktaferilsins, en það skiptir aðallega máli fyrir grafík (og getur hjálpað við fínni stillingu á _scanner sync_).
{% endhint %}

#### Frábært! Hvað þýðir þetta þá í raun?

Góð spurning. Hér eru mín ráð:

* Forðastu ómerkta skanna. Ef þú getur fengið hraðari skanna, gerðu það - að lágmarki 30KPPS.
* Í flestum tilvikum eru DT30 skannar fínir, og PT30 skannar eru líklega í lagi í ódýrari laserum.
* Ef þú ert að vinna með grafík eru fleiri laserar í flestum tilvikum betri en hraðari skannar.
* Þegar þú ert komin(n) í hærri gæðaflokk eru öll þekktu hágæðamerkin í lagi.
* Ef þú getur aðeins fengið ódýrustu ómerktu skannana eru sjálfgefnu stillingarnar í Liberation frekar hóflegar og þú færð líklega ásættanlegar niðurstöður fyrir grunnvinnu með geisla. Ef kerfið á í erfiðleikum skaltu lækka **Speed** stillinguna (en ekki breyta punktahraðanum!).

#### Og ILDA Test Pattern?

…er enn mjög gagnlegt sem kvörðunar- og viðmiðunartæki, en það var aldrei hannað sem yfirgripsmikið frammistöðuviðmið og framleiðendur geta misnotað það eða túlkað það frjálslega.
