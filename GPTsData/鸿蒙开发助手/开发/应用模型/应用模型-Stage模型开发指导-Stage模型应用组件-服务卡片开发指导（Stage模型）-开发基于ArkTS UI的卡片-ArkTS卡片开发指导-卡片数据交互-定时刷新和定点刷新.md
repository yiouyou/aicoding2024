# 定时刷新和定点刷新

更新时间: 2024-01-15 12:24

当前卡片框架提供了如下几种按时间刷新卡片的方式：

* 定时刷新：表示在一定时间间隔内调用[onUpdateForm](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/js-apis-app-form-formextensionability-0000001493424316-V3#ZH-CN_TOPIC_0000001573928781__onupdateform)的生命周期回调函数自动刷新卡片内容。可以在form_config.json配置文件的[updateDuration](https://developer.harmonyos.com/cn/docs/documentation/doc-guides-V3/arkts-ui-widget-configuration-0000001502333060-V3#ZH-CN_TOPIC_0000001523808634__table959386016151722)字段中进行设置。例如，可以将刷新时间设置为每小时一次。注意：updateDuration（定时刷新）优先级比scheduledUpdateTime（定点刷新）高，配置定时刷新后，定点刷新将失效。

```
{
  "forms": [
    {
      "name": "widget",
      "description": "This is a service widget.",
      "src": "./ets/widget/pages/WidgetCard.ets",
      "uiSyntax": "arkts",
      "window": {
        "designWidth": 720,
        "autoDesignWidth": true
      },
      "colorMode": "auto",
      "isDefault": true,
      "updateEnabled": true, // 使能刷新功能
      "scheduledUpdateTime": "10:30",                               
      "updateDuration": 2, // 设置卡片定时刷新的更新周期（单位为30分钟，取值为自然数）
      "defaultDimension": "2*2",
      "supportDimensions": ["2*2"]
    }
  ]
}
```
* 定点刷新：表示每天在某个时间点刷新，在form_config.json文件中配置，详见[scheduledUpdateTime](https://developer.harmonyos.com/cn/docs/documentation/doc-guides-V3/arkts-ui-widget-configuration-0000001502333060-V3#ZH-CN_TOPIC_0000001523808634__table959386016151722)字段。例如，每天在10:30更新卡片内容。

  说明

  当同时配置了定时刷新（updateDuration）和定点刷新（scheduledUpdateTime）时，定时刷新的优先级更高。如果想要配置定点刷新，则需要将updateDuration配置为0。

```
{
  "forms": [
    {
      "name": "widget",
      "description": "This is a service widget.",
      "src": "./ets/widget/pages/WidgetCard.ets",
      "uiSyntax": "arkts",
      "window": {
        "designWidth": 720,
        "autoDesignWidth": true
      },
      "colorMode": "auto",
      "isDefault": true,
      "updateEnabled": true, // 使能刷新功能
      "scheduledUpdateTime": "10:30", // 设置卡片的定点刷新的时刻
      "updateDuration": 0,
      "defaultDimension": "2*2",
      "supportDimensions": ["2*2"]
    }
  ]
}
```
* 下次刷新：通过setFormNextRefreshTime接口指定卡片的下一次刷新时间（最短时间5分钟），例如，在接口调用的5分钟后刷新卡片内容。

```
import formProvider from '@ohos.app.form.formProvider';

let formId = '123456789'; // 实际业务场景需要使用正确的formId
try {
  // 设置过5分钟后更新卡片内容
  formProvider.setFormNextRefreshTime(formId, 5, (err, data) => {
    if (err) {
      console.error(`Failed to setFormNextRefreshTime. Code: ${err.code}, message: ${err.message}`);
      return;
    } else {
      console.info('Succeeded in setFormNextRefreshTimeing.');
    }
  });
} catch (err) {
  console.error(`Failed to setFormNextRefreshTime. Code: ${err.code}, message: ${err.message}`);
}
```

在触发定时、定点或主动刷新后，系统会调用FormExtensionAbility的onUpdateForm生命周期回调，在回调中，可以使用updateForm进行提供方刷新卡片。onUpdateForm生命周期回调参考[通过FormExtensionAbility刷新卡片内容](https://developer.harmonyos.com/cn/docs/documentation/doc-guides-V3/arkts-ui-widget-event-formextensionability-0000001502350018-V3)。

说明

1. 定时刷新有配额限制，每张卡片每天最多通过定时方式触发刷新50次，定时刷新包含[卡片配置项updateDuration](https://developer.harmonyos.com/cn/docs/documentation/doc-guides-V3/arkts-ui-widget-configuration-0000001502333060-V3#ZH-CN_TOPIC_0000001523808634__table959386016151722)和调用setFormNextRefreshTime两种，当达到50次配额后，无法通过定时方式再次触发刷新，刷新次数会在每天的0点重置。
2. 当前定时刷新使用同一个计时器进行计时，因此卡片定时刷新的第一次刷新会有最多30分钟的偏差。比如第一张卡片A(每隔半小时刷新一次)在3点20分添加成功，定时器启动并每隔半小时触发一次事件，第二张卡片B(每隔半小时刷新一次)在3点40分添加成功，在3点50分定时器事件触发时，卡片A触发定时刷新，卡片B会在下次事件(4点20分)中才会触发。
3. 定时刷新和定点刷新仅在屏幕亮屏情况下才会触发，在灭屏场景下仅会将记录刷新动作，待亮屏时统一进行刷新。

