# 应用配置文件概述（Stage模型）

更新时间: 2024-01-10 11:30

每个应用项目必须在项目的代码目录下加入配置文件，这些配置文件会向编译工具、操作系统和应用市场提供应用的基本信息。

在基于Stage模型开发的应用项目代码下，都存在一个app.json5及一个或多个module.json5这两种配置文件。

[app.json5](https://developer.harmonyos.com/cn/docs/documentation/doc-guides-V3/app-configuration-file-0000001427584584-V3)主要包含以下内容：

* 应用的全局配置信息，包含应用的包名、开发厂商、版本号等基本信息。
* 特定设备类型的配置信息。

[module.json5](https://developer.harmonyos.com/cn/docs/documentation/doc-guides-V3/module-configuration-file-0000001427744540-V3)主要包含以下内容：

* Module的基本配置信息，例如Module名称、类型、描述、支持的设备类型等基本信息。
* [应用组件](https://developer.harmonyos.com/cn/docs/documentation/doc-guides-V3/stage-model-development-overview-0000001427744552-V3)信息，包含UIAbility组件和ExtensionAbility组件的描述信息。
* 应用运行过程中所需的权限信息。

