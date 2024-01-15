# UIAbility组件间交互（设备内）

更新时间: 2024-01-15 12:19

UIAbility是系统调度的最小单元。在设备内的功能模块之间跳转时，会涉及到启动特定的UIAbility，该UIAbility可以是应用内的其他UIAbility，也可以是其他应用的UIAbility（例如启动三方支付UIAbility）。

本章节将从如下场景分别介绍设备内UIAbility间的交互方式。

* [启动应用内的UIAbility](https://developer.harmonyos.com/cn/docs/documentation/doc-guides-V3/uiability-intra-device-interaction-0000001478181149-V3#ZH-CN_TOPIC_0000001574248797__%E5%90%AF%E5%8A%A8%E5%BA%94%E7%94%A8%E5%86%85%E7%9A%84uiability)
* [启动应用内的UIAbility并获取返回结果](https://developer.harmonyos.com/cn/docs/documentation/doc-guides-V3/uiability-intra-device-interaction-0000001478181149-V3#ZH-CN_TOPIC_0000001574248797__%E5%90%AF%E5%8A%A8%E5%BA%94%E7%94%A8%E5%86%85%E7%9A%84uiability%E5%B9%B6%E8%8E%B7%E5%8F%96%E8%BF%94%E5%9B%9E%E7%BB%93%E6%9E%9C)
* [启动其他应用的UIAbility](https://developer.harmonyos.com/cn/docs/documentation/doc-guides-V3/uiability-intra-device-interaction-0000001478181149-V3#ZH-CN_TOPIC_0000001574248797__%E5%90%AF%E5%8A%A8%E5%85%B6%E4%BB%96%E5%BA%94%E7%94%A8%E7%9A%84uiability)
* [启动其他应用的UIAbility并获取返回结果](https://developer.harmonyos.com/cn/docs/documentation/doc-guides-V3/uiability-intra-device-interaction-0000001478181149-V3#ZH-CN_TOPIC_0000001574248797__%E5%90%AF%E5%8A%A8%E5%85%B6%E4%BB%96%E5%BA%94%E7%94%A8%E7%9A%84uiability%E5%B9%B6%E8%8E%B7%E5%8F%96%E8%BF%94%E5%9B%9E%E7%BB%93%E6%9E%9C)
* [启动UIAbility的指定页面](https://developer.harmonyos.com/cn/docs/documentation/doc-guides-V3/uiability-intra-device-interaction-0000001478181149-V3#ZH-CN_TOPIC_0000001574248797__%E5%90%AF%E5%8A%A8uiability%E7%9A%84%E6%8C%87%E5%AE%9A%E9%A1%B5%E9%9D%A2)
* [通过Call调用实现UIAbility交互（仅对系统应用开放）](https://developer.harmonyos.com/cn/docs/documentation/doc-guides-V3/uiability-intra-device-interaction-0000001478181149-V3#ZH-CN_TOPIC_0000001574248797__%E9%80%9A%E8%BF%87call%E8%B0%83%E7%94%A8%E5%AE%9E%E7%8E%B0uiability%E4%BA%A4%E4%BA%92%E4%BB%85%E5%AF%B9%E7%B3%BB%E7%BB%9F%E5%BA%94%E7%94%A8%E5%BC%80%E6%94%BE)

## 启动应用内的UIAbility

当一个应用内包含多个UIAbility时，存在应用内启动UIAbility的场景。例如在支付应用中从入口UIAbility启动收付款UIAbility。

假设应用中有两个UIAbility：EntryAbility和FuncAbility（可以在同一个Module中，也可以在不同的Module中），需要从EntryAbility的页面中启动FuncAbility。

1. 在EntryAbility中，通过调用startAbility()方法启动UIAbility，[want](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/js-apis-app-ability-want-0000001493584192-V3)为UIAbility实例启动的入口参数，其中bundleName为待启动应用的Bundle名称，abilityName为待启动的UIAbility名称，moduleName在待启动的UIAbility属于不同的Module时添加，parameters为自定义信息参数。示例中的context的获取方式参见[获取UIAbility的Context属性](https://developer.harmonyos.com/cn/docs/documentation/doc-guides-V3/uiability-usage-0000001427584600-V3#ZH-CN_TOPIC_0000001574088337__%E8%8E%B7%E5%8F%96uiability%E7%9A%84%E4%B8%8A%E4%B8%8B%E6%96%87%E4%BF%A1%E6%81%AF)。
```
let wantInfo = {
    deviceId: '', // deviceId为空表示本设备
    bundleName: 'com.example.myapplication',
    abilityName: 'FuncAbility',
    moduleName: 'module1', // moduleName非必选
    parameters: { // 自定义信息
        info: '来自EntryAbility Index页面',
    },
}
// context为调用方UIAbility的AbilityContext
this.context.startAbility(wantInfo).then(() => {
    // ...
}).catch((err) => {
    // ...
})
```
2. 在FuncAbility的生命周期回调文件中接收EntryAbility传递过来的参数。
```
import UIAbility from '@ohos.app.ability.UIAbility';
import Window from '@ohos.window';

export default class FuncAbility extends UIAbility {
    onCreate(want, launchParam) {
    // 接收调用方UIAbility传过来的参数
        let funcAbilityWant = want;
        let info = funcAbilityWant?.parameters?.info;
        // ...
    }
}
```
3. 在FuncAbility业务完成之后，如需要停止当前UIAbility实例，在FuncAbility中通过调用terminateSelf()方法实现。
```
// context为需要停止的UIAbility实例的AbilityContext
this.context.terminateSelf((err) => {
    // ...
});
```

## 启动应用内的UIAbility并获取返回结果

在一个EntryAbility启动另外一个FuncAbility时，希望在被启动的FuncAbility完成相关业务后，能将结果返回给调用方。例如在应用中将入口功能和帐号登录功能分别设计为两个独立的UIAbility，在帐号登录UIAbility中完成登录操作后，需要将登录的结果返回给入口UIAbility。

1. 在EntryAbility中，调用startAbilityForResult()接口启动FuncAbility，异步回调中的data用于接收FuncAbility停止自身后返回给EntryAbility的信息。示例中的context的获取方式参见[获取UIAbility的Context属性](https://developer.harmonyos.com/cn/docs/documentation/doc-guides-V3/uiability-usage-0000001427584600-V3#ZH-CN_TOPIC_0000001574088337__%E8%8E%B7%E5%8F%96uiability%E7%9A%84%E4%B8%8A%E4%B8%8B%E6%96%87%E4%BF%A1%E6%81%AF)。
```
let wantInfo = {
    deviceId: '', // deviceId为空表示本设备
    bundleName: 'com.example.myapplication',
    abilityName: 'FuncAbility',
    moduleName: 'module1', // moduleName非必选
    parameters: { // 自定义信息
        info: '来自EntryAbility Index页面',
    },
}
// context为调用方UIAbility的AbilityContext
this.context.startAbilityForResult(wantInfo).then((data) => {
    // ...
}).catch((err) => {
    // ...
})
```
2. 在FuncAbility停止自身时，需要调用terminateSelfWithResult()方法，入参abilityResult为FuncAbility需要返回给EntryAbility的信息。
```
const RESULT_CODE: number = 1001;
let abilityResult = {
    resultCode: RESULT_CODE,
    want: {
        bundleName: 'com.example.myapplication',
        abilityName: 'FuncAbility',
        moduleName: 'module1',
        parameters: {
            info: '来自FuncAbility Index页面',
        },
    },
}
// context为被调用方UIAbility的AbilityContext
this.context.terminateSelfWithResult(abilityResult, (err) => {
    // ...
});
```
3. FuncAbility停止自身后，EntryAbility通过startAbilityForResult()方法回调接收被FuncAbility返回的信息，RESULT_CODE需要与前面的数值保持一致。
```
const RESULT_CODE: number = 1001;

// ...

// context为调用方UIAbility的AbilityContext
this.context.startAbilityForResult(want).then((data) => {
    if (data?.resultCode === RESULT_CODE) {
        // 解析被调用方UIAbility返回的信息
        let info = data.want?.parameters?.info;
        // ...
    }
}).catch((err) => {
    // ...
})
```

## 启动其他应用的UIAbility

启动其他应用的UIAbility，通常用户只需要完成一个通用的操作（例如需要选择一个文档应用来查看某个文档的内容信息），推荐使用[隐式Want启动](https://developer.harmonyos.com/cn/docs/documentation/doc-guides-V3/want-overview-0000001478340877-V3#ZH-CN_TOPIC_0000001574088785__want%E7%9A%84%E7%B1%BB%E5%9E%8B)。系统会根据调用方的want参数来识别和启动匹配到的应用UIAbility。

启动UIAbility有[显式Want启动和隐式Want启动](https://developer.harmonyos.com/cn/docs/documentation/doc-guides-V3/want-overview-0000001478340877-V3)两种方式。

* 显式Want启动：启动一个确定应用的UIAbility，在want参数中需要设置该应用bundleName和abilityName，当需要拉起某个明确的UIAbility时，通常使用显式Want启动方式。
* 隐式Want启动：根据匹配条件由用户选择启动哪一个UIAbility，即不明确指出要启动哪一个UIAbility（abilityName参数未设置），在调用startAbility()方法时，其入参want中指定了一系列的[entities](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/js-apis-ability-wantconstant-0000001544583997-V3#ZH-CN_TOPIC_0000001574088649__wantconstantentity)字段（表示目标UIAbility额外的类别信息，如浏览器、视频播放器）和[actions](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/js-apis-ability-wantconstant-0000001544583997-V3#ZH-CN_TOPIC_0000001574088649__wantconstantaction)字段（表示要执行的通用操作，如查看、分享、应用详情等）等参数信息，然后由系统去分析want，并帮助找到合适的UIAbility来启动。当需要拉起其他应用的UIAbility时，开发者通常不知道用户设备中应用的安装情况，也无法确定目标应用的bundleName和abilityName，通常使用隐式Want启动方式。

本章节主要讲解如何通过隐式Want启动其他应用的UIAbility。

1. 将多个待匹配的文档应用安装到设备，在其对应UIAbility的module.json5配置文件中，配置skills的[entities](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/js-apis-ability-wantconstant-0000001544583997-V3#ZH-CN_TOPIC_0000001574088649__wantconstantentity)字段和[actions](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/js-apis-ability-wantconstant-0000001544583997-V3#ZH-CN_TOPIC_0000001574088649__wantconstantaction)字段。

```
{
  "module": {
    "abilities": [
      {
        // ...
        "skills": [
          {
            "entities": [
              // ...
              "entity.system.default"
            ],
            "actions": [
              // ...
              "ohos.want.action.viewData"
            ]
          }
        ]
      }
    ]
  }
}
```
2. 在调用方want参数中的entities和action需要被包含在待匹配UIAbility的skills配置的entities和actions中。系统匹配到符合entities和actions参数条件的UIAbility后，会弹出选择框展示匹配到的UIAbility实例列表供用户选择使用。示例中的context的获取方式参见[获取UIAbility的Context属性](https://developer.harmonyos.com/cn/docs/documentation/doc-guides-V3/uiability-usage-0000001427584600-V3#ZH-CN_TOPIC_0000001574088337__%E8%8E%B7%E5%8F%96uiability%E7%9A%84%E4%B8%8A%E4%B8%8B%E6%96%87%E4%BF%A1%E6%81%AF)。

```
let wantInfo = {
    deviceId: '', // deviceId为空表示本设备
    // 如果希望隐式仅在特定的捆绑包中进行查询，请取消下面的注释。
    // bundleName: 'com.example.myapplication',
    action: 'ohos.want.action.viewData',
    // entities可以被省略。
    entities: ['entity.system.default'],
}

// context为调用方UIAbility的AbilityContext
this.context.startAbility(wantInfo).then(() => {
    // ...
}).catch((err) => {
    // ...
})
```

   效果示意如下图所示，点击“打开PDF文档”时，会弹出选择框供用户选择。

   ![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231214113213.82728149112755932678666489387332:50001231000000:2800:23F0C45DE48B37E9D09894F75B1CB5A557A83912AF90C102F92FA21140A44C04.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)
3. 在文档应用使用完成之后，如需要停止当前UIAbility实例，通过调用terminateSelf()方法实现。

```
// context为需要停止的UIAbility实例的AbilityContext
this.context.terminateSelf((err) => {
    // ...
});
```

## 启动其他应用的UIAbility并获取返回结果

当使用隐式Want启动其他应用的UIAbility并希望获取返回结果时，调用方需要使用startAbilityForResult()方法启动目标UIAbility。例如主应用中需要启动三方支付并获取支付结果。

1. 在支付应用对应UIAbility的module.json5配置文件中，配置skills的[entities](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/js-apis-ability-wantconstant-0000001544583997-V3#ZH-CN_TOPIC_0000001574088649__wantconstantentity)字段和[actions](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/js-apis-ability-wantconstant-0000001544583997-V3#ZH-CN_TOPIC_0000001574088649__wantconstantaction)字段。
```
{
  "module": {
    "abilities": [
      {
        // ...
        "skills": [
          {
            "entities": [
              // ...
              "entity.system.default"
            ],
            "actions": [
              // ...
              "ohos.want.action.editData"
            ]
          }
        ]
      }
    ]
  }
}
```
2. 调用方使用startAbilityForResult()方法启动支付应用的UIAbility，在调用方want参数中的entities和action需要被包含在待匹配UIAbility的skills配置的entities和actions中。异步回调中的data用于后续接收支付UIAbility停止自身后返回给调用方的信息。系统匹配到符合entities和actions参数条件的UIAbility后，会弹出选择框展示匹配到的UIAbility实例列表供用户选择使用。
```
let wantInfo = {
    deviceId: '', // deviceId为空表示本设备
    // uncomment line below if wish to implicitly query only in the specific bundle.
    // bundleName: 'com.example.myapplication',
    action: 'ohos.want.action.editData',
    // entities can be omitted.
    entities: ['entity.system.default'],
}

// context为调用方UIAbility的AbilityContext
this.context.startAbilityForResult(wantInfo).then((data) => {
    // ...
}).catch((err) => {
    // ...
})
```
3. 在支付UIAbility完成支付之后，需要调用terminateSelfWithResult()方法实现停止自身，并将abilityResult参数信息返回给调用方。
```
const RESULT_CODE: number = 1001;
let abilityResult = {
    resultCode: RESULT_CODE,
    want: {
        bundleName: 'com.example.myapplication',
        abilityName: 'EntryAbility',
        moduleName: 'entry',
        parameters: {
            payResult: 'OKay',
        },
    },
}
// context为被调用方UIAbility的AbilityContext
this.context.terminateSelfWithResult(abilityResult, (err) => {
    // ...
});
```
4. 在调用方startAbilityForResult()方法回调中接收支付应用返回的信息，RESULT_CODE需要与前面terminateSelfWithResult()返回的数值保持一致。
```
const RESULT_CODE: number = 1001;

let want = {
  // Want参数信息
};

// context为调用方UIAbility的AbilityContext
this.context.startAbilityForResult(want).then((data) => {
    if (data?.resultCode === RESULT_CODE) {
        // 解析被调用方UIAbility返回的信息
        let payResult = data.want?.parameters?.payResult;
        // ...
    }
}).catch((err) => {
    // ...
})
```

## 启动UIAbility的指定页面

一个UIAbility可以对应多个页面，在不同的场景下启动该UIAbility时需要展示不同的页面，例如从一个UIAbility的页面中跳转到另外一个UIAbility时，希望启动目标UIAbility的指定页面。本文主要讲解目标UIAbility首次启动和目标UIAbility非首次启动两种启动指定页面的场景，以及在讲解启动指定页面之前会讲解到在调用方如何指定启动页面。

### 调用方UIAbility指定启动页面

调用方UIAbility启动另外一个UIAbility时，通常需要跳转到指定的页面。例如FuncAbility包含两个页面（Index对应首页，Second对应功能A页面），此时需要在传入的want参数中配置指定的页面路径信息，可以通过want中的parameters参数增加一个自定义参数传递页面跳转信息。示例中的context的获取方式参见[获取UIAbility的Context属性](https://developer.harmonyos.com/cn/docs/documentation/doc-guides-V3/uiability-usage-0000001427584600-V3#ZH-CN_TOPIC_0000001574088337__%E8%8E%B7%E5%8F%96uiability%E7%9A%84%E4%B8%8A%E4%B8%8B%E6%96%87%E4%BF%A1%E6%81%AF)。

```
let wantInfo = {
    deviceId: '', // deviceId为空表示本设备
    bundleName: 'com.example.myapplication',
    abilityName: 'FuncAbility',
    moduleName: 'module1', // moduleName非必选
    parameters: { // 自定义参数传递页面信息
        router: 'funcA',
    },
}
// context为调用方UIAbility的AbilityContext
this.context.startAbility(wantInfo).then(() => {
    // ...
}).catch((err) => {
    // ...
})
```

### 目标UIAbility首次启动

目标UIAbility首次启动时，在目标UIAbility的onWindowStageCreate()生命周期回调中，解析EntryAbility传递过来的want参数，获取到需要加载的页面信息url，传入windowStage.loadContent()方法。

```
import UIAbility from '@ohos.app.ability.UIAbility'
import Window from '@ohos.window'

export default class FuncAbility extends UIAbility {
    funcAbilityWant;

    onCreate(want, launchParam) {
        // 接收调用方UIAbility传过来的参数
        this.funcAbilityWant = want;
    }

    onWindowStageCreate(windowStage: Window.WindowStage) {
        // Main window is created, set main page for this ability
        let url = 'pages/Index';
        if (this.funcAbilityWant?.parameters?.router) {
            if (this.funcAbilityWant.parameters.router === 'funA') {
                url = 'pages/Second';
            }
        }
        windowStage.loadContent(url, (err, data) => {
            // ...
        });
    }
}
```

### 目标UIAbility非首次启动

经常还会遇到一类场景，当应用A已经启动且处于主页面时，回到桌面，打开应用B，并从应用B再次启动应用A，且需要跳转到应用A的指定页面。例如联系人应用和短信应用配合使用的场景。打开短信应用主页，回到桌面，此时短信应用处于已打开状态且当前处于短信应用的主页。再打开联系人应用主页，进入联系人用户A查看详情，点击短信图标，准备给用户A发送短信，此时会再次拉起短信应用且当前处于短信应用的发送页面。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231214113213.01540436541801536334137907607472:50001231000000:2800:3B1C53467E64E11ABD48469806A08FB90BB717FE7787D02BFBBEC15A35A67D7B.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)

针对以上场景，即当应用A的UIAbility实例已创建，并且处于该UIAbility实例对应的主页面中，此时，从应用B中需要再次启动应用A的该UIAbility，并且需要跳转到不同的页面，这种情况下要如何实现呢？

1. 在目标UIAbility中，默认加载的是Index页面。由于当前UIAbility实例之前已经创建完成，此时会进入UIAbility的onNewWant()回调中且不会进入onCreate()和onWindowStageCreate()生命周期回调，在onNewWant()回调中解析调用方传递过来的want参数，并挂在到全局变量globalThis中，以便于后续在页面中获取。
```
import UIAbility from '@ohos.app.ability.UIAbility'

export default class FuncAbility extends UIAbility {
    onNewWant(want, launchParam) {
        // 接收调用方UIAbility传过来的参数
        globalThis.funcAbilityWant = want;
        // ...
    }
}
```
2. 在FuncAbility中，此时需要在Index页面中通过页面路由Router模块实现指定页面的跳转，由于此时FuncAbility对应的Index页面是处于激活状态，不会重新变量声明以及进入aboutToAppear()生命周期回调中。因此可以在Index页面的onPageShow()生命周期回调中实现页面路由跳转的功能。
```
import router from '@ohos.router';

@Entry
@Component
struct Index {
  onPageShow() {
    let funcAbilityWant = globalThis.funcAbilityWant;
    let url2 = funcAbilityWant?.parameters?.router;
    if (url2 && url2 === 'funcA') {
      router.replaceUrl({
        url: 'pages/Second',
      })
    }
  }

  // 页面展示
  build() {
    // ...
  }
}
```

说明

当被调用方[Ability的启动模式](https://developer.harmonyos.com/cn/docs/documentation/doc-guides-V3/uiability-launch-type-0000001428061476-V3)设置为multiton启动模式时，每次启动都会创建一个新的实例，那么[onNewWant()](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/js-apis-app-ability-uiability-0000001493584184-V3#ZH-CN_TOPIC_0000001523808838__abilityonnewwant)回调就不会被用到。

## 通过Call调用实现UIAbility交互（仅对系统应用开放）

Call调用是UIAbility能力的扩展，它为UIAbility提供一种能够被外部调用并与外部进行通信的能力。Call调用支持前台与后台两种启动方式，使UIAbility既能被拉起到前台展示UI，也可以在后台被创建并运行。Call调用在调用方与被调用方间建立了IPC通信，因此应用开发者可通过Call调用实现不同UIAbility之间的数据共享。

Call调用的核心接口是startAbilityByCall方法，与startAbility接口的不同之处在于：

* startAbilityByCall支持前台与后台两种启动方式，而startAbility仅支持前台启动。
* 调用方可使用startAbilityByCall所返回的Caller对象与被调用方进行通信，而startAbility不具备通信能力。

Call调用的使用场景主要包括：

* 需要与被启动的UIAbility进行通信。
* 希望被启动的UIAbility在后台运行。
  表1 Call调用相关名词解释

| 名词          | 描述                                                                                       |
| :------------ | :----------------------------------------------------------------------------------------- |
| CallerAbility | 进行Call调用的UIAbility（调用方）。                                                        |
| CalleeAbility | 被Call调用的UIAbility（被调用方）。                                                        |
| Caller        | 实际对象，由startAbilityByCall接口返回，CallerAbility可使用Caller与CalleeAbility进行通信。 |
| Callee        | 实际对象，被CalleeAbility持有，可与Caller进行通信。                                        |

Call调用示意图如下所示。

图1 Call调用示意图

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231214113213.19909720506112455623022369162681:50001231000000:2800:D99E97AFA4A7044E5DF77084C472822BDF282EEC44B2D438E9AD60FC452CA498.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)

* CallerAbility调用startAbilityByCall接口获取Caller，并使用Caller对象的call方法向CalleeAbility发送数据。
* CalleeAbility持有一个Callee对象，通过Callee的on方法注册回调函数，当接收到Caller发送的数据时将会调用对应的回调函数。

说明

1. 当前仅支持系统应用使用Call调用。
2. CalleeAbility的启动模式需要为单实例。
3. Call调用既支持本地（设备内）Call调用，也支持跨设备Call调用，下面介绍设备内Call调用方法。

### 接口说明

Call功能主要接口如下表所示。具体的API详见[接口文档](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/js-apis-app-ability-uiability-0000001493584184-V3#ZH-CN_TOPIC_0000001523808838__caller)。

表2 Call功能主要接口

| 接口名                                                                             | 描述                                                                                                                                                                                                                                                                                                                                                           |
| :--------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| startAbilityByCall(want: Want): Promise`<Caller>`                                | 启动指定UIAbility并获取其Caller通信接口，默认为后台启动，通过配置want可实现前台启动，详见[接口文档](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/js-apis-inner-application-uiabilitycontext-0000001478341321-V3#ZH-CN_TOPIC_0000001523648914__abilitycontextstartabilitybycall)。AbilityContext与ServiceExtensionContext均支持该接口。 |
| on(method: string, callback: CalleeCallBack): void                                 | 通用组件Callee注册method对应的callback方法。                                                                                                                                                                                                                                                                                                                   |
| off(method: string): void                                                          | 通用组件Callee解注册method的callback方法。                                                                                                                                                                                                                                                                                                                     |
| call(method: string, data: rpc.Parcelable): Promise`<void>`                      | 向通用组件Callee发送约定序列化数据。                                                                                                                                                                                                                                                                                                                           |
| callWithResult(method: string, data: rpc.Parcelable): Promise<rpc.MessageSequence> | 向通用组件Callee发送约定序列化数据, 并将Callee返回的约定序列化数据带回。                                                                                                                                                                                                                                                                                       |
| release(): void                                                                    | 释放通用组件的Caller通信接口。                                                                                                                                                                                                                                                                                                                                 |
| on(type: "release", callback: OnReleaseCallback): void                             | 注册通用组件通信断开监听通知。                                                                                                                                                                                                                                                                                                                                 |

设备内通过Call调用实现UIAbility交互，涉及如下两部分开发：

* [创建Callee被调用端](https://developer.harmonyos.com/cn/docs/documentation/doc-guides-V3/uiability-intra-device-interaction-0000001478181149-V3#ZH-CN_TOPIC_0000001574248797__%E5%BC%80%E5%8F%91%E6%AD%A5%E9%AA%A4%E5%88%9B%E5%BB%BAcallee%E8%A2%AB%E8%B0%83%E7%94%A8%E7%AB%AF)
* [访问Callee被调用端](https://developer.harmonyos.com/cn/docs/documentation/doc-guides-V3/uiability-intra-device-interaction-0000001478181149-V3#ZH-CN_TOPIC_0000001574248797__%E5%BC%80%E5%8F%91%E6%AD%A5%E9%AA%A4%E8%AE%BF%E9%97%AEcallee%E8%A2%AB%E8%B0%83%E7%94%A8%E7%AB%AF)

### 开发步骤（创建Callee被调用端）

在Callee被调用端，需要实现指定方法的数据接收回调函数、数据的序列化及反序列化方法。在需要接收数据期间，通过on接口注册监听，无需接收数据时通过off接口解除监听。

1. 配置Ability的启动模式。
   配置module.json5，将CalleeAbility配置为单实例"singleton"。

   | Json字段     | 字段说明                                   |
   | :----------- | :----------------------------------------- |
   | "launchType" | Ability的启动模式，设置为"singleton"类型。 |

   Ability配置标签示例如下：


```
"abilities":[{
  "name": ".CalleeAbility",
  "srcEntrance": "./ets/CalleeAbility/CalleeAbility.ts",
  "launchType": "singleton",
  "description": "$string:CalleeAbility_desc",
  "icon": "$media:icon",
  "label": "$string:CalleeAbility_label",
  "visible": true
}]
```
2. 导入UIAbility模块。

```
import Ability from '@ohos.app.ability.UIAbility';
```
3. 定义约定的序列化数据。
   调用端及被调用端发送接收的数据格式需协商一致，如下示例约定数据由number和string组成。

```
export default class MyParcelable {
    num: number = 0
    str: string = ""

    constructor(num, string) {
        this.num = num
        this.str = string
    }

    marshalling(messageSequence) {
        messageSequence.writeInt(this.num)
        messageSequence.writeString(this.str)
        return true
    }

    unmarshalling(messageSequence) {
        this.num = messageSequence.readInt()
        this.str = messageSequence.readString()
        return true
    }
}
```
4. 实现Callee.on监听及Callee.off解除监听。
   被调用端Callee的监听函数注册时机，取决于应用开发者。注册监听之前的数据不会被处理，取消监听之后的数据不会被处理。如下示例在Ability的onCreate注册'MSG_SEND_METHOD'监听，在onDestroy取消监听，收到序列化数据后作相应处理并返回，应用开发者根据实际需要做相应处理。具体示例代码如下：

```
const TAG: string = '[CalleeAbility]';
const MSG_SEND_METHOD: string = 'CallSendMsg';

function sendMsgCallback(data) {
    console.info('CalleeSortFunc called');

    // 获取Caller发送的序列化数据
    let receivedData = new MyParcelable(0, '');
    data.readParcelable(receivedData);
    console.info(`receiveData[${receivedData.num}, ${receivedData.str}]`);

    // 作相应处理
    // 返回序列化数据result给Caller
    return new MyParcelable(receivedData.num + 1, `send ${receivedData.str} succeed`);
}

export default class CalleeAbility extends Ability {
    onCreate(want, launchParam) {
        try {
            this.callee.on(MSG_SEND_METHOD, sendMsgCallback);
        } catch (error) {
            console.info(`${MSG_SEND_METHOD} register failed with error ${JSON.stringify(error)}`);
        }
    }

    onDestroy() {
        try {
            this.callee.off(MSG_SEND_METHOD);
        } catch (error) {
            console.error(TAG, `${MSG_SEND_METHOD} unregister failed with error ${JSON.stringify(error)}`);
        }
    }
}
```

### 开发步骤（访问Callee被调用端）

1. 导入UIAbility模块。

```
import Ability from '@ohos.app.ability.UIAbility';
```

1. 获取Caller通信接口。
   Ability的context属性实现了startAbilityByCall方法，用于获取指定通用组件的Caller通信接口。如下示例通过this.context获取Ability实例的context属性，使用startAbilityByCall拉起Callee被调用端并获取Caller通信接口，注册Caller的onRelease监听。应用开发者根据实际需要做相应处理。
```
// 注册caller的release监听
private regOnRelease(caller) {
    try {
        caller.on("release", (msg) => {
            console.info(`caller onRelease is called ${msg}`);
        })
        console.info('caller register OnRelease succeed');
    } catch (error) {
        console.info(`caller register OnRelease failed with ${error}`);
    }
}

async onButtonGetCaller() {
    try {
        this.caller = await context.startAbilityByCall({
            bundleName: 'com.samples.CallApplication',
            abilityName: 'CalleeAbility'
        })
        if (this.caller === undefined) {
            console.info('get caller failed')
            return
        }
        console.info('get caller success')
        this.regOnRelease(this.caller)
    } catch (error) {
        console.info(`get caller failed with ${error}`)
    }
}
```

