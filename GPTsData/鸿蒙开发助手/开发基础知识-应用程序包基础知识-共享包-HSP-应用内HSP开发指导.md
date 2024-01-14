# 应用内HSP开发指导

更新时间: 2024-01-10 11:30

应用内HSP指的是专门为某一应用开发的HSP，只能被该应用内部其他HAP/HSP使用，用于应用内部代码、资源的共享。

应用内HSP跟随其宿主应用的APP包一起发布，与该宿主应用具有相同的包名和生命周期。

## 开发应用内HSP

HSP模块可以在DevEco Studio中由[指定模板创建](https://developer.harmonyos.com/cn/docs/documentation/doc-guides-V3/hsp-0000001521396322-V3)，我们以创建一个名为library的HSP模块为例。基本的工程目录结构大致如下：

```
library
├── src
│   └── main
│       ├── ets
│       │   ├── pages
│       │   └── index.ets
│       ├── resources
│       └── module.json5
└── oh-package.json5
```

模块module.json5中的"type"标识模块类型，HSP的"type"是"shared"。

```
{
    "type": "shared"
}
```

HSP通过在入口文件中导出接口，对外提供能力。入口文件在模块oh-package.json5的"main"中配置。例如：

```
{
    "main": "./src/main/ets/index.ets"
}
```

### 导出ts类和方法

通过export导出ts类和方法，例如：

```
// library/src/main/ets/utils/test.ts
export class Log {
    static info(msg) {
        console.info(msg);
    }
}

export function add(a: number, b: number) {
  return a + b;
}

export function minus(a: number, b: number) {
  return a - b;
}
```

对外暴露的接口，需要在入口文件index.ets中声明：

```
// library/src/main/ets/index.ets
export { Log, add, minus } from './utils/test'
```

### 导出ArkUI组件

ArkUI组件也可以通过export导出，例如：

```
// library/src/main/ets/components/MyTitleBar.ets
@Component
export struct MyTitleBar {
  build() {
    Row() {
      Text($r('app.string.library_title'))
        .fontColor($r('app.color.white'))
        .fontSize(25)
        .margin({left:15})
    }
    .width('100%')
    .height(50)
    .padding({left:15})
    .backgroundColor('#0D9FFB')
  }
}
```

对外暴露的接口，需要在入口文件index.ets中声明：

```
// library/src/main/ets/index.ets
export { MyTitleBar } from './components/MyTitleBar'
```

**HSP中资源使用说明**

注意，在HSP中，通过$r/$rawfile可以使用本模块resources目录下的资源。

如果使用相对路径的方式，例如：

在HSP模块中使用Image("common/example.png")，实际上该Image组件访问的是HSP调用方（如entry）下的资源entry/src/main/ets/common/example.png。

### 导出native方法

在HSP中也可以包含C++编写的so。对于so中的native方法，HSP通过间接的方式导出，以导出libnative.so的乘法接口multi为例：

```
// ibrary/src/main/ets/utils/nativeTest.ts
import native from "libnative.so"

export function nativeMulti(a: number, b: number) {
    return native.multi(a, b);
}
```

对外暴露的接口，需要在入口文件index.ets中声明：

```
// library/src/main/ets/index.ets
export { nativeMulti } from './utils/nativeTest'
```

## 使用应用内HSP

要使用HSP中的接口，首先需要在使用方的oh-package.json5中配置对它的依赖。如果应用内HSP和使用方在同一工程下，可以直接本地引用，例如：

```
// entry/oh-package.json5
"dependencies": {
    "library": "file:../library"
}
```

然后就可以像使用HAR一样调用HSP的对外接口了。

例如，上面的library已经导出了下面这些接口：

```
// library/src/main/ets/index.ets
export { Log, add, minus } from './utils/test'
export { MyTitleBar } from './components/MyTitleBar'
export { nativeMulti } from './utils/nativeTest'
```

在使用方的代码中，可以这样使用：

```
// entry/src/main/ets/pages/index.ets
import { Log, add, MyTitleBar, nativeMulti } from "library"

@Entry
@Component
struct Index {
  @State message: string = 'Hello World'
  build() {
    Row() {
      Column() {
        MyTitleBar()
        Text(this.message)
          .fontSize(30)
          .fontWeight(FontWeight.Bold)
        Button('add(1, 2)')
          .onClick(()=>{
            Log.info("add button click!");
            this.message = "result: " + add(1, 2);
          })
        Button('nativeMulti(3, 4)')
          .onClick(()=>{
            Log.info("nativeMulti button click!");
            this.message = "result: " + nativeMulti(3, 4);
          })
      }
      .width('100%')
    }
    .height('100%')
  }
}
```

### 跨包页面路由跳转

若开发者想在entry模块中，添加一个按钮跳转至library模块中的menu页面（路径为：library/src/main/ets/pages/menu.ets），那么可以在使用方的代码（entry模块下的Index.ets，路径为：entry/src/main/ets/MainAbility/Index.ets）里这样使用：

```
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
            Text('click to menu')
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
        // 绑定点击事件
        .onClick(() => {
            router.pushUrl({
              url: '@bundle:com.example.hmservice/library/ets/pages/menu'
            }).then(() => {
              console.log("push page success");
            }).catch(err => {
              console.error(`pushUrl failed, code is ${err.code}, message is ${err.message}`);
            })
        })
      .width('100%')
    }
    .height('100%')
    }
  }
}
```

其中router.pushUrl方法的入参中url的内容为：

```
'@bundle:com.example.hmservice/library/ets/pages/menu'
```

url内容的模板为：

```
'@bundle:包名（bundleName）/模块名（moduleName）/路径/页面所在的文件名(不加.ets后缀)'
```

