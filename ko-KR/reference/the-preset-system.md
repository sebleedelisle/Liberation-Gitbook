---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/reference/the-preset-system
---

# ✅ Preset 시스템

Preset 시스템은 Liberation의 여러 위치에서 사용되며, _presets_ 목록에서 선택할 수 있는 여러 설정을 저장해야 할 때 사용됩니다.

현재 이 시스템은 다음 항목에 사용됩니다.

* Scanner 설정
* Colour calibration 설정
* 3D visualiser 카메라 설정
* 3D visualiser 레이저 설정
* DMX 프로필

예를 들어 새 CT6210 스캐너에 맞춰 Scanner 설정을 조정했다면, 이를 preset으로 저장하고 "CT6210"이라고 이름을 지정할 수 있습니다. 그러면 이후 필요할 때 preset 목록과 드롭다운 메뉴에서 해당 설정을 사용할 수 있습니다.

모든 preset은 사용 여부와 관계없이 프로젝트(또는 레이저 설정)와 함께 저장됩니다. 따라서 이러한 파일을 불러올 때마다 파일 안의 모든 preset이 기존 preset에 추가됩니다. 불러온 preset 중 기존 preset과 이름이 같은 것이 있으면 기존 preset을 덮어씁니다.

preset 드롭다운 목록 옆의 load/save 버튼(플로피 디스크 아이콘)을 사용해 preset 파일을 가져오거나 내보낼 수도 있습니다. 이 버튼을 클릭하면 import/export 버튼이 있는 팝업이 열리며, 하나 이상의 preset을 삭제하는 옵션도 제공됩니다.

<figure><img src="../.gitbook/assets/scanner-settings-presets.png" alt=""><figcaption><p>load/save 아이콘을 클릭하면 열리는 팝업 메뉴</p></figcaption></figure>

예를 들어 _Default_ 라는 Scanner 설정 preset을 편집해도, 다른 레이저가 자동으로 업데이트되지는 않습니다. 대신 각 레이저의 Scanner 설정 라벨이 _Default(edited)_ 로 표시됩니다. 이를 새 _Default_ preset으로 업데이트하려면 드롭다운 목록에서 다시 선택하세요.

{% hint style="info" %}
레이저가 많고 모든 Scanner 설정을 업데이트하려면 _COPY LASER SETTINGS_ 시스템을 사용하세요. [레이저 간 설정 복사](../setting-up/copy-laser-settings.md)를 참고하세요.
{% endhint %}

다른 곳에서 사용 중인 preset을 삭제해도 해당 설정이 사라지지는 않습니다. 대신 _(deleted)._ 로 표시됩니다.
