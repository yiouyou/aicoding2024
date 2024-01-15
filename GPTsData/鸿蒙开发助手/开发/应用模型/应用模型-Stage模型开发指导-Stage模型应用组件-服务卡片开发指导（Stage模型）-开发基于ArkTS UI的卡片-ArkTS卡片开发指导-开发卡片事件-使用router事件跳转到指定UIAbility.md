# 使用router事件跳转到指定UIAbility

更新时间: 2024-01-15 12:23

在卡片中使用postCardAction接口的router能力，能够快速拉起卡片提供方应用的指定UIAbility，因此UIAbility较多的应用往往会通过卡片提供不同的跳转按钮，实现一键直达的效果。例如相机卡片，卡片上提供拍照、录像等按钮，点击不同按钮将拉起相机应用的不同UIAbility，从而提升用户的体验。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231121183819.03602813329588850411386644697169:50001231000000:2800:7E22361997E98ECA714C32DDE78D54756A5EB4B351225F398F48C3A276F003CC.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)

通常使用按钮控件来实现页面拉起，示例代码如下：

* 在卡片页面中布局两个按钮，点击其中一个按钮时调用postCardAction向指定UIAbility发送router事件，并在事件内定义需要传递的内容。
```
@Entry
@Component
struct WidgetCard {
  build() {
    Column() {
      Button('功能A')
        .margin('20%')
        .onClick(() => {
          console.info('Jump to EntryAbility funA');
          postCardAction(this, {
            'action': 'router',
            'abilityName': 'EntryAbility', // 只能跳转到当前应用下的UIAbility
            'params': {
              'targetPage': 'funA' // 在EntryAbility中处理这个信息
            }
          });
        })

      Button('功能B')
        .margin('20%')
        .onClick(() => {
          console.info('Jump to EntryAbility funB');
          postCardAction(this, {
            'action': 'router',
            'abilityName': 'EntryAbility', // 只能跳转到当前应用下的UIAbility
            'params': {
              'targetPage': 'funB' // 在EntryAbility中处理这个信息
            }
          });
        })
    }
    .width('100%')
    .height('100%')
  }
}
```
* 在UIAbility中接收router事件并获取参数，根据传递的params不同，选择拉起不同的页面。
```
import UIAbility from '@ohos.app.ability.UIAbility';
import window from '@ohos.window';

let selectPage = "";
let currentWindowStage = null;

export default class CameraAbility extends UIAbility {
  // 如果UIAbility第一次启动，在收到Router事件后会触发onCreate生命周期回调
  onCreate(want, launchParam) {
    // 获取router事件中传递的targetPage参数
    console.info("onCreate want:" + JSON.stringify(want));
    if (want.parameters.params !== undefined) {
      let params = JSON.parse(want.parameters.params);
      console.info("onCreate router targetPage:" + params.targetPage);
      selectPage = params.targetPage;
    }
  }
  // 如果UIAbility已在后台运行，在收到Router事件后会触发onNewWant生命周期回调
  onNewWant(want, launchParam) {
    console.info("onNewWant want:" + JSON.stringify(want));
    if (want.parameters.params !== undefined) {
      let params = JSON.parse(want.parameters.params);
      console.info("onNewWant router targetPage:" + params.targetPage);
      selectPage = params.targetPage;
    }
    if (currentWindowStage != null) {
      this.onWindowStageCreate(currentWindowStage);
    }
  }

  onWindowStageCreate(windowStage: window.WindowStage) {
    let targetPage;
    // 根据传递的targetPage不同，选择拉起不同的页面
    switch (selectPage) {
      case 'funA':
        targetPage = 'pages/FunA';
        break;
      case 'funB':
        targetPage = 'pages/FunB';
        break;
      default:
        targetPage = 'pages/Index';
    }
    if (currentWindowStage === null) {
      currentWindowStage = windowStage;
    }
    windowStage.loadContent(targetPage, (err, data) => {
      if (err && err.code) {
        console.info('Failed to load the content. Cause: %{public}s', JSON.stringify(err));
        return;
      }
    });
  }
};
```

