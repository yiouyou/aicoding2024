# UIAbility组件基本用法

更新时间: 2024-01-15 12:18

UIAbility组件的基本用法包括：指定UIAbility的启动页面以及获取UIAbility的上下文[UIAbilityContext](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/js-apis-inner-application-uiabilitycontext-0000001478341321-V3)。

## 指定UIAbility的启动页面

应用中的UIAbility在启动过程中，需要指定启动页面，否则应用启动后会因为没有默认加载页面而导致白屏。可以在UIAbility的onWindowStageCreate()生命周期回调中，通过[WindowStage](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/js-apis-window-0000001477981397-V3#ZH-CN_TOPIC_0000001573929313__windowstage9)对象的loadContent()方法设置启动页面。

```
import UIAbility from '@ohos.app.ability.UIAbility';
import Window from '@ohos.window';

export default class EntryAbility extends UIAbility {
    onWindowStageCreate(windowStage: Window.WindowStage) {
        // Main window is created, set main page for this ability
        windowStage.loadContent('pages/Index', (err, data) => {
            // ...
        });
    }

    // ...
}
```

说明

在DevEco Studio中创建的UIAbility中，该UIAbility实例默认会加载Index页面，根据需要将Index页面路径替换为需要的页面路径即可。

## 获取UIAbility的上下文信息

UIAbility类拥有自身的上下文信息，该信息为[UIAbilityContext](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/js-apis-inner-application-uiabilitycontext-0000001478341321-V3)类的实例，[UIAbilityContext](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/js-apis-inner-application-uiabilitycontext-0000001478341321-V3)类拥有abilityInfo、currentHapModuleInfo等属性。通过UIAbilityContext可以获取UIAbility的相关配置信息，如包代码路径、Bundle名称、Ability名称和应用程序需要的环境状态等属性信息，以及可以获取操作UIAbility实例的方法（如startAbility()、connectServiceExtensionAbility()、terminateSelf()等）。

* 在UIAbility中可以通过this.context获取UIAbility实例的上下文信息。

```
import UIAbility from '@ohos.app.ability.UIAbility';

export default class EntryAbility extends UIAbility {
    onCreate(want, launchParam) {
        // 获取UIAbility实例的上下文
        let context = this.context;

        // ...
    }
}
```
* 在页面中获取UIAbility实例的上下文信息，包括导入依赖资源context模块和在组件中定义一个context变量两个部分。

```
import common from '@ohos.app.ability.common';

@Entry
@Component
struct Index {
  private context = getContext(this) as common.UIAbilityContext;

  startAbilityTest() {
    let want = {
      // Want参数信息
    };
    this.context.startAbility(want);
  }

  // 页面展示
  build() {
    // ...
  }
}
```

  也可以在导入依赖资源context模块后，在具体使用[UIAbilityContext](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/js-apis-inner-application-uiabilitycontext-0000001478341321-V3)前进行变量定义。

```
import common from '@ohos.app.ability.common';

@Entry
@Component
struct Index {

  startAbilityTest() {
    let context = getContext(this) as common.UIAbilityContext;
    let want = {
      // Want参数信息
    };
    context.startAbility(want);
  }

  // 页面展示
  build() {
    // ...
  }
}
```

