---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/advanced/colour-calibration
---

# 🟩 Kalibrace barev

Kalibrace barev zajišťuje, že červený, zelený a modrý laser v projektoru vyzařují světlo plynule a předvídatelně při všech úrovních jasu. Různé projektory mohou mít nelineární křivky jasu, takže 50 % červené může působit mnohem jasněji nebo tmavěji než poloviční intenzita 100 % červené. Kalibrace to koriguje, aby se barvy čistě míchaly, přechody vypadaly plynule a bílá byla vyvážená.

#### Zahřátí projektoru

Laserové diody mění své chování při zahřívání. Před kalibrací vždy nechte projektor stabilizovat:

* Promítejte jasný obraz, například **White rectangle test pattern (11)**, alespoň **15–20 minut**.
* Díky tomu zůstane vyvážení barev, které nastavíte, během show stabilní.

#### Jak kalibrační test funguje

Ke kalibraci použijte funkci test pattern (viz [Testovací obrazce](../output-view/test-patterns.md))

* **5** – Red
* **6** – Green
* **7** – Blue
* **8** – White

Každý z těchto obrazců zobrazuje čtyři pohybující se čáry:

* **Horní čára** – 100% jas při plné rychlosti
* **Druhá čára** – 75% jas při 75% rychlosti
* **Třetí čára** – 50% jas při 50% rychlosti
* **Čtvrtá čára** – 25% jas při 25% rychlosti

Protože se společně mění jas _i rychlost_, měly by všechny čáry vypadat stejně jasně. Pokud některá působí světleji nebo tmavěji, upravte příslušný posuvník, dokud se nesrovnají.

Každý test pattern má také pátou čáru při **0% jasu**, která by neměla být viditelná. Slouží ke korekci laserů, které při velmi nízkých úrovních nevydávají žádné světlo. Pokud laser při nízkém jasu zůstává neviditelný, postupně zvyšujte **nastavení 0 %**, dokud se čára právě neobjeví. Potom hodnotu mírně snižte, až znovu zmizí. Cílem je najít práh, při kterém laser začíná svítit, a zůstat těsně pod ním – aby stmívání začínalo přirozeně a neodřezávalo spodní rozsah.

#### Použití panelu Colour Calibration

Panel nabízí nezávislé ovládání každého kanálu (červený, zelený, modrý) na úrovních 100, 75, 50, 25 a 0 %.

1. **Vyberte test pattern** (začněte červenou).
2. **Upravte posuvníky** tak, aby čáry 100, 75, 50 a 25 % vypadaly stejně jasně.
3. **Dolaďte posuvník 0 %**, pokud je „vypnutá“ čára stále slabě viditelná.
4. **Opakujte pro zelenou a modrou.**
5. Přepněte na **White test pattern (8)**. Všechny čtyři čáry by měly vypadat stejně jasně a bílá by měla působit neutrálně (bez barevného nádechu).

#### Nastavení vyvážení bílé

Tento systém můžete použít také k nastavení **vyvážení bílé**. Po samostatné kalibraci jednotlivých kanálů přepněte na **White test pattern (8)**. Pokud má výstup barevný nádech (například je příliš do zelena nebo do modra), upravte relativní úrovně červeného, zeleného a modrého kanálu, dokud čáry nebudou působit neutrálně bíle. I když mají lasery výrazně rozdílný výkon, kalibrace je pomůže přiblížit k sobě a vytvořit čistší, vyváženější míchání barev.

#### Uložení kalibrace

* Pomocí **Store** přepište aktuální preset.
* Pomocí **Store As** vytvořte nový preset (užitečné, pokud pracujete s více lasery).
