# 构建第一个ArkTS应用（Stage模型）

更新时间: 2024-01-10 11:58

说明

为确保运行效果，本文以使用DevEco Studio 3.1 Release版本为例，点击[此处](https://developer.harmonyos.com/cn/develop/deveco-studio)获取下载链接。

## 创建ArkTS工程

1. 若首次打开 DevEco Studio ，请点击Create Project创建工程。如果已经打开了一个工程，请在菜单栏选择File > New > Create Project来创建一个新工程。
2. 选择Application应用开发（本文以应用开发为例，[Atomic Service](https://developer.harmonyos.com/cn/docs/documentation/doc-guides-V3/glossary-0000000000029587-V3#section1679023922312)对应为元服务开发），选择模板"Empty Ability"，点击Next进行下一步配置。![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231204103829.68264296914249548523410996677829:50001231000000:2800:CF46B05C01DA6E900A26ADFFD274661B6E9D4C3413E849767170959D6C517D8A.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true "点击放大")
3. 进入配置工程界面，Compile SDK选择"3.1.0(API 9)"，Model 选择"Stage"，其他参数保持默认设置即可。![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231204103830.56937195470461305130020610826710:50001231000000:2800:1456FD1791EB9A53930630BAAF99CE42ABEB40EC3285803F3AA1F7CEC2FE7072.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true "点击放大")

  说明

  支持使用ArkTS[低代码开发](https://developer.harmonyos.com/cn/docs/documentation/doc-guides-V3/ide-low-code-overview-0000001480179573-V3)方式。

  低代码开发方式具有丰富的UI界面编辑功能，通过可视化界面开发方式快速构建布局，可有效降低开发者的上手成本并提升开发者构建UI界面的效率。

  如需使用低代码开发方式，请打开上图中的Enable Super Visual开关。
4. 点击 Finish ，工具会自动生成示例代码和相关资源，等待工程创建完成。

## ArkTS工程目录结构（Stage模型）

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231204103830.91674512477950015833579106873574:50001231000000:2800:C039B713D6D0D5C3254471AC0CF229A0AA137568E35330B4CC6FB0250AD98480.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)

* AppScope > app.json5 ：应用的全局配置信息。
* entry ：HarmonyOS工程模块，编译构建生成一个HAP包。
  * src > main > ets ：用于存放ArkTS源码。
  * src > main > ets > entryability ：应用/服务的入口。
  * src > main > ets > pages ：应用/服务包含的页面。
  * src > main > resources ：用于存放应用/服务所用到的资源文件，如图形、多媒体、字符串、布局文件等。关于资源文件，详见[资源分类与访问](https://developer.harmonyos.com/cn/docs/documentation/doc-guides-V3/resource-categories-and-access-0000001711674888-V3)。
  * src > main > module.json5 ：Stage模型模块配置文件。主要包含HAP包的配置信息、应用/服务在具体设备上的配置信息以及应用/服务的全局配置信息。具体的配置文件说明，详见[module.json5配置文件](https://developer.harmonyos.com/cn/docs/documentation/doc-guides-V3/module-configuration-file-0000001427744540-V3)。
  * build-profile.json5 ：当前的模块信息、编译信息配置项，包括buildOption、targets配置等。其中targets中可配置当前运行环境，默认为HarmonyOS。
  * hvigorfile.ts ：模块级编译构建任务脚本，开发者可以自定义相关任务和代码实现。
* oh_modules ：用于存放三方库依赖信息。关于原npm工程适配ohpm操作，请参考[历史工程迁移](https://developer.harmonyos.com/cn/docs/documentation/doc-guides-V3/project_overview-0000001053822398-V3#section167081936119)。
* build-profile.json5 ：应用级配置信息，包括签名、产品配置等。
* hvigorfile.ts ：应用级编译构建任务脚本。

## 构建第一个页面

1. 使用文本组件。
  工程同步完成后，在"Project"窗口，点击"entry > src > main > ets > pages"，打开"Index.ets"文件，可以看到页面由Text组件组成。"Index.ets"文件的示例如下：

```
  // Index.ets
  @Entry
  @Component
  struct Index {
    @State message: string = 'Hello World'

    build() {
     Row() {
      Column() {
        Text(this.message)
         .fontSize(50)
         .fontWeight(FontWeight.Bold)
      }
      .width('100%')
     }
     .height('100%')
    }
  }
```
2. 添加按钮。
  在默认页面基础上，我们添加一个Button组件，作为按钮响应用户点击，从而实现跳转到另一个页面。"Index.ets"文件的示例如下：

```
  // Index.ets
  @Entry
  @Component
  struct Index {
    @State message: string = 'Hello World'

    build() {
     Row() {
      Column() {
        Text(this.message)
         .fontSize(50)
         .fontWeight(FontWeight.Bold)
        // 添加按钮，以响应用户点击
        Button() {
         Text('Next')
          .fontSize(30)
          .fontWeight(FontWeight.Bold)
        }
        .type(ButtonType.Capsule)
        .margin({
         top: 20
        })
        .backgroundColor('#0D9FFB')
        .width('40%')
        .height('5%')
      }
      .width('100%')
     }
     .height('100%')
    }
  }
```
3. 在编辑窗口右上角的侧边工具栏，点击Previewer，打开预览器。第一个页面效果如下图所示：
  ![img](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231204103830.38860359849368730928440125945618:50001231000000:2800:93509CB7EEDE6896036A8604191D79C431A573AB3C7B2764632640CB5E6810E8.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)

## 构建第二个页面

1. 创建第二个页面。

* 新建第二个页面文件。在"Project"窗口，打开"entry > src > main > ets"，右键点击“pages"文件夹，选择"New > ArkTS File"，命名为"Second"，点击"Finish"。可以看到文件目录结构如下：
  ![img](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231204103830.93838538522283941620962761967458:50001231000000:2800:E3493B81829D8107D105519B46E7EFEAFF36DF4A5866F9FAC97D3C11735D0185.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)

  说明

  开发者也可以在右键点击"pages"文件夹时，选择"New > Page"，则无需手动配置相关页面路由。
* 配置第二个页面的路由。在"Project"窗口，打开"entry > src > main > resources > base > profile"，在main_pages.json文件中的“src”下配置第二个页面的路由“pages/Second”。示例如下：

```
  {
    "src": [
      "pages/Index",
      "pages/Second"
    ]
  }
```
2. 添加文本及按钮。
  参照第一个页面，在第二个页面添加Text组件、Button组件等，并设置其样式。"Second.ets"文件的示例如下：

```
  // Second.ets
  @Entry
  @Component
  struct Second {
    @State message: string = 'Hi there'

    build() {
     Row() {
      Column() {
        Text(this.message)
         .fontSize(50)
         .fontWeight(FontWeight.Bold)
        Button() {
         Text('Back')
          .fontSize(25)
          .fontWeight(FontWeight.Bold)
        }
        .type(ButtonType.Capsule)
        .margin({
         top: 20
        })
        .backgroundColor('#0D9FFB')
        .width('40%')
        .height('5%')
      }
      .width('100%')
     }
     .height('100%')
    }
  }
```

## 实现页面间的跳转

页面间的导航可以通过[页面路由router](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/js-apis-router-0000001478061893-V3)来实现。页面路由router根据页面url找到目标页面，从而实现跳转。使用页面路由请导入router模块。

1. 第一个页面跳转到第二个页面。
  在第一个页面中，跳转按钮绑定onClick事件，点击按钮时跳转到第二页。"Index.ets"文件的示例如下：

```
  // Index.ets
  // 导入页面路由模块
  import router from '@ohos.router';

  @Entry
  @Component
  struct Index {
    @State message: string = 'Hello World'

    build() {
     Row() {
      Column() {
        Text(this.message)
         .fontSize(50)
         .fontWeight(FontWeight.Bold)
        // 添加按钮，以响应用户点击
        Button() {
         Text('Next')
          .fontSize(30)
          .fontWeight(FontWeight.Bold)
        }
        .type(ButtonType.Capsule)
        .margin({
         top: 20
        })
        .backgroundColor('#0D9FFB')
        .width('40%')
        .height('5%')
        // 跳转按钮绑定onClick事件，点击时跳转到第二页
        .onClick(() => {
         console.info(`Succeeded in clicking the 'Next' button.`)
         // 跳转到第二页
         router.pushUrl({ url: 'pages/Second' }).then(() => {
          console.info('Succeeded in jumping to the second page.')
         }).catch((err) => {
          console.error(`Failed to jump to the second page.Code is ${err.code}, message is ${err.message}`)
         })
        })
      }
      .width('100%')
     }
     .height('100%')
    }
  }
```
2. 第二个页面返回到第一个页面。
  在第二个页面中，返回按钮绑定onClick事件，点击按钮时返回到第一页。"Second.ets"文件的示例如下：

```
  // Second.ets
  // 导入页面路由模块
  import router from '@ohos.router';

  @Entry
  @Component
  struct Second {
    @State message: string = 'Hi there'

    build() {
     Row() {
      Column() {
        Text(this.message)
         .fontSize(50)
         .fontWeight(FontWeight.Bold)
        Button() {
         Text('Back')
          .fontSize(25)
          .fontWeight(FontWeight.Bold)
        }
        .type(ButtonType.Capsule)
        .margin({
         top: 20
        })
        .backgroundColor('#0D9FFB')
        .width('40%')
        .height('5%')
        // 返回按钮绑定onClick事件，点击按钮时返回到第一页
        .onClick(() => {
         console.info(`Succeeded in clicking the 'Back' button.`)
         try {
          // 返回第一页
          router.back()
          console.info('Succeeded in returning to the first page.')
         } catch (err) {
          console.error(`Failed to return to the first page.Code is ${err.code}, message is ${err.message}`)
         }
        })
      }
      .width('100%')
     }
     .height('100%')
    }
  }
```
3. 打开"Index.ets"文件，点击预览器中的![img](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231204103830.80177210997074142378298732691064:50001231000000:2800:5F53957F04DB629FA180B16DBC5D101B7F7EE959C1EDDCDC4DB7CA3D815D3DFB.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)按钮进行刷新。效果如下图所示：
  ![img](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231204103830.05932383015798000052028638197855:50001231000000:2800:56F19CC4EA6F00B0E06AF0D216A402F43AABBAFD9DA461439CEAE542008E3019.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)

## 使用真机运行应用

运行HarmonyOS应用可以使用远程模拟器和物理真机设备，区别在于使用远程模拟器运行应用不需要对应用进行签名。接下来将以物理真机设备为例，介绍HarmonyOS应用的运行方法，关于模拟器的使用请参考[使用Remote Emulator运行应用/服务](https://developer.harmonyos.com/cn/docs/documentation/doc-guides-V3/run_simulator-0000001053303709-V3)。

1. 将搭载HarmonyOS系统的真机与电脑连接。具体指导及要求，可查看[使用本地真机运行应用/服务](https://developer.harmonyos.com/cn/docs/documentation/doc-guides-V3/run_phone_tablat-0000001064774652-V3)。
2. 点击File > Project Structure... > Project > SigningConfigs界面勾选"Support HarmonyOS"和"Automatically generate signature"，点击界面提示的"Sign In"，使用华为帐号登录。等待自动签名完成后，点击"OK"即可。如下图所示：![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231204103830.80738181636006670897925102145759:50001231000000:2800:E5A5802DADED6EEF0E054151B8E49CF9C64377A0070D318508C2168D0E58A484.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true "点击放大")
3. 在编辑窗口右上角的工具栏，点击![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231204103830.07328505805358635903994656317959:50001231000000:2800:1D70B4D19BE7BF8C18F931169B6FDEA51DE3FDD63852C04B78A26CAED1FA6C50.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)按钮运行。效果如下图所示：![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231204103830.85056018715974776567635363562400:50001231000000:2800:2541F6AC14755F6FAB1CAE63E881DA0991C9C12CDD093B5FF2ACE9A54796BD5E.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true "点击放大")

恭喜您已经使用ArkTS语言开发（Stage模型）完成了第一个HarmonyOS应用，快来探索更多的HarmonyOS功能吧。

