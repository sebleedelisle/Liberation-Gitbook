---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/appendix-articles/scanner-specifications-and-liberation
---

# 🟩 Specifikace skenerů a Liberation

### Nepřehledná realita specifikací skenerů

Bodové frekvence a specifikace skenerů mohou být trochu matoucí. Často uvidíte údaje jako 30kpps @ 8° nebo 50kpps @ 4°, ale není vždy zřejmé, co tato čísla ve skutečnosti znamenají.

{% hint style="info" %}
Upozornění – nejsem specialista na hardware skenerů, ale mám roky praktických zkušeností s tím, jak pomocí softwaru a generování bodového toku dosáhnout dobrého vzhledu u skenerů velmi různé kvality, spíše než hardwarovým laděním. Tento text vychází z těchto zkušeností.
{% endhint %}

#### **Odkud tato čísla pocházejí**

Označení jako „30K“ a „50K“ jsou zkratky vycházející z toho, jak se skenery hodnotí pomocí testovacího obrazce ILDA při daných bodových frekvencích a za konkrétních podmínek.

Když je skener uváděn například jako: _30Kpps @ 8°_, ve skutečnosti to znamená:

> „Tento skener dokáže při správném seřízení reprodukovat testovací obrazec ILDA rychlostí 30 000 bodů/s při úhlu skenování 8°.“

Není to komplexní ani plně standardizované měření výkonu v reálném provozu. Ve skutečnosti to původně ani nebylo navrženo jako benchmark – používalo se to pro **postup seřízení**. Spustíte známý obrazec s pevnou bodovou frekvencí (např. 30 000 bodů/s) a upravujete tlumení a zesílení, dokud obrazec nevypadá správně.

Stále je to ale nejpoužívanější reference, kterou máme, a může dát dobrou představu o kvalitě skenerů, alespoň u renomovaných výrobců. U těch _méně renomovaných_ ovšem...

#### Pokud chcete skenery otestovat podle jejich uváděných parametrů

{% hint style="danger" %}
**Toto je pokročilý postup a při neopatrnosti můžete skenery poškodit. Nedoporučuje se, pokud přesně nevíte, co děláte.**
{% endhint %}

Budete muset najít software, který dokáže výstupem poslat [testovací obrazec ILDA](https://ilda.com/technical.htm?r=7950) – myslím, že LaserShowGen to možná umí – a nastavit velikost výstupu tak, aby odpovídala uvedenému úhlu skenování (např. 8°). Pokyny k analýze výstupu najdete v dokumentaci ILDA.

#### Proč to nemusí být dobrý benchmark

Za prvé, testovací obrazec se může zobrazovat nesprávně, i když máte dobré skenery, protože nejsou seřízené způsobem optimalizovaným právě pro něj.

Může to být užitečné obecné vodítko pro rozlišení „dobrých“ a „špatných“ skenerů, ale výrobci někdy s těmito specifikacemi zacházejí dost volně.

#### Jak tedy vybrat dobrý skener?

Podle mě je hlavní ověřit, že je vyrábí renomovaný výrobce. Drazí výrobci špičkových skenerů, jako Cambridge Technology (CT), Eye Magic (EMS) a ScannerMAX (dceřiná společnost Pangolin), jsou vždy dobrá volba a neuděláte chybu. Jenže když pár skenerů stojí kolem 1000 dolarů, pro mnoho z nás na začátku je to víc než cena samotných laserů!

Proto jsem většinou používal čínské výrobce. Skenery Dragon Tiger (DT) jsou slušné a cenově dostupné a myslím, že je používá LightSpace. Mnoho dalších výrobců (včetně OPT a u některých modelů Able) také používá systémy založené na DT.

Phenix Technology (PT) jsou obecně nižší třída, ale upřímně řečeno budou pro většinu věcí pravděpodobně stačit.

**Pokud jsou vaše skenery neznačkové, pak je asi namístě začít se o kvalitu zajímat!**

#### Jak pomáhá Liberation

Především: pro většinu věcí opravdu nepotřebujete drahé skenery. Cenově dostupné DT 30kpps, nebo dokonce PT, budou stačit. Výchozí nastavení skenerů jsou záměrně konzervativní a ve většině případů _byste je neměli potřebovat upravovat_ (kromě _Scanner sync_).

I když máte lepší skenery, nemá smysl je zatěžovat víc, než je potřeba. Výrazně tím prodloužíte jejich životnost.

#### Co je „bodový tok“?

Tenhle pojem jste už pravděpodobně slyšeli – jde o způsob, jak ovládáme dráhu skenerů.

Bodový tok je seznam pozic X/Y, z nichž každá má přiřazenou barvu. Chcete-li vykreslit například bílou čáru, pošlete posloupnost bodů podél této čáry, všechny nastavené na bílou. Skenery se pak pohybují z bodu na bod pevnou rychlostí – bodovou frekvencí (PPS) – a paprsek vykreslí daný tvar.

#### Jak to funguje v tradičním laserovém softwaru

Tradiční laserový software ukládá bodový tok pro každou cue. U animovaných cue to obvykle znamená samostatný bodový tok pro každý snímek. Podstatné je, že všechno je kompletně předem dané. Zvýšení bodové frekvence proto způsobí, že se skenery pohybují rychleji stejnými předem připravenými daty.

{% hint style="info" %}
U staršího softwaru byl tento přístup nutný – počítače jednoduše nebyly dost rychlé na to, aby generovaly bodové toky v reálném čase. Proto obvykle existuje samostatný editor cue, který se používá k předgenerování dat pro každý snímek animace.

To také vysvětluje, proč může obsah zabírat gigabajty místa. Ve skutečnosti ukládáte velké nekomprimované průběhy s poměrně vysokými vzorkovacími frekvencemi.
{% endhint %}

#### Proč je v Liberation „point rate“ méně podstatná

Liberation generuje bodový tok v reálném čase, což nám dává obrovskou flexibilitu. Všimněte si nastavení "Scanner speed" v panelu Laser Settings. Umožňuje skenery zrychlit nebo zpomalit, ale důležité je, že **nemění** základní bodovou frekvenci (PPS).

#### Počkat, cože? Jak?

Vím, zpočátku to zní divně.

Protože Liberation generuje bodový tok v reálném čase, může tento bodový tok upravovat. Čím dál jsou body od sebe, tím rychleji se skenery pohybují. Čím blíž jsou u sebe, tím pomaleji se skenery pohybují.

{% hint style="info" %}
V novějších verzích Liberation nemá skutečná _point rate_ (v pokročilých nastaveních) na rychlost skenerů žádný vliv. Renderer místo toho upravuje rozložení bodů tak, aby odpovídalo zvolené bodové frekvenci, a zároveň zachovává stejný pohyb skenerů.

Má to vliv na „rozlišení“ bodové dráhy, ale to je podstatné hlavně u grafiky (a může pomoci s jemnějším nastavením _scanner sync_).
{% endhint %}

#### Skvělé! Co to tedy všechno vlastně znamená?

Dobrá otázka. Tady jsou moje tipy:

* Vyhněte se neznačkovým skenerům. Pokud můžete získat rychlejší skenery, udělejte to – minimum je 30KPPS.
* Ve většině případů jsou skenery DT30 v pořádku a skenery PT30 budou u levnějších laserů pravděpodobně také OK.
* Pokud děláte grafiku, ve většině případů bude lepší mít více laserů než rychlejší skenery.
* Jakmile se dostanete k vyšší třídě sestav, jakákoli zavedená špičková značka bude v pořádku.
* Pokud seženete jen nejlevnější neznačkové skenery, výchozí nastavení Liberation jsou poměrně konzervativní a pro základní práci s paprsky pravděpodobně dosáhnete přijatelných výsledků. Pokud to bude mít potíže, snižte nastavení **Speed** (ale neměňte bodovou frekvenci!).

#### A co testovací obrazec ILDA?

…je stále velmi užitečný jako kalibrační a referenční nástroj, ale nikdy nebyl navržen jako komplexní benchmark a výrobci ho mohou zneužívat nebo vykládat volně.
