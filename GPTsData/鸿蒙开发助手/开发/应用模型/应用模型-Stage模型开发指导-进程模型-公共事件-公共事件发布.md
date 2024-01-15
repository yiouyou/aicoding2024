# 公共事件发布

更新时间: 2024-01-15 12:19

## 场景介绍

当需要发布某个自定义公共事件时，可以通过publish()方法发布事件。发布的公共事件可以携带数据，供订阅者解析并进行下一步处理。

注意

已发出的粘性公共事件后来订阅者也可以接收到，其他公共事件都需要先订阅再接收，订阅参考[公共事件订阅章节](https://developer.harmonyos.com/cn/docs/documentation/doc-guides-V3/common-event-subscription-0000001544583897-V3)。

## 接口说明

详细接口见[接口文档](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/js-apis-commonevent-0000001478181597-V3#ZH-CN_TOPIC_0000001523648890__commoneventpublish)。

| 接口名                                                                                                                                                                                                                                                      | 接口描述                     |
| :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :--------------------------- |
| publish(event: string, callback: AsyncCallback)                                                                                                                                                                                                             | 发布公共事件。               |
| publish(event: string, options:[CommonEventPublishData](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/js-apis-commoneventmanager-0000001427902640-V3#ZH-CN_TOPIC_0000001574088313__commoneventpublishdata), callback: AsyncCallback) | 指定发布信息并发布公共事件。 |

## 发布不携带信息的公共事件

不携带信息的公共事件，只能发布无序公共事件。

1. 导入CommonEvent模块。
```
import commonEvent from '@ohos.commonEventManager';
```
2. 传入需要发布的事件名称和回调函数，发布事件。
```
// 发布公共事件
commonEvent.publish("usual.event.SCREEN_OFF", (err) => {
    if (err) {
        console.error(`[CommonEvent] PublishCallBack err=${JSON.stringify(err)}`);
    } else {
        console.info(`[CommonEvent] Publish success`);
    }
})
```

## 发布携带信息的公共事件

携带信息的公共事件，可以发布为无序公共事件、有序公共事件和粘性事件，可以通过参数[CommonEventPublishData](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/js-apis-commoneventmanager-0000001427902640-V3#ZH-CN_TOPIC_0000001574088313__commoneventpublishdata)的isOrdered、isSticky的字段进行设置。

1. 导入CommonEvent模块。
```
import commonEvent from '@ohos.commonEventManager';
```
2. 传入需要发布的事件名称和回调函数，发布事件。
```
// 公共事件相关信息
let options = {
    code: 1, // 公共事件的初始代码
    data: "initial data", // 公共事件的初始数据
}
```
3. 传入需要发布的事件名称、需要发布的指定信息和回调函数，发布事件。
```
// 发布公共事件
commonEventManager.publish("custom_event", options, (err) => {
    if (err) {
        console.error('[CommonEvent] PublishCallBack err=' + JSON.stringify(err));
    } else {
        console.info('[CommonEvent] Publish success')
    }
})
```

