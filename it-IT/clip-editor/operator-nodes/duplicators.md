---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clip-editor/operator-nodes/duplicators
---

# 🟩 Duplicators

## <img src="../../.gitbook/assets/image (5).png" alt="" data-size="line"> Mirror

Crea una copia speculare di tutto il contenuto. Per impostazione predefinita, l’asse dello specchio è una linea verticale al centro.

* **angle** - l’angolo della linea dell’asse dello specchio.
* **offset position** - sposta l’asse dello specchio (perpendicolarmente all’asse).
* **delay** - ritardo temporale del contenuto specchiato. Nota che avrà effetto solo se il contenuto include qualche tipo di animazione.

#### Opzioni 3D (disponibili quando è selezionato 3D)

* **angle X / angle Y** - l’asse dello specchio diventa un piano e puoi usare queste impostazioni per ruotare il piano in 3D.

## <img src="../../.gitbook/assets/image (6).png" alt="" data-size="line"> Circular Pattern

Duplica il contenuto in un pattern circolare.

* **radius** - la distanza dal punto centrale a cui il contenuto viene spostato prima della rotazione.
* **count** - il numero di copie dell’oggetto da creare.
* **use each objects pivot point** - quando è selezionato, ogni elemento viene spostato e ruotato attorno al proprio punto centrale. (Ha effetto solo quando vengono duplicati più elementi)
* **delay** - aggiunge un ritardo temporale progressivamente più lungo a ogni elemento duplicato. Nota che il contenuto deve includere qualche tipo di animazione perché l’effetto sia visibile.
* **rotation** - una rotazione di offset aggiunta agli elementi.

#### Opzioni 3D (disponibili quando è selezionato 3D)

* **rotation x / rotation y** - ruota l’intero pattern circolare attorno agli assi x e y.

## <img src="../../.gitbook/assets/image (7).png" alt="" data-size="line"> Grid Pattern

Duplica il contenuto in un pattern a griglia di righe e colonne.

* **spacing** - la distanza tra gli elementi
* **count X**- il numero di copie in orizzontale (colonne)
* **count Y**- il numero di copie in verticale (righe)
* **horizontal alignment** - il punto di partenza delle colonne, LEFT, CENTRE o RIGHT
* **vertical alignment** - il punto di partenza delle righe, TOP, MIDDLE o BOTTOM
* **delay** - aggiunge un ritardo temporale progressivamente più lungo a ogni elemento duplicato. Nota che il contenuto deve includere qualche tipo di animazione perché l’effetto sia visibile.
