# ArkTS卡片相关模块

更新时间: 2024-01-15 12:20

图1 ArkTS卡片相关模块
![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231121183816.58959716451617224104657554983988:50001231000000:2800:66F5D0DCFE26D6E5FA8C71D3F18AF038D10CE3C9B80652B6956E45906CB91634.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true "点击放大")

* [FormExtensionAbility](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/js-apis-app-form-formextensionability-0000001493424316-V3)：卡片扩展模块，提供卡片创建、销毁、刷新等生命周期回调。
* FormExtensionContext：FormExtensionAbility的上下文环境，提供FormExtensionAbility具有的接口和能力。
* [formProvider](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/js-apis-app-form-formprovider-0000001544464081-V3)：提供卡片提供方相关的接口能力，可通过该模块提供接口实现更新卡片、设置卡片更新时间、获取卡片信息、请求发布卡片等。
* [formInfo](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/js-apis-app-form-forminfo-0000001493903980-V3)：提供了卡片信息和状态等相关类型和枚举。
* [formBindingData](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/js-apis-app-form-formbindingdata-0000001544703921-V3)：提供卡片数据绑定的能力，包括FormBindingData对象的创建、相关信息的描述。
* [页面布局（Card.ets）](https://developer.harmonyos.com/cn/docs/documentation/doc-guides-V3/arkts-ui-widget-page-overview-0000001553173049-V3)：提供声明式范式的UI接口能力。
  * [ArkTS卡片特有能力](https://developer.harmonyos.com/cn/docs/documentation/doc-guides-V3/arkts-ui-widget-event-overview-0000001553069581-V3)：postCardAction用于卡片内部和提供方应用间的交互，仅在卡片中可以调用。
  * [ArkTS卡片能力列表](https://developer.harmonyos.com/cn/docs/documentation/doc-guides-V3/arkts-ui-widget-page-overview-0000001553173049-V3#section17744162145013)：列举了能在ArkTS卡片中使用的API、组件、事件、属性和生命周期调度。
* [卡片配置](https://developer.harmonyos.com/cn/docs/documentation/doc-guides-V3/arkts-ui-widget-configuration-0000001502333060-V3)：包含FormExtensionAbility的配置和卡片的配置
  * 在[module.json5配置文件](https://developer.harmonyos.com/cn/docs/documentation/doc-guides-V3/module-configuration-file-0000001427744540-V3)中的extensionAbilities标签下，配置FormExtensionAbility相关信息。
  * 在resources/base/profile/目录下的[form_config.json配置文件](https://developer.harmonyos.com/cn/docs/documentation/doc-guides-V3/arkts-ui-widget-configuration-0000001502333060-V3#ZH-CN_TOPIC_0000001523808634__table959386016151722)中，配置卡片（WidgetCard.ets）相关信息。

