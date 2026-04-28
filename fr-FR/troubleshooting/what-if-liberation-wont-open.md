---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/troubleshooting/what-if-liberation-wont-open
---

# ✅ Que faire si Liberation ne s’ouvre pas ?

C’est rare, mais il peut arriver que Liberation ne se lance pas, ou qu’il plante juste après son ouverture. Cela vient presque toujours d’un fichier de configuration local corrompu, généralement après un plantage du système ou un événement inattendu sur votre ordinateur.

Heureusement, le problème se corrige facilement en réinitialisant vos paramètres locaux. Voici comment procéder sur macOS et Windows.

> **Important**
>
> * Fermez Liberation avant toute manipulation.
> * Ces étapes n’affectent que les paramètres locaux, les journaux et les caches. Votre licence et votre compte ne sont pas concernés.

***

#### Où trouver le dossier de travail

Chaque version de Liberation possède son propre dossier de travail. Par exemple, si vous utilisez la version 1.0.0, le dossier s’appellera 1.0.0.

* **macOS** : `~/Library/Application Support/Liberation/1.0.0`
* **Windows** : `AppData\Local\Liberation\1.0.0`

**Comment ouvrir rapidement le dossier**

**macOS**

1. Dans Finder, appuyez sur **Shift + Cmd + G**.
2.  Collez ce chemin, puis appuyez sur **Enter** :

    ```
    ~/Library/Application Support/Liberation
    ```
3. Ouvrez le dossier correspondant à votre numéro de version, par exemple `1.0.0`.

**Windows**

1.  Appuyez sur **Win + R**, collez ceci, puis appuyez sur **Enter** :

    ```
    %LOCALAPPDATA%\Liberation
    ```
2. Ouvrez le dossier correspondant à votre numéro de version, par exemple `1.0.0`.

> **Astuce pour Windows** : si vous parcourez les dossiers avec File Explorer, activez les éléments masqués : **View > Show > Hidden items**.

***

#### Étape 1 – Réinitialiser votre fichier de paramètres en toute sécurité

Dans le dossier de votre version, ouvrez :

```
data/liberation/
```

Dans le dossier liberation, vous devriez trouver un fichier appelé se`ttings.json`. Supprimez ce fichier.

* **Exemple macOS** : `~/Library/Application Support/Liberation/1.0.0/data/liberation/settings.json`
* **Exemple Windows** : `%LOCALAPPDATA%\Liberation\1.0.0\data\liberation\settings.json`

Essayez maintenant de lancer Liberation. S’il s’ouvre, c’est terminé.

***

#### Étape 2 – Vérifier s’il y a un clip problématique

Si Liberation a planté pendant que vous modifiiez un clip, il est possible qu’un élément de ce fichier de clip soit à l’origine du problème.

Dans le même dossier que votre fichier settings.json, vous devriez trouver un fichier appelé clipEdit`.json`

Sauvegardez ce fichier dans un emplacement sûr (par exemple sur votre Desktop), puis supprimez-le du dossier de travail de Liberation.

Essayez de relancer Liberation. S’il s’ouvre maintenant normalement, veuillez envoyer le fichier sauvegardé par e-mail à [**info@liberationlaser.com**](mailto:info@liberationlaser.com) afin que nous puissions rechercher la cause du problème.

***

#### Étape 3 - Sauvegarder, puis supprimer tout le dossier de travail

Si l’étape 1 et l’étape 2 n’ont pas résolu le problème :

1. **Sauvegardez** tout le dossier de version :
   * macOS : faites un clic droit sur le dossier `1.0.0` et choisissez **Compress** pour créer un fichier zip, ou copiez-le dans un emplacement sûr comme le Desktop.
   * Windows : faites un clic droit sur le dossier `1.0.0` et choisissez **Send to > Compressed (zipped) folder**, ou copiez-le dans un emplacement sûr comme le Desktop.
2. Après la sauvegarde, **supprimez** le dossier `1.0.0` d’origine depuis l’emplacement de travail de Liberation.
3. Relancez Liberation. Il recréera un nouveau dossier de travail propre.

Si Liberation s’ouvre maintenant, passez à l’étape 4.

***

#### Étape 4 - Nous envoyer la sauvegarde

Cela nous aide à identifier la cause du problème afin de pouvoir l’éviter dans les prochaines versions.

Compressez votre **sauvegarde** de l’étape 3 si ce n’est pas déjà fait, puis envoyez-la-nous par e-mail pour que nous puissions diagnostiquer la cause.

* **À** : [info@liberationlaser.com](mailto:info@liberationlaser.com)
* **Objet** : Correction du démarrage de Liberation - sauvegarde du dossier de travail
* **Message** : veuillez inclure :
  * Système d’exploitation et version (par exemple macOS 14.6 ou Windows 11 23H2)
  * Version de Liberation (par exemple 1.0.0)
  * L’étape qui a résolu le problème, le cas échéant (étape 1, étape 2 ou étape 3)
  * Une brève description de ce qui s’est passé avant l’apparition du problème
* **Pièce jointe** : la sauvegarde compressée de votre dossier de travail `1.0.0`.

> Si le fichier zip est trop volumineux pour un e-mail, téléversez-le sur un service de stockage cloud et partagez un lien.

***

#### Liberation ne se lance toujours pas après l’étape 3 ?

Si Liberation ne s’ouvre toujours pas après la suppression du dossier de travail :

* Redémarrez votre ordinateur et réessayez.
* Désactivez temporairement les antivirus ou outils de sécurité susceptibles de bloquer la création de nouveaux dossiers, puis essayez de lancer Liberation.
* Réinstallez la dernière build de Liberation par-dessus votre installation existante.
* Si aucune de ces solutions ne fonctionne, contactez le support à l’adresse [**info@liberationlaser.com**](mailto:info@liberationlaser.com) avec les détails du problème et les éventuels journaux de plantage du sous-dossier `logs`, s’il existe.

***

#### Résumé

1. Supprimez `data/liberation/settings.json` dans le dossier de travail correspondant à votre version.
2. Si vous étiez en train de modifier un clip, sauvegardez puis supprimez `data/liberation/clipEdit.json`.
3. S’il ne s’ouvre toujours pas, sauvegardez puis supprimez tout le dossier `1.0.0` (ou celui de votre version).
4. Si l’étape 3 résout le problème (ou même si ce n’est pas le cas), compressez la sauvegarde et envoyez-la à [**info@liberationlaser.com**](mailto:info@liberationlaser.com) avec votre système d’exploitation et votre version de Liberation.
