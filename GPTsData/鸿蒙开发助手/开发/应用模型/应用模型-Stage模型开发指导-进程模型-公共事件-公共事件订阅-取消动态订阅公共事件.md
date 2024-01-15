# 取消动态订阅公共事件

更新时间: 2024-01-15 11:54

## 场景介绍

动态订阅者完成业务需要时，需要主动取消订阅，订阅者通过调用[unsubscribe()](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/js-apis-commoneventmanager-0000001427902640-V3#ZH-CN_TOPIC_0000001574088313__commoneventmanagerunsubscribe)方法取消订阅事件。

## 接口说明

| 接口名                                                                   | 接口描述         |
| :------------------------------------------------------------------------- | :----------------- |
| unsubscribe(subscriber: CommonEventSubscriber, callback?: AsyncCallback) | 取消订阅公共事件 |

## 开发步骤

1. 导入CommonEvent模块。

```
import commonEvent from '@ohos.commonEventManager';
```

1. 根据[动态订阅公共事件](https://developer.harmonyos.com/cn/docs/documentation/doc-guides-V3/common-event-subscription-0000001544583897-V3)章节的步骤来订阅某个事件。
2. 调用CommonEvent中的unsubscribe方法取消订阅某事件。
```
// subscriber为订阅事件时创建的订阅者对象
if (subscriber !== null) {
    commonEvent.unsubscribe(subscriber, (err) => {
        if (err) {
            console.error(`[CommonEvent] UnsubscribeCallBack err=${JSON.stringify(err)}`)
        } else {
            console.info(`[CommonEvent] Unsubscribe`)
            subscriber = null
        }
    })
}
```

