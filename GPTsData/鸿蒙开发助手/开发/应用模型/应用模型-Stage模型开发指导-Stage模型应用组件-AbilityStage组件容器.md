# AbilityStage组件容器

更新时间: 2024-01-15 11:54

AbilityStage是一个[Module](https://developer.harmonyos.com/cn/docs/documentation/doc-guides-V3/application-package-structure-stage-0000001478061425-V3)级别的组件容器，应用的HAP在首次加载时会创建一个AbilityStage实例，可以对该Module进行初始化等操作。

AbilityStage与Module一一对应，即一个Module拥有一个AbilityStage。

DevEco Studio默认工程中未自动生成AbilityStage，如需要使用AbilityStage的能力，可以手动新建一个AbilityStage文件，具体步骤如下。

1. 在工程Module对应的ets目录下，右键选择“New > Directory”，新建一个目录并命名为myabilitystage。
2. 在myabilitystage目录，右键选择“New > TypeScript File”，新建一个TypeScript文件并命名为MyAbilityStage.ts。
3. 打开MyAbilityStage.ts文件，导入AbilityStage的依赖包，自定义类继承AbilityStage并加上需要的生命周期回调，示例中增加了一个onCreate()生命周期回调。
```
import AbilityStage from '@ohos.app.ability.AbilityStage';

export default class MyAbilityStage extends AbilityStage {
  onCreate() {
    // 应用的HAP在首次加载的时，为该Module初始化操作
  }
  onAcceptWant(want) {
    // 仅specified模式下触发
    return "MyAbilityStage";
  }
}
```
4. 在[module.json5配置文件](https://developer.harmonyos.com/cn/docs/documentation/doc-guides-V3/module-configuration-file-0000001427744540-V3)中，通过配置srcEntry参数来指定模块对应的代码路径，以作为HAP加载的入口。
```
{
  "module": {
    "name": "entry",
    "type": "entry",
    "srcEntry": "./ets/myabilitystage/MyAbilityStage.ts",
    ...
  }
}
```

[AbilityStage](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/js-apis-app-ability-abilitystage-0000001493424312-V3)拥有[onCreate()](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/js-apis-app-ability-abilitystage-0000001493424312-V3#ZH-CN_TOPIC_0000001574088265__abilitystageoncreate)生命周期回调和[onAcceptWant()](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/js-apis-app-ability-abilitystage-0000001493424312-V3#ZH-CN_TOPIC_0000001574088265__abilitystageonacceptwant)、[onConfigurationUpdated()](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/js-apis-app-ability-abilitystage-0000001493424312-V3#ZH-CN_TOPIC_0000001574088265__abilitystageonconfigurationupdate)、[onMemoryLevel()](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/js-apis-app-ability-abilitystage-0000001493424312-V3#ZH-CN_TOPIC_0000001574088265__abilitystageonmemorylevel)事件回调。

* [onCreate()](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/js-apis-app-ability-abilitystage-0000001493424312-V3#ZH-CN_TOPIC_0000001574088265__abilitystageoncreate)生命周期回调：在开始加载对应Module的第一个UIAbility实例之前会先创建AbilityStage，并在AbilityStage创建完成之后执行其onCreate()生命周期回调。AbilityStage模块提供在Module加载的时候，通知开发者，可以在此进行该Module的初始化（如资源预加载，线程创建等）能力。
* [onAcceptWant()](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/js-apis-app-ability-abilitystage-0000001493424312-V3#ZH-CN_TOPIC_0000001574088265__abilitystageonacceptwant)事件回调：UIAbility[指定实例模式（specified）](https://developer.harmonyos.com/cn/docs/documentation/doc-guides-V3/uiability-launch-type-0000001428061476-V3#ZH-CN_TOPIC_0000001523489150__specified%E5%90%AF%E5%8A%A8%E6%A8%A1%E5%BC%8F)启动时候触发的事件回调，具体使用请参见[UIAbility启动模式综述](https://developer.harmonyos.com/cn/docs/documentation/doc-guides-V3/uiability-launch-type-0000001428061476-V3)。
* [onConfigurationUpdated()](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/js-apis-app-ability-abilitystage-0000001493424312-V3#ZH-CN_TOPIC_0000001574088265__abilitystageonconfigurationupdate)事件回调：当系统全局配置发生变更时触发的事件，系统语言、深浅色等，配置项目前均定义在[Configuration](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/js-apis-app-ability-configuration-0000001493424320-V3)类中。
* [onMemoryLevel()](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/js-apis-app-ability-abilitystage-0000001493424312-V3#ZH-CN_TOPIC_0000001574088265__abilitystageonmemorylevel)事件回调：当系统调整内存时触发的事件。

应用被切换到后台时，系统会将在后台的应用保留在缓存中。即使应用处于缓存中，也会影响系统整体性能。当系统资源不足时，系统会通过多种方式从应用中回收内存，必要时会完全停止应用，从而释放内存用于执行关键任务。为了进一步保持系统内存的平衡，避免系统停止用户的应用进程，可以在AbilityStage中的onMemoryLevel()生命周期回调中订阅系统内存的变化情况，释放不必要的资源。

```
import AbilityStage from '@ohos.app.ability.AbilityStage';

export default class MyAbilityStage extends AbilityStage {
    onMemoryLevel(level) {
        // 根据系统可用内存的变化情况，释放不必要的内存
    }
}
```

