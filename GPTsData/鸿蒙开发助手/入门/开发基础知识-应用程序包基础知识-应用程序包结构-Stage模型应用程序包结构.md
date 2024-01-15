# Stage模型应用程序包结构

更新时间: 2024-01-10 11:59

基于[Stage模型](https://developer.harmonyos.com/cn/docs/documentation/doc-guides-V3/application-configuration-file-overview-stage-0000001428061460-V3)开发的应用，经编译打包后，其应用程序包结构如下图 应用程序包结构（Stage模型） 所示。开发者需要熟悉应用程序包结构相关的基本概念。

* 在开发态，一个应用包含一个或者多个Module，可以在DevEco Studio工程中[创建一个或者多个Module](https://developer.harmonyos.com/cn/docs/documentation/doc-guides-V3/add_new_module-0000001053223741-V3)。Module是HarmonyOS应用/服务的基本功能单元，包含了源代码、资源文件、第三方库及应用/服务配置文件，每一个Module都可以独立进行编译和运行。Module分为“Ability”和“Library”两种类型，“Ability”类型的Module对应于编译后的HAP（Harmony Ability Package）；“Library”类型的Module对应于[HAR](https://developer.harmonyos.com/cn/docs/documentation/doc-guides-V3/har-package-0000001573432125-V3)（Harmony Archive），或者[HSP](https://developer.harmonyos.com/cn/docs/documentation/doc-guides-V3/in-app-hsp-0000001523312158-V3)（Harmony Shared Package）。
  一个Module可以包含一个或多个[UIAbility](https://developer.harmonyos.com/cn/docs/documentation/doc-guides-V3/uiability-overview-0000001477980929-V3)组件，如下图所示。
  图1 Module与UIAbility组件关系示意图
  ![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231222175602.06348448876678338911787765671508:50001231000000:2800:926268A336ACD4027F5295E0DE02DDC0BA87F9490C1EE6AA404E153A0AB02EA3.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)
  全文中介绍到的Module默认指的是“Ability”类型的Module。
* 开发者通过DevEco Studio把应用程序编译为一个或者多个.hap后缀的文件，即HAP。HAP是HarmonyOS应用安装的基本单位，包含了编译后的代码、资源、三方库及配置文件。HAP可分为Entry和Feature两种类型。
  * Entry类型的HAP：是应用的主模块，在[module.json5配置文件](https://developer.harmonyos.com/cn/docs/documentation/doc-guides-V3/module-configuration-file-0000001427744540-V3)中的type标签配置为“entry”类型。在同一个应用中，同一设备类型只支持一个Entry类型的HAP，通常用于实现应用的入口界面、入口图标、主特性功能等。
  * Feature类型的HAP：是应用的动态特性模块，在[module.json5配置文件](https://developer.harmonyos.com/cn/docs/documentation/doc-guides-V3/module-configuration-file-0000001427744540-V3)中的type标签配置为“feature”类型。一个应用程序包可以包含一个或多个Feature类型的HAP，也可以不包含；Feature类型的HAP通常用于实现应用的特性功能，可以配置成按需下载安装，也可以配置成随Entry类型的HAP一起下载安装（请参见[module对象内部结构](https://developer.harmonyos.com/cn/docs/documentation/doc-guides-V3/module-configuration-file-0000001427744540-V3)中的“deliveryWithInstall”）。
* 每个HarmonyOS应用可以包含多个.hap文件，一个应用中的.hap文件合在一起称为一个Bundle，而bundleName就是应用的唯一标识（请参见[app.json5配置文件](https://developer.harmonyos.com/cn/docs/documentation/doc-guides-V3/app-configuration-file-0000001427584584-V3)中的bundleName标签）。需要特别说明的是：在应用上架到应用市场时，需要把应用包含的所有.hap文件（即Bundle）打包为一个.app后缀的文件用于上架，这个.app文件称为App Pack（Application Package），其中同时包含了描述App Pack属性的pack.info文件；在云端（服务器）分发和终端设备安装时，都是以HAP为单位进行分发和安装的。
* 打包后的HAP包结构包括ets、libs、resources等文件夹和resources.index、module.json、pack.info等文件。
  * ets目录用于存放应用代码编译后的字节码文件。
  * libs目录用于存放库文件。库文件是HarmonyOS应用依赖的第三方代码（.so二进制文件）。
  * resources目录用于存放应用的资源文件（字符串、图片等），便于开发者使用和维护，详见[资源分类与访问](https://developer.harmonyos.com/cn/docs/documentation/doc-guides-V3/resource-categories-and-access-0000001711674888-V3)。
  * resources.index是资源索引表，由IDE编译工程时生成。
  * module.json是HAP的配置文件，内容由工程配置中的module.json5和app.json5组成，该文件是HAP中必不可少的文件。IDE会自动生成一部分默认配置，开发者按需修改其中的配置。详细字段请参见[应用配置文件](https://developer.harmonyos.com/cn/docs/documentation/doc-guides-V3/application-configuration-file-overview-stage-0000001428061460-V3)。
  * pack.info是Bundle中用于描述每个HAP属性的文件，例如app中的bundleName和versionCode信息、module中的name、type和abilities等信息，由IDE工具生成Bundle包时自动生成。

  图2 应用程序包结构（Stage模型）
  ![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231222175602.65944847906957402204737313379023:50001231000000:2800:5E22A01EF4BB7428597F5ADFC4DA09752ACC1BDF9BDA621EA63556E41B679895.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)

