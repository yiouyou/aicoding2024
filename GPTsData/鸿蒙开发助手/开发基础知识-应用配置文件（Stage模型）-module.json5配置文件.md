# module.json5配置文件

更新时间: 2024-01-10 11:58

先通过一个示例，整体认识一下module.json5配置文件。

```
{
  "module": {
    "name": "entry",
    "type": "entry",
    "description": "$string:module_desc",
    "mainElement": "EntryAbility",
    "deviceTypes": [
      "tv",
      "tablet"
    ],
    "deliveryWithInstall": true,
    "installationFree": false,
    "pages": "$profile:main_pages",
    "virtualMachine": "ark",
    "metadata": [
      {
        "name": "string",
        "value": "string",
        "resource": "$profile:distributionFilter_config"
      }
    ],
    "abilities": [
      {
        "name": "EntryAbility",
        "srcEntry": "./ets/entryability/EntryAbility.ts",
        "description": "$string:EntryAbility_desc",
        "icon": "$media:icon",
        "label": "$string:EntryAbility_label",
        "startWindowIcon": "$media:icon",
        "startWindowBackground": "$color:start_window_background",
        "exported": true,
        "skills": [
          {
            "entities": [
              "entity.system.home"
            ],
            "actions": [
              "ohos.want.action.home"
            ]
          }
        ]
      }
    ],
    "requestPermissions": [
      {
        "name": "ohos.abilitydemo.permission.PROVIDER",
        "reason": "$string:reason",
        "usedScene": {
          "abilities": [
            "FormAbility"
          ],
          "when": "inuse"
        }
      }
    ]
  }
}
```

module.json5配置文件包含以下标签。

表1 module.json5配置文件配置标签说明

| 属性名称                                                                                                                                                                                                | 含义                                                                                                                                                                                                                                                                                                                      | 数据类型   | 是否可缺省                                           |
| :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | :--------- | :--------------------------------------------------- |
| name                                                                                                                                                                                                    | 标识当前Module的名称，标签值采用字符串表示（最大长度31个字节），该名称在整个应用要唯一，仅支持英文字符。                                                                                                                                                                                                                  | 字符串     | 该标签不可缺省。                                     |
| type                                                                                                                                                                                                    | 标识当前Module的类型。类型有两种，分别：- entry：应用的主模块。- feature：应用的动态特性模块。                                                                                                                                                                                                                            | 字符串     | 该标签不可缺省。                                     |
| srcEntry                                                                                                                                                                                                | 标识当前Module所对应的代码路径，标签值为字符串（最长为127字节）。                                                                                                                                                                                                                                                         | 字符串     | 该标签可缺省，缺省值为空。                           |
| description                                                                                                                                                                                             | 标识当前Module的描述信息，标签值是字符串类型（最长255字节）或对描述内容的字符串资源索引。                                                                                                                                                                                                                                 | 字符串     | 该标签可缺省，缺省值为空。                           |
| process                                                                                                                                                                                                 | 标识当前Module的进程名，标签值为字符串类型（最长为31个字节）。如果在HAP标签下配置了process，该应用的所有UIAbility、DataShareExtensionAbility、ServiceExtensionAbility都运行在该进程中。说明：- 仅支持系统应用配置，三方应用配置不生效。                                                                                   | 字符串     | 可缺省，缺省为app.json5文件下app标签下的bundleName。 |
| mainElement                                                                                                                                                                                             | 标识当前Module的入口UIAbility名称或者ExtensionAbility名称。标签最大字节长度为255。                                                                                                                                                                                                                                        | 字符串     | 该标签可缺省，缺省值为空。                           |
| [deviceTypes](https://developer.harmonyos.com/cn/docs/documentation/doc-guides-V3/module-configuration-file-0000001427744540-V3#ZH-CN_TOPIC_0000001573929365__devicetypes%E6%A0%87%E7%AD%BE)               | 标识当前Module可以运行在哪类设备上，标签值采用字符串数组的表示。                                                                                                                                                                                                                                                          | 字符串数组 | 该标签不可缺省。                                     |
| deliveryWithInstall                                                                                                                                                                                     | 标识当前Module是否在用户主动安装的时候安装，表示该Module对应的HAP是否跟随应用一起安装。- true：主动安装时安装。- false：主动安装时不安装。                                                                                                                                                                                | 布尔值     | 该标签不可缺省。                                     |
| installationFree                                                                                                                                                                                        | 标识当前Module是否支持免安装特性。- true：表示支持免安装特性，且符合免安装约束。- false：表示不支持免安装特性。说明：- 当应用的entry类型Module的该字段配置为true时，该应用的feature类型的该字段也需要配置为true。- 当应用的entry类型Module的该字段配置为false时，该应用的feature类型的该字段根据业务需求配置true或false。 | 布尔值     | 该标签不可缺省。                                     |
| virtualMachine                                                                                                                                                                                          | 标识当前Module运行的目标虚拟机类型，供云端分发使用，如应用市场和分发中心。该标签值为字符串。如果目标虚拟机类型为ArkTS引擎，则其值为“ark+版本号”。                                                                                                                                                                       | 字符串     | 该标签由IDE构建HAP的时候自动插入。                   |
| [pages](https://developer.harmonyos.com/cn/docs/documentation/doc-guides-V3/module-configuration-file-0000001427744540-V3#ZH-CN_TOPIC_0000001573929365__pages%E6%A0%87%E7%AD%BE)                           | 标识当前Module的profile资源，用于列举每个页面信息。该标签最大长度为255个字节。                                                                                                                                                                                                                                            | 字符串     | 在有UIAbility的场景下，该标签不可缺省。              |
| [metadata](https://developer.harmonyos.com/cn/docs/documentation/doc-guides-V3/module-configuration-file-0000001427744540-V3#ZH-CN_TOPIC_0000001573929365__metadata%E6%A0%87%E7%AD%BE)                     | 标识当前Module的自定义元信息，标签值为数组类型，只对当前Module、UIAbility、ExtensionAbility生效。                                                                                                                                                                                                                         | 对象数组   | 该标签可缺省，缺省值为空。                           |
| [abilities](https://developer.harmonyos.com/cn/docs/documentation/doc-guides-V3/module-configuration-file-0000001427744540-V3#ZH-CN_TOPIC_0000001573929365__abilities%E6%A0%87%E7%AD%BE)                   | 标识当前Module中UIAbility的配置信息，标签值为数组类型，只对当前UIAbility生效。                                                                                                                                                                                                                                            | 对象       | 该标签可缺省，缺省值为空。                           |
| [extensionAbilities](https://developer.harmonyos.com/cn/docs/documentation/doc-guides-V3/module-configuration-file-0000001427744540-V3#ZH-CN_TOPIC_0000001573929365__extensionabilities%E6%A0%87%E7%AD%BE) | 标识当前Module中ExtensionAbility的配置信息，标签值为数组类型，只对当前ExtensionAbility生效。                                                                                                                                                                                                                              | 对象       | 该标签可缺省，缺省值为空。                           |
| [requestPermissions](https://developer.harmonyos.com/cn/docs/documentation/doc-guides-V3/module-configuration-file-0000001427744540-V3#ZH-CN_TOPIC_0000001573929365__requestpermissions%E6%A0%87%E7%AD%BE) | 标识当前应用运行时需向系统申请的权限集合。                                                                                                                                                                                                                                                                                | 对象       | 该标签可缺省，缺省值为空。                           |
| [testRunner](https://developer.harmonyos.com/cn/docs/documentation/doc-guides-V3/module-configuration-file-0000001427744540-V3#ZH-CN_TOPIC_0000001573929365__testrunner%E6%A0%87%E7%AD%BE)                 | 标识当前Module用于支持对测试框架的配置。                                                                                                                                                                                                                                                                                  | 对象       | 该标签可缺省，缺省值为空。                           |

## deviceTypes标签

表2 deviceType标签配置说明

| 设备类型 | 枚举值   | 说明                                 |
| :------- | :------- | :----------------------------------- |
| 平板     | tablet   | -                                    |
| 智慧屏   | tv       | -                                    |
| 智能手表 | wearable | 系统能力较丰富的手表，具备电话功能。 |
| 车机     | car      | -                                    |
| 手机     | phone    | -                                    |

deviceTypes示例：

```
{
  "module": {
    "name": "myHapName",
    "type": "feature",
    "deviceTypes" : [
       "tablet"
    ]
  }
}
```

## pages标签

该标签是一个profile文件资源，用于指定描述页面信息的配置文件。

```
{
  "module": {
    // ...
    "pages": "$profile:main_pages", // 通过profile下的资源文件配置
  }
}
```

在开发视图的resources/base/profile下面定义配置文件 main_pages .json，其中文件名( main_pages )可自定义，需要和前文中pages标签指定的信息对应，配置文件中列举了当前应用组件中的页面信息。

表3 pages配置文件标签说明

| 属性名称 | 含义                                                                                                                 | 数据类型   | 是否可缺省                 |
| :------- | :------------------------------------------------------------------------------------------------------------------- | :--------- | :------------------------- |
| src      | 描述有关JavaScript模块中所有页面的路由信息，包括页面路径和页面名称。该值是一个字符串数组，其中每个元素表示一个页面。 | 字符串数组 | 该标签不可缺省。           |
| window   | 用于定义与显示窗口相关的配置。                                                                                       | 对象       | 该标签可缺省，缺省值为空。 |

表4 pages配置文件中的window标签说明

| 属性名称        | 含义                                                                                                                | 数据类型 | 是否可缺省              |
| :-------------- | :------------------------------------------------------------------------------------------------------------------ | :------- | :---------------------- |
| designWidth     | 标识页面设计基准宽度。以此为基准，根据实际设备宽度来缩放元素大小。                                                  | 数值     | 可缺省，缺省值为720px。 |
| autoDesignWidth | 标识页面设计基准宽度是否自动计算。当配置为true时，designWidth将会被忽略，设计基准宽度由设备宽度与屏幕密度计算得出。 | 布尔值   | 可缺省，缺省值为false。 |

```
{
  "src": [
    "pages/index/mainPage",
    "pages/second/payment",
    "pages/third/shopping_cart",
    "pages/four/owner"
  ]
}
```

## metadata标签

该标签标识HAP的自定义元信息，标签值为数组类型，包含name，value，resource三个子标签。

表5 metadata标签说明

| 属性名称 | 含义                                                                                              | 数据类型 | 是否可缺省                 |
| :------- | :------------------------------------------------------------------------------------------------ | :------- | :------------------------- |
| name     | 该标签标识数据项的键名称，字符串类型（最大长度255字节）。                                         | 字符串   | 该标签可缺省，缺省值为空。 |
| value    | 该标签标识数据项的值，标签值为字符串（最大长度255字节）。                                         | 字符串   | 该标签可缺省，缺省值为空。 |
| resource | 该标签标识定义用户自定义数据格式，标签值为标识该数据的资源的索引值。该标签最大字节长度为255字节。 | 字符串   | 该标签可缺省，缺省值为空。 |

```
{
  "module": {
    "metadata": [{
      "name": "module_metadata",
      "value": "a test demo for module metadata",
      "resource": "$profile:shortcuts_config",
    }],

    "abilities": [{
      "metadata": [{
        "name": "ability_metadata",
        "value": "a test demo for ability",
        "resource": "$profile:config_file"
      },
      {
        "name": "ability_metadata_2",
        "value": "a string test",
        "resource": "$profile:config_file"
      }],
    }],

    "extensionAbilities": [{
      "metadata": [{
        "name": "extensionAbility_metadata",
        "value": "a test for extensionAbility",
        "resource": "$profile:config_file"
      },
      {
        "name": "extensionAbility_metadata_2",
        "value": "a string test",
        "resource": "$profile:config_file"
      }],
    }]
  }
}
```

## abilities标签

abilities标签描述UIAbility组件的配置信息，标签值为数组类型，该标签下的配置只对当前UIAbility生效。

表6 abilities标签说明

| 属性名称                                                                                                                                                                            | 含义                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | 数据类型   | 是否可缺省                                                                   |
| :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | :--------- | :--------------------------------------------------------------------------- |
| name                                                                                                                                                                                | 标识当前UIAbility组件的名称，该名称在整个应用要唯一，标签值采用字符串表示（最大长度127个字节），仅支持英文字符。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | 字符串     | 该标签不可缺省。                                                             |
| srcEntry                                                                                                                                                                            | 该标签标识入口UIAbility的代码路径，标签值为字符串（最长为127字节）。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | 字符串     | 该标签不可缺省。                                                             |
| [launchType](https://developer.harmonyos.com/cn/docs/documentation/doc-guides-V3/uiability-launch-type-0000001428061476-V3)                                                            | 标识当前UIAbility组件的启动模式，可选标签值：- multiton：多实例模式，每次启动创建一个新的实例。- singleton：单实例模式，仅第一次启动创建新实例。- specified：指定实例模式，运行时由开发者决定是否创建新实例。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | 字符串     | 可缺省，该标签缺省为“singleton”。                                          |
| description                                                                                                                                                                         | 标识当前UIAbility组件的描述信息，标签值是字符串类型（最长255字节）或对描述内容的资源索引，要求采用资源索引方式，以支持多语言。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | 字符串     | 该标签可缺省，缺省值为空。                                                   |
| icon                                                                                                                                                                                | 标识当前UIAbility组件的图标，标签值为图标资源文件的索引。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | 字符串     | 该标签可缺省，缺省值为空。如果UIAbility被配置为MainElement，该标签必须配置。 |
| label                                                                                                                                                                               | 标识当前UIAbility组件对用户显示的名称，标签值配置为该名称的资源索引以支持多语言。如果UIAbility被配置当前Module的mainElement时，该标签必须配置，且应用内唯一。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | 字符串     | 该标签不可缺省。                                                             |
| permissions                                                                                                                                                                         | 标识当前UIAbility组件自定义的权限信息。当其他应用访问该UIAbility时，需要申请相应的权限信息。一个数组元素为一个权限名称。通常采用反向域名格式（最大255字节），取值为系统预定义的权限。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | 字符串数组 | 该标签可缺省，缺省值为空。                                                   |
| [metadata](https://developer.harmonyos.com/cn/docs/documentation/doc-guides-V3/module-configuration-file-0000001427744540-V3#ZH-CN_TOPIC_0000001573929365__metadata%E6%A0%87%E7%AD%BE) | 标识当前UIAbility组件的元信息。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | 对象数组   | 该标签可缺省，缺省值为空。                                                   |
| exported                                                                                                                                                                            | 标识当前UIAbility组件是否可以被其他应用调用。- true：表示可以被其他应用调用。- false：表示不可以被其他应用调用。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | 布尔值     | 该标签可缺省，缺省值为false。                                                |
| continuable                                                                                                                                                                         | 标识当前UIAbility组件是否可以迁移。- true：表示可以被迁移。- false：表示不可以被迁移。说明当前版本暂不支持跨设备能力。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | 布尔值     | 该标签可缺省，缺省值为false。                                                |
| [skills](https://developer.harmonyos.com/cn/docs/documentation/doc-guides-V3/module-configuration-file-0000001427744540-V3#ZH-CN_TOPIC_0000001573929365__skills%E6%A0%87%E7%AD%BE)     | 标识当前UIAbility组件或ExtensionAbility组件能够接收的[Want](https://developer.harmonyos.com/cn/docs/documentation/doc-guides-V3/want-overview-0000001478340877-V3)的特征集，为数组格式。配置规则：- 对于Entry类型的HAP，应用可以配置多个具有入口能力的skills标签（即配置了ohos.want.action.home和entity.system.home）。- 对于Feature类型的HAP，只有应用可以配置具有入口能力的skills标签，服务不允许配置。                                                                                                                                                                                                                                                                                            | 对象数组   | 该标签可缺省，缺省值为空。                                                   |
| backgroundModes                                                                                                                                                                     | 标识当前UIAbility组件的长时任务集合。指定用于满足特定类型的长时任务。长时任务类型有如下：- dataTransfer：通过网络/对端设备进行数据下载、备份、分享、传输等业务。- audioPlayback：音频输出业务。- audioRecording：音频输入业务。- location：定位、导航业务。- bluetoothInteraction：蓝牙扫描、连接、传输业务（穿戴）。- multiDeviceConnection：多设备互联业务。- wifiInteraction：Wi-Fi扫描、连接、传输业务（克隆多屏）。- voip：音视频电话，VoIP业务。- taskKeeping：计算业务。                                                                                                                                                                                                                   | 字符串数组 | 该标签可缺省，缺省值为空。                                                   |
| startWindowIcon                                                                                                                                                                     | 标识当前UIAbility组件启动页面图标资源文件的索引。取值示例：$media:icon。该标签最大字节长度为255。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | 字符串     | 不可缺省。                                                                   |
| startWindowBackground                                                                                                                                                               | 标识当前UIAbility组件启动页面背景颜色资源文件的索引。取值示例：$color:red。该标签最大字节长度为255。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | 字符串     | 不可缺省。                                                                   |
| removeMissionAfterTerminate                                                                                                                                                         | 标识当前UIAbility组件销毁后是否从任务列表中移除任务，为布尔类型：- true表示销毁后移除任务。- false表示销毁后不移除任务。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | 布尔值     | 该标签可缺省，缺省值为false。                                                |
| orientation                                                                                                                                                                         | 标识当前UIAbility组件启动时的方向。该方向的取值范围包括：- unspecified：未指定方向，由系统自动判断显示方向。- landscape：横屏。- portrait：竖屏。- landscape_inverted：反向横屏。- portrait_inverted：反向竖屏。- auto_rotation：随传感器旋转。- auto_rotation_landscape：传感器横屏旋转，包括了横屏和反向横屏。- auto_rotation_portrait：传感器竖屏旋转，包括了竖屏和反向竖屏。- auto_rotation_restricted：传感器开关打开，方向可随传感器旋转。- auto_rotation_landscape_restricted：传感器开关打开，方向可随传感器旋转为横屏， 包括了横屏和反向横屏。- auto_rotation_portrait_restricted：传感器开关打开，方向随可传感器旋转为竖屏， 包括了竖屏和反向竖屏。- locked：传感器开关关闭，方向锁定。 | 字符串     | 该标签可缺省，缺省值为unspecified。                                          |
| supportWindowMode                                                                                                                                                                   | 标识当前UIAbility组件所支持的窗口模式，包含：- fullscreen：全屏模式。- split：分屏模式。- floating：悬浮窗模式。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | 字符串数组 | 该标签可缺省，缺省值为["fullscreen", "split", "floating"]。                  |
| priority                                                                                                                                                                            | 标识当前UIAbility组件的优先级，仅支持系统应用配置，三方应用配置不生效。[隐式查询](https://developer.harmonyos.com/cn/docs/documentation/doc-guides-V3/explicit-implicit-want-mappings-0000001478061453-V3)时，优先级越高，UIAbility在返回列表越靠前。该标签取值为integer类型，取值范围0-10。数值越大，优先级越高。                                                                                                                                                                                                                                                                                                                                                                                   | 数值       | 该标签可缺省，缺省值为0。                                                    |
| maxWindowRatio                                                                                                                                                                      | 标识当前UIAbility组件支持的最大的宽高比。该标签最小取值为0。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | 数值       | 该标签可缺省，缺省值为平台支持的最大的宽高比。                               |
| minWindowRatio                                                                                                                                                                      | 标识当前UIAbility组件支持的最小的宽高比。该标签最小取值为0。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | 数值       | 该标签可缺省，缺省值为平台支持的最小的宽高比。                               |
| maxWindowWidth                                                                                                                                                                      | 标识当前UIAbility组件支持的最大的窗口宽度，宽度单位为vp。该标签最小取值为0。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | 数值       | 该标签可缺省，缺省值为平台支持的最大的窗口宽度。                             |
| minWindowWidth                                                                                                                                                                      | 标识当前UIAbility组件支持的最小的窗口宽度, 宽度单位为vp。该标签最小取值为0。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | 数值       | 该标签可缺省，缺省值为平台支持的最小的窗口宽度。                             |
| maxWindowHeight                                                                                                                                                                     | 标识当前UIAbility组件支持的最大的窗口高度, 高度单位为vp。该标签最小取值为0。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | 数值       | 该标签可缺省，缺省值为平台支持的最大的窗口高度。                             |
| minWindowHeight                                                                                                                                                                     | 标识当前UIAbility组件支持的最小的窗口高度, 高度单位为vp。该标签最小取值为0。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | 数值       | 该标签可缺省，缺省值为平台支持的最小的窗口高度。                             |
| excludeFromMissions                                                                                                                                                                 | 标识当前UIAbility组件是否在最近任务列表中显示。- true：表示不在任务列表中显示。- false：表示在任务列表中显示。说明：- 仅支持系统应用配置，三方应用配置不生效。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | 布尔值     | 该标签可缺省，缺省值为false。                                                |

abilities示例：

```
{
  "abilities": [{
    "name": "EntryAbility",
    "srcEntry": "./ets/entryability/EntryAbility.ts",
    "launchType":"singleton",
    "description": "$string:description_main_ability",
    "icon": "$media:icon",
    "label": "Login",
    "permissions": [],
    "metadata": [],
    "exported": true,
    "continuable": true,
    "skills": [{
      "actions": ["ohos.want.action.home"],
      "entities": ["entity.system.home"],
      "uris": []
    }],
    "backgroundModes": [
      "dataTransfer",
      "audioPlayback",
      "audioRecording",
      "location",
      "bluetoothInteraction",
      "multiDeviceConnection",
      "wifiInteraction",
      "voip",
      "taskKeeping"
    ],
    "startWindowIcon": "$media:icon",
    "startWindowBackground": "$color:red",
    "removeMissionAfterTerminate": true,
    "orientation": " ",
    "supportWindowMode": ["fullscreen", "split", "floating"],
    "maxWindowRatio": 3.5,
    "minWindowRatio": 0.5,
    "maxWindowWidth": 2560,
    "minWindowWidth": 1400,
    "maxWindowHeight": 300,
    "minWindowHeight": 200,
    "excludeFromMissions": false
  }]
}
```

## skills标签

该标签标识UIAbility组件或者ExtensionAbility组件能够接收的[Want](https://developer.harmonyos.com/cn/docs/documentation/doc-guides-V3/want-overview-0000001478340877-V3)的特征。

表7 skills标签说明

| 属性名称 | 含义                                                                                                                                                                                        | 数据类型   | 是否可缺省           |
| :------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | :--------- | :------------------- |
| actions  | 标识能够接收的Want的[Action值的集合](https://developer.harmonyos.com/cn/docs/documentation/doc-guides-V3/actions-entities-0000001477980937-V3)，取值通常为系统预定义的action值，也允许自定义。 | 字符串数组 | 可缺省，缺省值为空。 |
| entities | 标识能够接收Want的[Entity值的集合](https://developer.harmonyos.com/cn/docs/documentation/doc-guides-V3/actions-entities-0000001477980937-V3)。                                                 | 字符串数组 | 可缺省，缺省值为空。 |
| uris     | 标识与Want中URI（Uniform Resource Identifier）相匹配的集合。                                                                                                                                | 对象数组   | 可缺省，缺省值为空。 |

表8 uris对象内部结构说明

| 属性名称 | 含义                                                                                                                        | 数据类型  | 是否可缺省                                                                                                                                                                                                                                       |
| :------- | :-------------------------------------------------------------------------------------------------------------------------- | :-------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| scheme   | 标识URI的协议名部分，常见的有http、https、file、ftp等。                                                                     | 字符串    | uris中仅配置type时可以缺省，缺省值为空，否则不可缺省。                                                                                                                                                                                           |
| host     | 标识URI的主机地址部分，该字段要在schema存在时才有意义。常见的方式：- 域名方式，如example.com。- IP地址方式，如10.10.10.1。  | 字符串    | 可缺省，缺省值为空。                                                                                                                                                                                                                             |
| port     | 标识URI的端口部分。如http默认端口为80，https默认端口是443，ftp默认端口是21。该字段要在schema和host都存在时才有意义。        | 字符串    | 可缺省，缺省值为空。                                                                                                                                                                                                                             |
| path     | pathStartWith                                                                                                               | pathRegex | 标识URI的路径部分，path、pathStartWith和pathRegex配置时三选一。path标识URI与want中的路径部分全匹配，pathStartWith标识URI与want中的路径部分允许前缀匹配，pathRegex标识URI与want中的路径部分允许正则匹配。该字段要在schema和host都存在时才有意义。 |
| type     | 标识与Want相匹配的数据类型，使用MIME（Multipurpose Internet Mail Extensions）类型规范。可与schema同时配置，也可以单独配置。 | 字符串    | 可缺省，缺省值为空。                                                                                                                                                                                                                             |

skills示例：

```
{
  "abilities": [
    {
      "skills": [
        {
          "actions": [
            "ohos.want.action.home"
          ],
          "entities": [
            "entity.system.home"
          ],
          "uris": [
            {
              "scheme":"http",
              "host":"example.com",
              "port":"80",
              "path":"path",
              "type": "text/*"
            }
          ]
        }
      ]
    }
  ]
}
```

## extensionAbilities标签

描述extensionAbilities的配置信息，标签值为数组类型，该标签下的配置只对当前extensionAbilities生效。

表9 extensionAbilities标签说明

| 属性名称                                                                                                                                                                            | 含义                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | 数据类型   | 是否可缺省                    |
| :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :--------- | :---------------------------- |
| name                                                                                                                                                                                | 标识当前ExtensionAbility组件的名称，标签值最大长度为127个字节，该名称在整个应用要唯一。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | 字符串     | 该标签不可缺省。              |
| srcEntry                                                                                                                                                                            | 标识当前ExtensionAbility组件所对应的代码路径，标签值最大长度为127字节。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | 字符串     | 该标签不可缺省。              |
| description                                                                                                                                                                         | 标识当前ExtensionAbility组件的描述，标签值最大长度为255字节，标签也可以是描述内容的资源索引，用于支持多语言。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | 字符串     | 该标签可缺省，缺省值为空。    |
| icon                                                                                                                                                                                | 标识当前ExtensionAbility组件的图标，标签值为资源文件的索引。如果ExtensionAbility组件被配置为MainElement，该标签必须配置。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | 字符串     | 该标签可缺省，缺省值为空。    |
| label                                                                                                                                                                               | 标识当前ExtensionAbility组件对用户显示的名称，标签值配置为该名称的资源索引以支持多语言。说明：- 如果ExtensionAbility被配置当前Module的mainElement时，该标签必须配置，且应用内唯一。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | 字符串     | 该标签不可缺省。              |
| type                                                                                                                                                                                | 标识当前ExtensionAbility组件的类型，取值为：- form：卡片的ExtensionAbility。- workScheduler：延时任务的ExtensionAbility。- inputMethod：输入法的ExtensionAbility。- service：后台运行的service组件。- accessibility：辅助能力的ExtensionAbility。- dataShare：数据共享的ExtensionAbility。- fileShare：文件共享的ExtensionAbility。- staticSubscriber：静态广播的ExtensionAbility。- wallpaper：壁纸的ExtensionAbility。- backup：数据备份的ExtensionAbility。- window：该ExtensionAbility会在启动过程中创建一个window，为开发者提供界面开发。开发者开发出来的界面将通过abilityComponent控件组合到其他应用的窗口中。- thumbnail：获取文件缩略图的ExtensionAbility，开发者可以对自定义文件类型的文件提供缩略。- preview：该ExtensionAbility会将文件解析后在一个窗口中显示，开发者可以通过将此窗口组合到其他应用窗口中。说明：- 其中service和dataShare类型，仅支持系统应用配置，三方应用配置不生效。 | 字符串     | 该标签不可缺省。              |
| permissions                                                                                                                                                                         | 标识当前ExtensionAbility组件自定义的权限信息。当其他应用访问该ExtensionAbility时，需要申请相应的权限信息。一个数组元素为一个权限名称。通常采用反向域名格式（最大255字节），可以是系统预定义的权限，也可以是该应用自定义的权限。如果是后者，需与defPermissions标签中定义的某个权限的name标签值一致。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | 字符串数组 | 该标签可缺省，缺省值为空。    |
| uri                                                                                                                                                                                 | 标识当前ExtensionAbility组件提供的数据URI，为字符数组类型（最大长度255），用反向域名的格式表示。说明：- 该标签在type为dataShare类型的ExtensionAbility时，不可缺省。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | 字符串     | 该标签可缺省，缺省值为空。    |
| skills                                                                                                                                                                              | 标识当前ExtensionAbility组件能够接收的[Want](https://developer.harmonyos.com/cn/docs/documentation/doc-guides-V3/want-overview-0000001478340877-V3)的特征集，为数组格式。配置规则：entry包可以配置多个具有入口能力的skills标签（配置了ohos.want.action.home和entity.system.home）的ExtensionAbility，其中第一个配置了skills标签的ExtensionAbility中的label和icon作为应用或服务的label和icon。说明：- 应用的Feature包可以配置具有入口能力的skills标签。- 服务的Feature包不能配置具有入口能力的skills标签。                                                                                                                                                                                                                                                                                                                                                                                             | 数组       | 该标签可缺省，缺省值为空。    |
| [metadata](https://developer.harmonyos.com/cn/docs/documentation/doc-guides-V3/module-configuration-file-0000001427744540-V3#ZH-CN_TOPIC_0000001573929365__metadata%E6%A0%87%E7%AD%BE) | 标识当前ExtensionAbility组件的元信息。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | 对象       | 该标签可缺省，缺省值为空。    |
| exported                                                                                                                                                                            | 标识当前ExtensionAbility组件是否可以被其他应用调用，为布尔类型。- true：表示可以被其他应用调用。- false：表示不可以被其他应用调用。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | 布尔值     | 该标签可缺省，缺省值为false。 |

extensionAbilities示例：

```
{
  "extensionAbilities": [
    {
      "name": "FormName",
      "srcEntry": "./form/MyForm.ts",
      "icon": "$media:icon",
      "label" : "$string:extension_name",
      "description": "$string:form_description",
      "type": "form", 
      "permissions": ["ohos.abilitydemo.permission.PROVIDER"],
      "readPermission": "",
      "writePermission": "",
      "exported": true,
      "uri":"scheme://authority/path/query",
      "skills": [{
        "actions": [],
        "entities": [],
        "uris": []
      }],
      "metadata": [
        {
          "name": "ohos.extension.form",
          "resource": "$profile:form_config", 
        }
      ]
    }
  ]
}
```

## requestPermissions标签

该标签标识应用运行时需向系统申请的权限集合。

说明

* 在requestPermissions标签中配置的权限项将在应用级别生效，即该权限适用于整个应用程序。
* 如果应用需要订阅自己发布的事件，而且应用在extensionAbilities标签中的permissions字段中设置了访问该应用所需要的权限，那么应用也需要在requestPermissions标签中注册相关权限才能收到该事件。

表10 requestPermissions标签说明

| 属性      | 含义                                                                                                                                                                                                                                       | 类型                                                                 | 取值范围                                                                                    | 默认值                    |
| :-------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------- | :------------------------------------------------------------------------------------------ | :------------------------ |
| name      | 必须，填写需要使用的权限名称。                                                                                                                                                                                                             | 字符串                                                               | 自定义。                                                                                    | 无。                      |
| reason    | 可选，当申请的权限为user_grant权限时此字段必填，用于描述申请权限的原因。说明：- 当申请的权限为user_grant权限时，如果未填写该字段则不允许在应用市场上架，并且需要进行多语种适配。                                                           | 字符串                                                               | 使用string类资源引用。格式为$string: *。                                                    | 空。                      |
| usedScene | 可选，当申请的权限为user_grant权限时此字段必填。描述权限使用的场景由abilities和when组成。其中abilities可以配置为多个UIAbility组件，when表示调用时机。说明：- 默认为可选，当申请的权限为user_grant权限时，abilities标签必填，when标签可选。 | abilities：UIAbility或者ExtensionAbility名称的字符串数组when：字符串 | abilities：UIAbility或者ExtensionAbility组件的名称。when：inuse（使用时）、always（始终）。 | abilities：空。when：空。 |

requestPermissions示例：

```
{
  "module" : {
    "requestPermissions": [
      {
        "name": "ohos.abilitydemo.permission.PROVIDER",
        "reason": "$string:reason",
        "usedScene": {
          "abilities": [
            "EntryFormAbility"
          ],
          "when": "inuse"
        }
      }
    ]
  }
}
```

## shortcuts标签

shortcuts标识应用的快捷方式信息。标签值为数组，最多可以配置四个快捷方式。其包含四个子标签shortcutId、label、icon、wants。

metadata中指定shortcut信息，其中：

* name：指定shortcuts的名称。使用ohos.ability.shortcuts作为shortcuts信息的标识。
* resource：指定shortcuts信息的资源位置。

表11 shortcuts标签说明

| 属性                                                                                                        | 含义                                                                                                                                                                                               | 类型   | 默认值                     |
| :---------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :----- | :------------------------- |
| shortcutId                                                                                                  | 标识快捷方式的ID。字符串的最大长度为63字节。                                                                                                                                                       | 字符串 | 该标签不可缺省。           |
| label                                                                                                       | 标识快捷方式的标签信息，即快捷方式对外显示的文字描述信息。取值可以是描述性内容，也可以是标识label的资源索引。字符串最大长度为255字节。                                                             | 字符串 | 该标签可缺省，缺省值为空。 |
| icon                                                                                                        | 标识快捷方式的图标，标签值为资源文件的索引。                                                                                                                                                       | 字符串 | 该标签可缺省，缺省值为空。 |
| [wants](https://developer.harmonyos.com/cn/docs/documentation/doc-guides-V3/want-overview-0000001478340877-V3) | 标识快捷方式内定义的目标wants信息集合，每个wants可配置bundleName和abilityName两个子标签。bundleName：表示快捷方式的目标Bundle名称，字符串类型。abilityName：表示快捷方式的目标组件名，字符串类型。 | 对象   | 该标签可缺省，缺省为空。   |

1. 在/resource/base/profile/目录下配置shortcuts_config.json配置文件。

```
{
  "shortcuts": [
    {
      "shortcutId": "id_test1",
      "label": "$string:shortcut",
      "icon": "$media:aa_icon",
      "wants": [
        {
          "bundleName": "com.ohos.hello",
          "abilityName": "EntryAbility"
        }
      ]
    }
  ]
}
```

2. 在module.json5配置文件的abilities标签中，针对需要添加快捷方式的UIAbility进行配置metadata标签，使shortcut配置文件对该UIAbility生效。

```
{
  "module": {
    // ...
    "abilities": [
      {
        "name": "EntryAbility",
        "srcEntry": "./ets/entryability/EntryAbility.ts",
        // ...
        "skills": [
          {
            "entities": [
              "entity.system.home"
            ],
            "actions": [
              "ohos.want.action.home"
            ]
          }
        ],
        "metadata": [
          {
            "name": "ohos.ability.shortcuts",
            "resource": "$profile:shortcuts_config"
          }
        ]
      }
    ]
  }
}
```

## distroFilter标签

该标签下的子标签均为可选字段，在应用市场云端分发时使用，distroFilter标签用于定义HAP对应的细分设备规格的分发策略，以便在应用市场进行云端分发应用包时做精准匹配。该标签可配置的分发策略维度包括API Version、屏幕形状、屏幕尺寸、屏幕分辨率，设备的国家与地区码。在进行分发时，通过deviceType与这五个属性的匹配关系，唯一确定一个用于分发到设备的HAP。

该标签需要配置在/resource/profile资源目录下，并在模块的metadata的resource字段中引用。

表12 distroFilter标签说明

| 属性名称      | 含义                                                                                   | 数据类型 | 是否可缺省                 |
| :------------ | :------------------------------------------------------------------------------------- | :------- | :------------------------- |
| apiVersion    | 标识支持的apiVersion范围。                                                             | 对象数组 | 该标签可缺省，缺省值为空。 |
| screenShape   | 标识屏幕形状的支持策略。                                                               | 对象数组 | 该标签可缺省，缺省值为空。 |
| screenWindow  | 标识应用运行时窗口的分辨率支持策略。该字段仅支持对轻量级智能穿戴设备进行配置。         | 对象数组 | 该标签可缺省，缺省值为空。 |
| screenDensity | 标识屏幕的像素密度（dpi：Dot Per Inch）。                                              | 对象数组 | 该标签可缺省，缺省值为空。 |
| countryCode   | 表示应用需要分发的国家地区码，具体值以ISO-3166-1标准为准。支持多个国家和地区枚举定义。 | 对象数组 | 该标签可缺省，缺省值为空。 |

表13 screenShape对象的内部结构

| 属性名称 | 含义                                                                                                                           | 数据类型   | 是否可缺省       |
| :------- | :----------------------------------------------------------------------------------------------------------------------------- | :--------- | :--------------- |
| policy   | 标识该子属性取值规则。配置为“exclude”或“include”。- exclude：表示需要排除的value属性。- include：表示需要包含的value属性。 | 字符串     | 该标签不可缺省。 |
| value    | 支持的取值为circle（圆形）、rect（矩形）。场景示例：针对智能穿戴设备，可为圆形表盘和矩形表盘分别提供不同的HAP。                | 字符串数组 | 该标签不可缺省。 |

表14 screenWindow对象的内部结构说明

| 属性名称 | 含义                                                                                                                                                                                 | 数据类型   | 是否可缺省       |
| :------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :--------- | :--------------- |
| policy   | 标识该子属性取值规则。配置为“exclude”或“include”。- exclude：表示该字段取值不包含value枚举值匹配规则的匹配该属性。- include：表示该字段取值满足value枚举值匹配规则的匹配该属性。 | 字符串     | 该标签不可缺省。 |
| value    | 单个字符串的取值格式为“宽 * 高”，取值为整数像素值，例如“454 * 454”。                                                                                                             | 字符串数组 | 该标签不可缺省。 |

表15 screenDensity对象的内部结构说明

| 属性名称 | 含义                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | 数据类型   | 是否可缺省       |
| :------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :--------- | :--------------- |
| policy   | 标识该子属性取值规则。配置为“exclude”或“include”。- exclude：表示需要排除的value属性。- include：表示需要包含的value属性。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | 字符串     | 该标签不可缺省。 |
| value    | 该标签标识屏幕的像素密度（dpi :Dot Per Inch）。该标签为字符串数组，字符串范围如下。- sdpi：表示小规模的屏幕密度（Small-scale Dots per Inch），适用于dpi取值为(0,120]的设备。- mdpi：表示中规模的屏幕密度（Medium-scale Dots Per Inch），适用于dpi取值为(120,160]的设备。- ldpi：表示大规模的屏幕密度（Large-scale Dots Per Inch），适用于dpi取值为(160,240]的设备。- xldpi：表示大规模的屏幕密度（Extra Large-scale Dots Per Inch），适用于dpi取值为(240,320]的设备。- xxldpi：表示大规模的屏幕密度（Extra Extra Large-scale Dots Per Inch），适用于dpi取值为(320，480]的设备。- xxxldpi：表示大规模的屏幕密度（Extra Extra Extra Large-scale Dots Per Inch），适用于dpi取值为(480, 640]的设备。 | 字符串数组 | 该标签不可缺省。 |

表16 countryCode对象的内部结构说明

| 属性名称 | 含义                                                                                                                           | 数据类型   | 是否可缺省       |
| :------- | :----------------------------------------------------------------------------------------------------------------------------- | :--------- | :--------------- |
| policy   | 标识该子属性取值规则。配置为“exclude”或“include”。- exclude：表示需要排除的value属性。- include：表示需要包含的value属性。 | 字符串     | 该标签不可缺省。 |
| value    | 标识应用需要分发的国家地区码。                                                                                                 | 字符串数组 | 该标签不可缺省。 |

在开发视图的resources/base/profile下面定义配置文件distro_filter_config.json，文件名可以自定义。

```
{
  "distroFilter": {
    "screenShape": {
      "policy": "include",
      "value": [
        "circle",
        "rect"
      ]
    },
    "screenWindow": {
      "policy": "include",
      "value": [
        "454*454",
        "466*466"
      ]
    },
    "screenDensity": {
      "policy": "exclude",
      "value": [
        "ldpi",
        "xldpi"
      ]
    },
    "countryCode": { // 支持中国和香港地区分发
      "policy": "include",
      "value": [
        "CN",
        "HK"
      ]
    }
  }
}
```

在module.json5配置文件的module标签中定义metadata信息。

```
{
  "module": {
    // ...
    "metadata": [
      {
        "name": "ohos.module.distro",
        "resource": "$profile:distro_filter_config",
      }
    ]
  }
}
```

## testRunner标签

此标签用于支持对测试框架的配置。

表17 testRunner标签说明

| 属性名称 | 含义                                                  | 数据类型 | 是否可缺省 |
| :------- | :---------------------------------------------------- | :------- | :--------- |
| name     | 标识测试框架对象名称。该标签最大字节长度为255个字节。 | 字符串   | 不可缺省。 |
| srcPath  | 标识测试框架代码路径。该标签最大字节长度为255个字节。 | 字符串   | 不可缺省。 |

testRunner标签示例：

```
{
  "module": {
    // ...
    "testRunner": {
      "name": "myTestRunnerName",
      "srcPath": "etc/test/TestRunner.ts"
    }
  }
}
```
