---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/graphics-and-the-canvas-system/canvas-overview
---

# 🟩 Přehled Canvas

Systém Canvas v Liberation je poměrně jednoduchý, ale zpočátku může působit matoucím dojmem. Tady je základní koncepční přehled, který vám pomůže začít.

{% hint style="info" %}
**Počkat, potřebuji systém Canvas?**

Možná ne! Pokud jen promítáte jednu grafiku na jeden laser, snadno to uděláte pomocí beam zone (ve výchozím nastavení je ale obsah beam zone převrácený vodorovně, takže u daného Clip budete muset použít X flip).

Pokud ale chcete grafický obsah rozdělit mezi více laserů nebo ho rozdělit do různých částí pro mapování na architekturu, systém Canvas je přesně k tomu určený.
{% endhint %}

### Canvas

Nejdřív je tu samotný Canvas. To je to, co vidíte v zobrazení _CANVAS_. Představuje velkou plochu — zkrátka canvas — a obsah můžete kreslit kamkoli do tohoto prostoru.

### Cílové oblasti Canvas

V zobrazení Canvas se zobrazují jako modré obrysové obdélníky. Jsou to oblasti, do kterých můžete posílat obsah. Obsah Clip pošlete do cílové oblasti Canvas podobně, jako byste Clip poslali do beam zone. Tlačítka cílových oblastí Canvas najdete v Clip Deck vpravo od tlačítek beam zone.

{% hint style="info" %}
Pokud v Clip Deck nevidíte tlačítka Canvas, zkuste posunout tlačítka beam zone pomocí `Shift + Left / Right Arrow`. Měli byste vidět tlačítko pro každou cílovou oblast Canvas označené _CANVAS 1, CANVAS 2_ atd.
{% endhint %}

### Canvas zones

Canvas zones jsou oblasti uvnitř Canvas, které se rozhodnete poslat do laseru. V zobrazení Canvas jsou znázorněné růžovými obrysovými obdélníky. Na každou zone můžete kliknout pravým tlačítkem a vybrat lasery, ke kterým má být přiřazena. Pokud se teď přepnete do zobrazení _OUTPUT_ pro daný laser, uvidíte, že se objevila nová zone.

{% hint style="danger" %}
VAROVÁNÍ – pokud je laser armed, mohl by náhle začít promítat obsah ve výchozí canvas zone. Před přiřazováním Canvas zones k laseru je nejlepší laser disarm.
{% endhint %}

{% hint style="info" %}
Canvas zone můžete k laseru přiřadit také kliknutím na tlačítko _add canvas zone_ v zobrazení _OUTPUT_. Viz [Zones](../output-view/zones.md "mention").
{% endhint %}

### Pomocné obrázky

Do Canvas můžete přidat pomocný obrázek a použít ho jako šablonu pro grafiku. Doporučuje se upravit barevné tónování pomocného obrázku (nabídka po kliknutí pravým tlačítkem) a ztmavit ho, abyste přes něj obsah lépe viděli.

{% hint style="info" %}
Při architektonickém mapování se mi osvědčilo připravit „rozbalený“ vizuál budovy, který všechny její povrchy znázorňuje jako plochý nezkreslený obrázek. Korekci perspektivy pro jednotlivé části pak můžete provést pomocí canvas zone v zobrazení _OUTPUT_.
{% endhint %}

<figure><img src="../.gitbook/assets/SaltwellHallFlat2.jpg" alt=""><figcaption><p>„Zploštělý“ pomocný obrázek pro Saltwell Hall v Gateshead ve Velké Británii</p></figcaption></figure>

<figure><img src="../.gitbook/assets/SaltwellHallZones.png" alt=""><figcaption><p>Canvas zones v rané verzi Liberation (cca 2017!) Všimněte si, že růžové obdélníky určují, která část Canvas se má zobrazit, a zobrazení Output dole pak ukazují, do které části jednotlivých laserů tyto zones směřují.</p></figcaption></figure>

### Canvas ve 3D vizualizéru

Znovu vytvářet složitý projekční systém s více lasery ve 3D vizualizéru by pravděpodobně bylo dost pracné (mírně řečeno). Místo toho máte možnost umístit Canvas přímo do 3D prostoru. Aktivujte zaškrtávací políčko _Show canvas_ v panelu _3D visualiser settings_. (Všechny pomocné obrázky, které máte v Canvas, se ve vizualizéru zobrazí také.)

{% hint style="info" %}
Všimněte si, že vizualizér bude projekce Canvas stále zobrazovat jako atmosférické efekty vycházející z laserů. Můžete je buď jednoduše posunout mimo záběr, nebo — pokud si chcete vyhrát — je zarovnat s Canvas.
{% endhint %}

<figure><img src="../.gitbook/assets/Screenshot 2025-01-17 at 10.36.49.png" alt=""><figcaption><p>Když ve 3D vizualizéru zarovnáte paprsky z laseru s obrázkem Canvas, může to být mimořádně uspokojivé!</p></figcaption></figure>
