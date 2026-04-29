---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/reference/the-preset-system
---

# ✅ Le système de préréglages

Le système de préréglages est utilisé à plusieurs endroits dans Liberation lorsqu’il est nécessaire d’enregistrer plusieurs réglages sélectionnables dans une liste de _presets_.

Ce système est actuellement utilisé pour :

* Les paramètres de scanners
* Les paramètres de calibration des couleurs
* Les paramètres de caméra du 3D Visualiser
* Les paramètres laser du 3D Visualiser
* Les profils DMX

Ainsi, si vous ajustez les paramètres de scanner pour vos nouveaux scanners CT6210, vous pouvez les enregistrer comme préréglage, l’appeler « CT6210 », et il sera ensuite disponible dans la liste des préréglages chaque fois que vous en aurez besoin, ainsi que dans le menu déroulant.

Tous les préréglages sont enregistrés avec votre projet (ou vos paramètres laser), que vous les utilisiez ou non. Ainsi, chaque fois que vous chargez l’un de ces fichiers, tous les préréglages qu’il contient seront ajoutés à vos préréglages existants. Si l’un des préréglages chargés porte le même nom que l’un de vos préréglages existants, il remplacera le préréglage existant.

Vous pouvez également importer et exporter des fichiers de préréglages à l’aide du bouton load/save (une icône de disquette) situé à côté de la liste déroulante des préréglages. Cela ouvre une fenêtre contextuelle qui contient des boutons import/export, ainsi que l’option permettant de supprimer un ou plusieurs de vos préréglages.

<figure><img src="../.gitbook/assets/scanner-settings-presets.png" alt=""><figcaption><p>Le menu contextuel qui s’ouvre lorsque vous cliquez sur l’icône load/save</p></figcaption></figure>

Si vous modifiez un préréglage, par exemple le paramètre de scanner appelé _Default_, notez que les autres lasers ne seront pas mis à jour automatiquement. À la place, leurs paramètres de scanner seront désormais libellés _Default(edited)_. Pour les mettre à jour avec le nouveau préréglage _Default_, sélectionnez-le à nouveau dans la liste déroulante.

{% hint style="info" %}
Si vous avez beaucoup de lasers et que vous souhaitez mettre à jour tous leurs paramètres de scanner, utilisez le système _COPY LASER SETTINGS_. Voir [Copier les réglages entre lasers](../setting-up/copy-laser-settings.md "mention")
{% endhint %}

Si vous supprimez un préréglage utilisé ailleurs, vous ne perdrez pas le réglage : il apparaîtra simplement avec le libellé _(deleted)._
