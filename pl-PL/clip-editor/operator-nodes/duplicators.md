---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clip-editor/operator-nodes/duplicators
---

# 🟩 Duplicators

## <img src="../../.gitbook/assets/image (5).png" alt="" data-size="line"> Mirror

Tworzy lustrzaną kopię całej zawartości. Domyślnie oś odbicia jest pionową linią pośrodku.

* **angle** - kąt linii osi odbicia.
* **offset position** - przesuwa oś odbicia (prostopadle do osi).
* **delay** - opóźnienie czasowe odbitej zawartości. Pamiętaj, że będzie to widoczne tylko wtedy, gdy zawartość ma jakąś animację.

#### Opcje 3D (dostępne po wybraniu 3D)

* **angle X / angle Y** - oś odbicia staje się płaszczyzną, a te ustawienia pozwalają obracać ją w 3D.

## <img src="../../.gitbook/assets/image (6).png" alt="" data-size="line"> Circular Pattern

Duplikuje zawartość w układzie kołowym.

* **radius** - odległość od punktu środkowego, o jaką zawartość jest przesuwana przed obrotem.
* **count** - liczba kopii obiektu do utworzenia.
* **use each objects pivot point** - po wybraniu tej opcji każdy element zostanie przesunięty i obrócony wokół własnego punktu środkowego. (Działa tylko wtedy, gdy duplikowanych jest wiele elementów)
* **delay** - dodaje coraz większe opóźnienie czasowe do każdego zduplikowanego elementu. Aby efekt był zauważalny, zawartość musi mieć jakąś animację.
* **rotation** - dodatkowy obrót dodawany do elementów.

#### Opcje 3D (dostępne po wybraniu 3D)

* **rotation x / rotation y** - obraca cały układ kołowy wokół osi x i y.

## <img src="../../.gitbook/assets/image (7).png" alt="" data-size="line"> Grid Pattern

Duplikuje zawartość w układzie siatki złożonej z wierszy i kolumn.

* **spacing** - odległość między elementami.
* **count X**- liczba kopii w poziomie (kolumn).
* **count Y**- liczba kopii w pionie (wierszy).
* **horizontal alignment** - punkt początkowy kolumn: LEFT, CENTRE lub RIGHT.
* **vertical alignment** - punkt początkowy wierszy: TOP, MIDDLE lub BOTTOM.
* **delay** - dodaje coraz większe opóźnienie czasowe do każdego zduplikowanego elementu. Aby efekt był zauważalny, zawartość musi mieć jakąś animację.
