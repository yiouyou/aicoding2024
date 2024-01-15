# 使用隐式Want打开网址

更新时间: 2024-01-15 12:22

## 前提条件

设备上安装了一个或多个浏览器。

浏览器应用中通过module.json5配置如下：

```
"skills": [
  {
    "entities": [
      "entity.system.browsable"
      // ...
    ],
    "actions": [
        "ohos.want.action.viewData"
        // ...
    ],
    "uris": [
      {
        "scheme": "https",
        "host": "www.test.com",
        "port": "8080",
        // prefix matching
        "pathStartWith": "query",
        "type": "text/*"
      },
      {
        "scheme": "http",
        // ...
      }
      // ...
    ]
  },
]
```

## 开发步骤

1. 在自定义函数implicitStartAbility内使用隐式Want启动Ability。

```
    async implicitStartAbility() {
        try {
            let want = {
                // uncomment line below if wish to implicitly query only in the specific bundle.
                // bundleName: "com.example.myapplication",
                "action": "ohos.want.action.viewData",
                // entities can be omitted.
                "entities": [ "entity.system.browsable" ],
                "uri": "https://www.test.com:8080/query/student",
                "type": "text/plain"
            }
            let context = getContext(this) as common.UIAbilityContext;
            await context.startAbility(want)
            console.info(`explicit start ability succeed`)
        } catch (error) {
            console.info(`explicit start ability failed with ${error.code}`)
        }
     }
```

  匹配过程如下：
  a. want内action不为空，且被skills内action包括，匹配成功。
  b. want内entities不为空，且被skills内entities包括，匹配成功。
  c. skills内uris拼接为[https://www.test.com:8080/query\](https://www.test. com:8080/query/)* (*为通配符)包含want内uri，匹配成功。
  d. want内type不为空，且被skills内type包含，匹配成功。
2. 当有多个匹配应用时，会被应用选择器展示给用户进行选择。
  ![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231121183826.33983711079055035785122152254165:50001231000000:2800:91CDA924E084855AC790113BE5E0BBFE211CD60D9F067A191EA29B1C01318EA5.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)

