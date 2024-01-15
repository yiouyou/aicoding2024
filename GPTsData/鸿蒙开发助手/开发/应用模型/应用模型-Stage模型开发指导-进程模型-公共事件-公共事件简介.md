# 公共事件简介

更新时间: 2024-01-15 12:17

HarmonyOS通过CES（Common Event Service，公共事件服务）为应用程序提供订阅、发布、退订公共事件的能力。

公共事件从系统角度可分为：系统公共事件和自定义公共事件。

* 系统公共事件：CES内部定义的公共事件，只有系统应用和系统服务才能发布，例如HAP安装，更新，卸载等公共事件。目前支持的系统公共事件详见[系统公共事件定义](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/commoneventmanager-definitions-0000001493424344-V3)。
* 自定义公共事件：应用自定义一些公共事件用来实现跨进程的事件通信能力。

公共事件按发送方式可分为：无序公共事件、有序公共事件和粘性公共事件。

* 无序公共事件：CES转发公共事件时，不考虑订阅者是否接收到，且订阅者接收到的顺序与其订阅顺序无关。
* 有序公共事件：CES转发公共事件时，根据订阅者设置的优先级等级，优先将公共事件发送给优先级较高的订阅者，等待其成功接收该公共事件之后再将事件发送给优先级较低的订阅者。如果有多个订阅者具有相同的优先级，则他们将随机接收到公共事件。
* 粘性公共事件：能够让订阅者收到在订阅前已经发送的公共事件就是粘性公共事件。普通的公共事件只能在订阅后发送才能收到，而粘性公共事件的特殊性就是可以先发送后订阅。发送粘性事件必须是系统应用或系统服务，且需要申请ohos.permission.COMMONEVENT_STICKY权限，配置方式请参阅[访问控制授权申请指导](https://developer.harmonyos.com/cn/docs/documentation/doc-guides-V3/accesstoken-guidelines-0000001493744016-V3#ZH-CN_TOPIC_0000001574088333__stage%E6%A8%A1%E5%9E%8B)。

每个应用都可以按需订阅公共事件，订阅成功，当公共事件发布时，系统会将其发送给对应的应用。这些公共事件可能来自系统、其他应用和应用自身。

图1 公共事件示意图

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20240103115012.44536390775276881684360472468542:50001231000000:2800:92B9D2C9ABA98B9CAA382490A39F880D50740D784A686E40F4A0145BB9EB6336.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)

