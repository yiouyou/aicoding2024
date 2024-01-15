# ExtensionAbility组件

更新时间: 2024-01-15 11:54

ExtensionAbility组件是基于特定场景提供的应用组件，以便满足更多的使用场景。

每一个具体场景对应一个[ExtensionAbilityType](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/js-apis-bundlemanager-0000001427585060-V3#ZH-CN_TOPIC_0000001573928977__extensionabilitytype)，各类型的ExtensionAbility组件均由相应的系统服务统一管理，例如InputMethodExtensionAbility组件由输入法管理服务统一管理。当前支持的ExtensionAbility类型有：

* [FormExtensionAbility](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/js-apis-app-form-formextensionability-0000001493424316-V3)：FORM类型的ExtensionAbility组件，用于提供服务卡片场景相关能力。
* [WorkSchedulerExtensionAbility](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/js-apis-workschedulerextensionability-0000001493904024-V3)：WORK_SCHEDULER类型的ExtensionAbility组件，用于提供延迟任务注册、取消、查询的能力。

