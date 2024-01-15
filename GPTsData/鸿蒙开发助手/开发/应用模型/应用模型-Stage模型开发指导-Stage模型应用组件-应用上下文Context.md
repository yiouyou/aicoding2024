# 应用上下文Context

更新时间: 2024-01-15 12:18

## 概述

[Context](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/js-apis-inner-application-context-0000001427744988-V3)是应用中对象的上下文，其提供了应用的一些基础信息，例如resourceManager（资源管理）、applicationInfo（当前应用信息）、dir（应用开发路径）、area（文件分区）等，以及应用的一些基本方法，例如createBundleContext()、getApplicationContext()等。UIAbility组件和各种ExtensionAbility派生类组件都有各自不同的Context类。分别有基类Context、ApplicationContext、AbilityStageContext、UIAbilityContext、ExtensionContext、ServiceExtensionContext等Context。

* 各类Context的继承关系
  ![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231121183823.69650744555189217956730374112938:50001231000000:2800:DFACD66BE423434F31418A78C8022AACC830C2DFC4CAD22B1CEEF9BD9DA7A2BC.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)
* 各类Context的持有关系
  ![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231121183823.17427505326590215569510479309825:50001231000000:2800:A91B2D987EB20AE437A16147C7194992F2DD80DDB4035104040B1753EDFA3E75.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)
* 各类Context的获取方式
  * 获取[UIAbilityContext](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/js-apis-inner-application-uiabilitycontext-0000001478341321-V3)。每个UIAbility中都包含了一个Context属性，提供操作Ability、获取Ability的配置信息、应用向用户申请授权等能力。
```
import UIAbility from '@ohos.app.ability.UIAbility';
export default class EntryAbility extends UIAbility {
    onCreate(want, launchParam) {
        let uiAbilityContext = this.context;
        // ...
    }
}
```
  * 获取[AbilityStageContext](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/js-apis-inner-application-abilitystagecontext-0000001478181577-V3)。Module级别的Context，和基类Context相比，额外提供HapModuleInfo、Configuration等信息。
```
import AbilityStage from "@ohos.app.ability.AbilityStage";
export default class MyAbilityStage extends AbilityStage {
    onCreate() {
        let abilityStageContext = this.context;
        // ...
    }
}
```
  * 获取[ApplicationContext](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/js-apis-inner-application-applicationcontext-0000001477981357-V3)。应用级别的Context。ApplicationContext在基类Context的基础上提供了订阅应用内Ability的生命周期的变化、订阅系统内存变化和订阅应用内系统环境的变化的能力，在UIAbility、ExtensionAbility、AbilityStage中均可以获取。
```
import UIAbility from '@ohos.app.ability.UIAbility';
export default class EntryAbility extends UIAbility {
    onCreate(want, launchParam) {
        let applicationContext = this.context.getApplicationContext();
        // ...
    }
}
```

## Context的典型使用场景

本章节通过如下典型场景来介绍Context的用法：

* [获取应用文件路径](https://developer.harmonyos.com/cn/docs/documentation/doc-guides-V3/application-context-stage-0000001427744560-V3#ZH-CN_TOPIC_0000001574128741__%E8%8E%B7%E5%8F%96%E5%BA%94%E7%94%A8%E5%BC%80%E5%8F%91%E8%B7%AF%E5%BE%84)
* [获取和修改加密分区](https://developer.harmonyos.com/cn/docs/documentation/doc-guides-V3/application-context-stage-0000001427744560-V3#ZH-CN_TOPIC_0000001574128741__%E8%8E%B7%E5%8F%96%E5%92%8C%E4%BF%AE%E6%94%B9%E5%8A%A0%E5%AF%86%E5%88%86%E5%8C%BA)
* [创建其他应用或其他Module的Context](https://developer.harmonyos.com/cn/docs/documentation/doc-guides-V3/application-context-stage-0000001427744560-V3#ZH-CN_TOPIC_0000001574128741__%E5%88%9B%E5%BB%BA%E5%85%B6%E4%BB%96%E5%BA%94%E7%94%A8%E6%88%96%E5%85%B6%E4%BB%96module%E7%9A%84context)
* [订阅进程内Ability生命周期变化](https://developer.harmonyos.com/cn/docs/documentation/doc-guides-V3/application-context-stage-0000001427744560-V3#ZH-CN_TOPIC_0000001574128741__%E8%AE%A2%E9%98%85%E8%BF%9B%E7%A8%8B%E5%86%85ability%E7%94%9F%E5%91%BD%E5%91%A8%E6%9C%9F%E5%8F%98%E5%8C%96)

### 获取应用文件路径

基类[Context](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/js-apis-inner-app-context-0000001478181573-V3)提供了获取应用文件路径的能力，ApplicationContext、AbilityStageContext、UIAbilityContext和ExtensionContext均继承该能力。应用文件路径属于应用沙箱路径，具体请参见[应用沙箱目录](https://developer.harmonyos.com/cn/docs/documentation/doc-guides-V3/app-sandbox-directory-0000001491863498-V3)。

上述各类Context获取的应用文件路径有所不同。

* 通过ApplicationContext获取应用级别的应用文件路径，此路径是应用全局信息推荐的存放路径，这些文件会跟随应用的卸载而删除。| 属性                | 路径                                    |
  | :------------------ | :-------------------------------------- |
  | bundleCodeDir       | <路径前缀>/el1/bundle/                  |
  | cacheDir            | <路径前缀>/<加密等级>/base/cache/       |
  | filesDir            | <路径前缀>/<加密等级>/base/files/       |
  | preferencesDir      | <路径前缀>/<加密等级>/base/preferences/ |
  | tempDir             | <路径前缀>/<加密等级>/base/temp/        |
  | databaseDir         | <路径前缀>/<加密等级>/database/         |
  | distributedFilesDir | <路径前缀>/el2/distributedFiles/        |
* 通过AbilityStageContext、UIAbilityContext、ExtensionContext获取HAP级别的应用文件路径。此路径是HAP相关信息推荐的存放路径，这些文件会跟随HAP的卸载而删除，但不会影响应用级别路径的文件，除非该应用的HAP已全部卸载。| 属性                | 路径                                                           |
  | :------------------ | :------------------------------------------------------------- |
  | bundleCodeDir       | <路径前缀>/el1/bundle/                                         |
  | cacheDir            | <路径前缀>/<加密等级>/base/haps/`<module-name>`/cache/       |
  | filesDir            | <路径前缀>/<加密等级>/base/haps/`<module-name>`/files/       |
  | preferencesDir      | <路径前缀>/<加密等级>/base/haps/`<module-name>`/preferences/ |
  | tempDir             | <路径前缀>/<加密等级>/base/haps/`<module-name>`/temp/        |
  | databaseDir         | <路径前缀>/<加密等级>/database/`<module-name>`/              |
  | distributedFilesDir | <路径前缀>/el2/distributedFiles/`<module-name>`/             |

示例代码如下。

```
import UIAbility from '@ohos.app.ability.UIAbility';

export default class EntryAbility extends UIAbility {
    onCreate(want, launchParam) {
        let cacheDir = this.context.cacheDir;
        let tempDir = this.context.tempDir;
        let filesDir = this.context.filesDir;
        let databaseDir = this.context.databaseDir;
        let bundleCodeDir = this.context.bundleCodeDir;
        let distributedFilesDir = this.context.distributedFilesDir;
        let preferencesDir = this.context.preferencesDir;
        // ...
    }
}
```

### 获取和修改加密分区

上一个场景中，引入了加密等级的概念，通过对[Context的area属性](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/js-apis-inner-application-context-0000001427744988-V3)的读写来实现获取和设置当前加密分区，支持如下两种加密等级：

* AreaMode.EL1：设备级加密区，设备开机后可访问的数据区。
* AreaMode.EL2：用户级加密区，设备开机，首次输入密码后才能够访问的数据区。

```
import UIAbility from '@ohos.app.ability.UIAbility';

export default class EntryAbility extends UIAbility {
    onCreate(want, launchParam) {
        // 存储普通信息前，切换到EL1设备级加密
        if (this.context.area === 1) { // 获取area
            this.context.area = 0;     // 修改area
        }
        // 存储普通信息

        // 存储敏感信息前，切换到EL2用户级加密
        if (this.context.area === 0) { // 获取area
            this.context.area = 1;     // 修改area
        }
        // 存储敏感信息
    }
}
```

### 创建其他应用或其他Module的Context

基类Context提供创建其他应用或其他Module的Context的方法为[createModuleContext(moduleName:string)](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/js-apis-inner-application-context-0000001427744988-V3#ZH-CN_TOPIC_0000001523648906__contextcreatemodulecontext)，创建其他应用或者其他Module的Context，从而通过该Context获取相应的资源信息（例如获取其他Module的[获取应用开发路径](https://developer.harmonyos.com/cn/docs/documentation/doc-guides-V3/application-context-stage-0000001427744560-V3#ZH-CN_TOPIC_0000001574128741__%E8%8E%B7%E5%8F%96%E5%BA%94%E7%94%A8%E5%BC%80%E5%8F%91%E8%B7%AF%E5%BE%84)信息）。

调用createModuleContext(moduleName:string)方法，获取本应用中其他Module的Context。获取到其他Module的Context之后，即可获取到相应Module的资源信息。

```
import UIAbility from '@ohos.app.ability.UIAbility';

export default class EntryAbility extends UIAbility {
    onCreate(want, launchParam) {
        let moduleName2 = "module1";
        let context2 = this.context.createModuleContext(moduleName2);
        // ...
    }
}
```

### 订阅进程内Ability生命周期变化

在应用内的DFX统计场景，如需要统计对应页面停留时间和访问频率等信息，可以使用订阅进程内Ability生命周期变化功能。

在进程内Ability生命周期变化时，如创建、可见/不可见、获焦/失焦、销毁等，会触发进入相应的回调，其中返回的此次注册监听生命周期的ID（每次注册该ID会自增+1，当超过监听上限数量2^63-1时，返回-1），以在[UIAbilityContext](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/js-apis-inner-application-uiabilitycontext-0000001478341321-V3)中使用为例进行说明。

```
import UIAbility from '@ohos.app.ability.UIAbility';
import Window from '@ohos.window';

const TAG: string = "[Example].[Entry].[EntryAbility]";

export default class EntryAbility extends UIAbility {
    lifecycleId: number;

    onCreate(want, launchParam) {
        let abilityLifecycleCallback = {
            onAbilityCreate(ability) {
                console.info(TAG, "onAbilityCreate ability:" + JSON.stringify(ability));
            },
            onWindowStageCreate(ability, windowStage) {
                console.info(TAG, "onWindowStageCreate ability:" + JSON.stringify(ability));
                console.info(TAG, "onWindowStageCreate windowStage:" + JSON.stringify(windowStage));
            },
            onWindowStageActive(ability, windowStage) {
                console.info(TAG, "onWindowStageActive ability:" + JSON.stringify(ability));
                console.info(TAG, "onWindowStageActive windowStage:" + JSON.stringify(windowStage));
            },
            onWindowStageInactive(ability, windowStage) {
                console.info(TAG, "onWindowStageInactive ability:" + JSON.stringify(ability));
                console.info(TAG, "onWindowStageInactive windowStage:" + JSON.stringify(windowStage));
            },
            onWindowStageDestroy(ability, windowStage) {
                console.info(TAG, "onWindowStageDestroy ability:" + JSON.stringify(ability));
                console.info(TAG, "onWindowStageDestroy windowStage:" + JSON.stringify(windowStage));
            },
            onAbilityDestroy(ability) {
                console.info(TAG, "onAbilityDestroy ability:" + JSON.stringify(ability));
            },
            onAbilityForeground(ability) {
                console.info(TAG, "onAbilityForeground ability:" + JSON.stringify(ability));
            },
            onAbilityBackground(ability) {
                console.info(TAG, "onAbilityBackground ability:" + JSON.stringify(ability));
            },
            onAbilityContinue(ability) {
                console.info(TAG, "onAbilityContinue ability:" + JSON.stringify(ability));
            }
        }
        // 1. 通过context属性获取applicationContext
        let applicationContext = this.context.getApplicationContext();
        // 2. 通过applicationContext注册监听应用内生命周期
        this.lifecycleId = applicationContext.on("abilityLifecycle", abilityLifecycleCallback);
        console.info(TAG, "register callback number: " + JSON.stringify(this.lifecycleId));
    }

    onDestroy() {
        let applicationContext = this.context.getApplicationContext();
        applicationContext.off("abilityLifecycle", this.lifecycleId, (error, data) => {
            console.info(TAG, "unregister callback success, err: " + JSON.stringify(error));
        });
    }
}
```

