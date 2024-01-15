# 应用/组件级配置

更新时间: 2024-01-15 12:17

在开发应用时，需要配置应用的一些标签，例如应用的包名、图标等标识特征的属性。本文描述了在开发应用需要配置的一些关键标签。图标和标签通常一起配置，可以分为应用图标、应用标签和入口图标、入口标签，分别对应[app.json5配置文件](https://developer.harmonyos.com/cn/docs/documentation/doc-guides-V3/app-configuration-file-0000001427584584-V3)和[module.json5配置文件](https://developer.harmonyos.com/cn/docs/documentation/doc-guides-V3/module-configuration-file-0000001427744540-V3)文件中的icon和label标签。应用图标和标签是在设置应用中使用，例如设置应用中的应用列表。入口图标是应用安装完成后在设备桌面上显示出来的，如图一所示。入口图标是以[UIAbility](https://developer.harmonyos.com/cn/docs/documentation/doc-guides-V3/uiability-overview-0000001477980929-V3)为粒度，支持同一个应用存在多个入口图标和标签，点击后进入对应的UIAbility界面。

图1 应用图标和标签

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231121183808.47800877830405254968295228528543:50001231000000:2800:F91F650D8625C46F4C013F689E347E890ECC2873F208A4CC729F550117942BC4.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)

* 应用包名配置
  应用需要在工程的AppScope目录下的[app.json5配置文件](https://developer.harmonyos.com/cn/docs/documentation/doc-guides-V3/app-configuration-file-0000001427584584-V3)中配置bundleName标签，该标签用于标识应用的唯一性。推荐采用反域名形式命名（如com.example.demo，建议第一级为域名后缀com，第二级为厂商/个人名，第三级为应用名，也可以多级）。
* 应用图标和标签配置
  Stage模型的应用需要配置应用图标和应用标签。应用图标和标签是在设置应用中使用，例如设置应用中的应用列表，会显示出对应的图标和标签。
  应用图标需要在工程的AppScope目录下的[app.json5配置文件](https://developer.harmonyos.com/cn/docs/documentation/doc-guides-V3/app-configuration-file-0000001427584584-V3)中配置icon标签。应用图标需配置为图片的资源索引，配置完成后，该图片即为应用的图标。
  应用标签需要在工程的AppScope模块下的[app.json5配置文件](https://developer.harmonyos.com/cn/docs/documentation/doc-guides-V3/app-configuration-file-0000001427584584-V3)中配置label标签。标识应用对用户显示的名称，需要配置为字符串资源的索引。
```
  {
    "app": {
      "icon": "$media:app_icon",
      "label": "$string:app_name"
      // ...
    }
  }
```
* 入口图标和标签配置
  Stage模型支持对组件配置入口图标和入口标签。入口图标和入口标签会显示在桌面上。
  入口图标需要在[module.json5配置文件](https://developer.harmonyos.com/cn/docs/documentation/doc-guides-V3/module-configuration-file-0000001427744540-V3)中配置，在abilities标签下面有icon标签。例如希望在桌面上显示该UIAbility的图标，则需要在skills标签下面的entities中添加"entity.system.home"、actions中添加"action.system.home"。同一个应用有多个UIAbility配置上述字段时，桌面上会显示出多个图标，分别对应各自的UIAbility。
```
{
  "module": {
    // ...
    "abilities": [
      {
        // $开头的为资源值
        "icon": "$media:icon",
        "label": "$string:EntryAbility_label",
        "skills": [
          {
            "entities": [
              "entity.system.home"
            ],
            "actions": [
              "action.system.home"
            ]
          }
        ],
      }
    ]
  }
}
```
* 应用版本声明配置
  应用版本声明需要在工程的AppScope目录下的[app.json5配置文件](https://developer.harmonyos.com/cn/docs/documentation/doc-guides-V3/app-configuration-file-0000001427584584-V3)中配置versionCode标签和versionName标签。versionCode用于标识应用的版本号，该标签值为32位非负整数。此数字仅用于确定某个版本是否比另一个版本更新，数值越大表示版本越高。versionName标签标识版本号的文字描述。
* Module支持的设备类型配置
  Module支持的设备类型需要在[module.json5配置文件](https://developer.harmonyos.com/cn/docs/documentation/doc-guides-V3/module-configuration-file-0000001427744540-V3)中配置deviceTypes标签，如果deviceTypes标签中添加了某种设备，则表明当前的Module支持在该设备上运行。
* Module权限配置
  Module访问系统或其他应用受保护部分所需的权限信息需要在[module.json5配置文件](https://developer.harmonyos.com/cn/docs/documentation/doc-guides-V3/module-configuration-file-0000001427744540-V3)中配置requestPermission标签。该标签用于声明需要申请权限的名称、申请权限的原因以及权限使用的场景。

