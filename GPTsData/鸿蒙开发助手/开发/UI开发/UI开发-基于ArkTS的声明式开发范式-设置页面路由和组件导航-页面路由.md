# 页面路由（router）

更新时间: 2024-01-10 11:31

页面路由指在应用程序中实现不同页面之间的跳转和数据传递。HarmonyOS提供了Router模块，通过不同的url地址，可以方便地进行页面路由，轻松地访问不同的页面。本文将从[页面跳转](https://developer.harmonyos.com/cn/docs/documentation/doc-guides-V3/arkts-routing-0000001503325125-V3#section6414655195312)、[页面返回](https://developer.harmonyos.com/cn/docs/documentation/doc-guides-V3/arkts-routing-0000001503325125-V3#ZH-CN_TOPIC_0000001523968678__%E9%A1%B5%E9%9D%A2%E8%BF%94%E5%9B%9E)和[页面返回前增加一个询问框](https://developer.harmonyos.com/cn/docs/documentation/doc-guides-V3/arkts-routing-0000001503325125-V3#ZH-CN_TOPIC_0000001523968678__%E9%A1%B5%E9%9D%A2%E8%BF%94%E5%9B%9E%E5%89%8D%E5%A2%9E%E5%8A%A0%E4%B8%80%E4%B8%AA%E8%AF%A2%E9%97%AE%E6%A1%86)几个方面介绍Router模块提供的功能。

## 页面跳转

页面跳转是开发过程中的一个重要组成部分。在使用应用程序时，通常需要在不同的页面之间跳转，有时还需要将数据从一个页面传递到另一个页面。

图1 页面跳转
![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231121183905.73177245914949934193787529304382:50001231000000:2800:503A6766708ADAB864585E3F4E77E1421222401D579D3CC78FBFCBE3F7C96221.gif?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true "点击放大")

Router模块提供了两种跳转模式，分别是[router.pushUrl()](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/js-apis-router-0000001478061893-V3#ZH-CN_TOPIC_0000001523808578__routerpushurl9)和[router.replaceUrl()](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/js-apis-router-0000001478061893-V3#ZH-CN_TOPIC_0000001523808578__routerreplaceurl9)。这两种模式决定了目标页是否会替换当前页。

* router.pushUrl()：目标页不会替换当前页，而是压入页面栈。这样可以保留当前页的状态，并且可以通过返回键或者调用[router.back()](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/js-apis-router-0000001478061893-V3#ZH-CN_TOPIC_0000001523808578__routerback)方法返回到当前页。
* router.replaceUrl()：目标页会替换当前页，并销毁当前页。这样可以释放当前页的资源，并且无法返回到当前页。

说明

页面栈的最大容量为32个页面。如果超过这个限制，可以调用[router.clear()](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/js-apis-router-0000001478061893-V3#ZH-CN_TOPIC_0000001523808578__routerclear)方法清空历史页面栈，释放内存空间。

同时，Router模块提供了两种实例模式，分别是Standard和Single。这两种模式决定了目标url是否会对应多个实例。

* Standard：标准实例模式，也是默认情况下的实例模式。每次调用该方法都会新建一个目标页，并压入栈顶。
* Single：单实例模式。即如果目标页的url在页面栈中已经存在同url页面，则离栈顶最近的同url页面会被移动到栈顶，并重新加载；如果目标页的url在页面栈中不存在同url页面，则按照标准模式跳转。

在使用页面路由Router相关功能之前，需要在代码中先导入Router模块。

```
import router from '@ohos.router';
```

* 场景一：有一个主页（Home）和一个详情页（Detail），希望从主页点击一个商品，跳转到详情页。同时，需要保留主页在页面栈中，以便返回时恢复状态。这种场景下，可以使用pushUrl()方法，并且使用Standard实例模式（或者省略）。

```
// 在Home页面中
function onJumpClick(): void {
  router.pushUrl({
    url: 'pages/Detail' // 目标url
  }, router.RouterMode.Standard, (err) => {
    if (err) {
      console.error(`Invoke pushUrl failed, code is ${err.code}, message is ${err.message}`);
      return;
    }
    console.info('Invoke pushUrl succeeded.');
  });
}
```

  说明

  标准实例模式下，router.RouterMode.Standard参数可以省略。
* 场景二：有一个登录页（Login）和一个个人中心页（Profile），希望从登录页成功登录后，跳转到个人中心页。同时，销毁登录页，在返回时直接退出应用。这种场景下，可以使用replaceUrl()方法，并且使用Standard实例模式（或者省略）。

```
// 在Login页面中
function onJumpClick(): void {
  router.replaceUrl({
    url: 'pages/Profile' // 目标url
  }, router.RouterMode.Standard, (err) => {
    if (err) {
      console.error(`Invoke replaceUrl failed, code is ${err.code}, message is ${err.message}`);
      return;
    }
    console.info('Invoke replaceUrl succeeded.');
  })
}
```

  说明

  标准实例模式下，router.RouterMode.Standard参数可以省略。
* 场景三：有一个设置页（Setting）和一个主题切换页（Theme），希望从设置页点击主题选项，跳转到主题切换页。同时，需要保证每次只有一个主题切换页存在于页面栈中，在返回时直接回到设置页。这种场景下，可以使用pushUrl()方法，并且使用Single实例模式。

```
// 在Setting页面中
function onJumpClick(): void {
  router.pushUrl({
    url: 'pages/Theme' // 目标url
  }, router.RouterMode.Single, (err) => {
    if (err) {
      console.error(`Invoke pushUrl failed, code is ${err.code}, message is ${err.message}`);
      return;
    }
    console.info('Invoke pushUrl succeeded.');
  });
}
```
* 场景四：有一个搜索结果列表页（SearchResult）和一个搜索结果详情页（SearchDetail），希望从搜索结果列表页点击某一项结果，跳转到搜索结果详情页。同时，如果该结果已经被查看过，则不需要再新建一个详情页，而是直接跳转到已经存在的详情页。这种场景下，可以使用replaceUrl()方法，并且使用Single实例模式。

```
// 在SearchResult页面中
function onJumpClick(): void {
  router.replaceUrl({
    url: 'pages/SearchDetail' // 目标url
  }, router.RouterMode.Single, (err) => {
    if (err) {
      console.error(`Invoke replaceUrl failed, code is ${err.code}, message is ${err.message}`);
      return;
    }
    console.info('Invoke replaceUrl succeeded.');})
}
```

以上是不带参数传递的场景。

如果需要在跳转时传递一些数据给目标页，则可以在调用Router模块的方法时，添加一个params属性，并指定一个对象作为参数。例如：

```
class DataModelInfo {
  age: number;
}

class DataModel {
  id: number;
  info: DataModelInfo;
}

function onJumpClick(): void {
  // 在Home页面中
  let paramsInfo: DataModel = {
    id: 123,
    info: {
      age: 20
    }
  };

  router.pushUrl({
    url: 'pages/Detail', // 目标url
    params: paramsInfo // 添加params属性，传递自定义参数
  }, (err) => {
    if (err) {
      console.error(`Invoke pushUrl failed, code is ${err.code}, message is ${err.message}`);
      return;
    }
    console.info('Invoke pushUrl succeeded.');
  })
}
```

在目标页中，可以通过调用Router模块的[getParams()](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/js-apis-router-0000001478061893-V3#ZH-CN_TOPIC_0000001523808578__routergetparams)方法来获取传递过来的参数。例如：

```
const params = router.getParams(); // 获取传递过来的参数对象
const id = params['id']; // 获取id属性的值
const age = params['info'].age; // 获取age属性的值
```

## 页面返回

当用户在一个页面完成操作后，通常需要返回到上一个页面或者指定页面，这就需要用到页面返回功能。在返回的过程中，可能需要将数据传递给目标页，这就需要用到数据传递功能。

图2 页面返回
![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231121183906.98169907922746313941789656678279:50001231000000:2800:750DFB10201E55052720342F37DD77D813F5AFEE19EB5B6EAFC6262F5A8144F4.gif?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true "点击放大")

在使用页面路由Router相关功能之前，需要在代码中先导入Router模块。

<pre class="ts prettyprint linenums hljs typescript"><div class="sun"></div><div class="copybtn"></div><ol class="linenums"><li><p>import router from '@ohos.router';</p></li></ol></pre>

可以使用以下几种方式进行页面返回：

* 方式一：返回到上一个页面。

```
import router from '@ohos.router';
```

  这种方式会返回到上一个页面，即上一个页面在页面栈中的位置。但是，上一个页面必须存在于页面栈中才能够返回，否则该方法将无效。
* 方式二：返回到指定页面。

```
router.back();
```

  这种方式可以返回到指定页面，需要指定目标页的路径。目标页必须存在于页面栈中才能够返回。
* 方式三：返回到指定页面，并传递自定义参数信息。

```
router.back({
  url: 'pages/Home',
  params: {
    info: '来自Home页'
  }
});
```

  这种方式不仅可以返回到指定页面，还可以在返回的同时传递自定义参数信息。这些参数信息可以在目标页中通过调用router.getParams()方法进行获取和解析。

在目标页中，在需要获取参数的位置调用router.getParams()方法即可，例如在[onPageShow()生命周期](https://developer.harmonyos.com/cn/docs/documentation/doc-guides-V3/arkts-page-custom-components-lifecycle-0000001524296665-V3)回调中：

```
onPageShow() {
  const params = router.getParams(); // 获取传递过来的参数对象
  const info = params['info']; // 获取info属性的值
}
```

说明

当使用router.back()方法返回到指定页面时，该页面会被重新压入栈顶，而原栈顶页面（包括）到指定页面（不包括）之间的所有页面栈都将被销毁。

另外，如果使用router.back()方法返回到原来的页面，原页面不会被重复创建，因此使用@State声明的变量不会重复声明，也不会触发页面的aboutToAppear()生命周期回调。如果需要在原页面中使用返回页面传递的自定义参数，可以在需要的位置进行参数解析。例如，在onPageShow()生命周期回调中进行参数解析。

## 页面返回前增加一个询问框

在开发应用时，为了避免用户误操作或者丢失数据，有时候需要在用户从一个页面返回到另一个页面之前，弹出一个询问框，让用户确认是否要执行这个操作。

本文将从[系统默认询问框](https://developer.harmonyos.com/cn/docs/documentation/doc-guides-V3/arkts-routing-0000001503325125-V3#ZH-CN_TOPIC_0000001523968678__%E7%B3%BB%E7%BB%9F%E9%BB%98%E8%AE%A4%E8%AF%A2%E9%97%AE%E6%A1%86)和[自定义询问框](https://developer.harmonyos.com/cn/docs/documentation/doc-guides-V3/arkts-routing-0000001503325125-V3#ZH-CN_TOPIC_0000001523968678__%E8%87%AA%E5%AE%9A%E4%B9%89%E8%AF%A2%E9%97%AE%E6%A1%86)两个方面来介绍如何实现页面返回前增加一个询问框的功能。

图3 页面返回前增加一个询问框
![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231121183906.55033134735560264295205914009821:50001231000000:2800:53C6371D78ACF3FA5771C3FADB77105A997374E6982A4B6A6641E66A5E21B10A.gif?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true "点击放大")

### 系统默认询问框

为了实现这个功能，可以使用页面路由Router模块提供的两个方法：[router.showAlertBeforeBackPage()](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/js-apis-router-0000001478061893-V3#ZH-CN_TOPIC_0000001523808578__routershowalertbeforebackpage9)和[router.back()](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/js-apis-router-0000001478061893-V3#ZH-CN_TOPIC_0000001523808578__routerback)来实现这个功能。

在使用页面路由Router相关功能之前，需要在代码中先导入Router模块。

```
import router from '@ohos.router';
```

如果想要在目标界面开启页面返回询问框，需要在调用[router.back()](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/js-apis-router-0000001478061893-V3#ZH-CN_TOPIC_0000001523808578__routerback)方法之前，通过调用[router.showAlertBeforeBackPage()](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/js-apis-router-0000001478061893-V3#ZH-CN_TOPIC_0000001523808578__routershowalertbeforebackpage9)方法设置返回询问框的信息。例如，在支付页面中定义一个返回按钮的点击事件处理函数：

```
// 定义一个返回按钮的点击事件处理函数
function onBackClick(): void {
  // 调用router.showAlertBeforeBackPage()方法，设置返回询问框的信息
  try {
    router.showAlertBeforeBackPage({
      message: '您还没有完成支付，确定要返回吗？' // 设置询问框的内容
    });
  } catch (err) {
    console.error(`Invoke showAlertBeforeBackPage failed, code is ${err.code}, message is ${err.message}`);
  }

  // 调用router.back()方法，返回上一个页面
  router.back();
}
```

其中，router.showAlertBeforeBackPage()方法接收一个对象作为参数，该对象包含以下属性：

* message：string类型，表示询问框的内容。如果调用成功，则会在目标界面开启页面返回询问框；如果调用失败，则会抛出异常，并通过err.code和err.message获取错误码和错误信息。

  当用户点击“返回”按钮时，会弹出确认对话框，询问用户是否确认返回。选择“取消”将停留在当前页目标页；选择“确认”将触发router.back()方法，并根据参数决定如何执行跳转。

### 自定义询问框

自定义询问框的方式，可以使用[弹窗](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/js-apis-promptaction-0000001478341345-V3)或者[自定义弹窗](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/ts-methods-custom-dialog-box-0000001477981237-V3)实现。这样可以让应用界面与系统默认询问框有所区别，提高应用的用户体验度。本文以弹窗为例，介绍如何实现自定义询问框。

在使用页面路由Router相关功能之前，需要在代码中先导入Router模块。

```
import router from '@ohos.router';
```

在事件回调中，调用弹窗的[promptAction.showDialog()](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/js-apis-promptaction-0000001478341345-V3#ZH-CN_TOPIC_0000001573929081__promptactionshowdialog)方法：

```
function onBackClick() {
  // 弹出自定义的询问框
  promptAction.showDialog({
    message: '您还没有完成支付，确定要返回吗？',
    buttons: [
      {
        text: '取消',
        color: '#FF0000'
      },
      {
        text: '确认',
        color: '#0099FF'
      }
    ]
  }).then((result) => {
    if (result.index === 0) {
      // 用户点击了“取消”按钮
      console.info('User canceled the operation.');
    } else if (result.index === 1) {
      // 用户点击了“确认”按钮
      console.info('User confirmed the operation.');
      // 调用router.back()方法，返回上一个页面
      router.back();
    }
  }).catch((err) => {
    console.error(`Invoke showDialog failed, code is ${err.code}, message is ${err.message}`);
  })
}
```

当用户点击“返回”按钮时，会弹出自定义的询问框，询问用户是否确认返回。选择“取消”将停留在当前页目标页；选择“确认”将触发router.back()方法，并根据参数决定如何执行跳转。

