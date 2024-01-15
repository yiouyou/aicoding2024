# Navigation

更新时间: 2024-01-15 12:18

[Navigation](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/ts-basic-components-navigation-0000001478341133-V3)组件一般作为页面的根容器，包括单页面、分栏和自适应三种显示模式。同时，Navigation提供了属性来设置页面的标题栏、工具栏、导航栏等。

Navigation组件的页面包含主页和内容页。主页由标题栏、内容区和工具栏组成，可在内容区中使用[NavRouter](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/ts-basic-components-navrouter-0000001478061693-V3)子组件实现导航栏功能。内容页主要显示[NavDestination](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/ts-basic-components-navdestination-0000001477981193-V3)子组件中的内容。

NavRouter是配合Navigation使用的特殊子组件，默认提供点击响应处理，不需要开发者自定义点击事件逻辑。NavRouter有且仅有两个子组件，其中第二个子组件必须是NavDestination。NavDestination是配合NavRouter使用的特殊子组件，用于显示Navigation组件的内容页。当开发者点击NavRouter组件时，会跳转到对应的NavDestination内容区。

## 设置页面显示模式

Navigation组件通过mode属性设置页面的显示模式。

* 自适应模式Navigation组件默认为自适应模式，此时mode属性为NavigationMode.Auto。自适应模式下，当设备宽度大于520vp时，Navigation组件采用分栏模式，反之采用单页面模式。

```
Navigation() {
  ...
}
.mode(NavigationMode.Auto)
```
* 单页面模式
  图1 单页面布局示意图
  ![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231121183907.22083766261129926323372459598762:50001231000000:2800:26E46C812A2353787B85A201D811678F4C97E56EF09168F5EF6EE9867708A11F.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true "点击放大")
  将mode属性设置为NavigationMode.Stack，Navigation组件即可设置为单页面显示模式。

```
Navigation() {
  ...
}
.mode(NavigationMode.Stack)
```

  ![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231121183907.15336480528378636863953476133211:50001231000000:2800:66784937ACF83A4401C64FB6B9769AA138CEEAFCDBB00376FE7062E5CDA475CD.jpg?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true "点击放大")
* 分栏模式
  图2 分栏布局示意图
  ![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231121183907.80686546974892578856180834138451:50001231000000:2800:EA5EAB64D9EED9DA155C74BB5A476561508B26A6C11EBAEC0EF17140778F6471.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true "点击放大")
  将mode属性设置为NavigationMode.Split，Navigation组件即可设置为分栏显示模式。

```
@Entry
@Component
struct NavigationExample {
  private arr: number[] = [1, 2, 3];

  build() {
    Column() {
      Navigation() {
        TextInput({ placeholder: 'search...' })
          .width("90%")
          .height(40)
          .backgroundColor('#FFFFFF')

        List({ space: 12 }) {
          ForEach(this.arr, (item) => {
            ListItem() {
              NavRouter() {
                Text("NavRouter" + item)
                  .width("100%")
                  .height(72)
                  .backgroundColor('#FFFFFF')
                  .borderRadius(24)
                  .fontSize(16)
                  .fontWeight(500)
                  .textAlign(TextAlign.Center)
                NavDestination() {
                  Text("NavDestinationContent" + item)
                }
                .title("NavDestinationTitle" + item)
              }
            }
          }, item => item)
        }
        .width("90%")
        .margin({ top: 12 })
      }
      .title("主标题")
      .mode(NavigationMode.Split)
      .menus([
        {value: "", icon: "./image/ic_public_search.svg", action: ()=> {}},
        {value: "", icon: "./image/ic_public_add.svg", action: ()=> {}},
        {value: "", icon: "./image/ic_public_add.svg", action: ()=> {}},
        {value: "", icon: "./image/ic_public_add.svg", action: ()=> {}},
        {value: "", icon: "./image/ic_public_add.svg", action: ()=> {}}
      ])
      .toolBar({items: [
        {value: "func", icon: "./image/ic_public_highlights.svg", action: ()=> {}},
        {value: "func", icon: "./image/ic_public_highlights.svg", action: ()=> {}},
        {value: "func", icon: "./image/ic_public_highlights.svg", action: ()=> {}}
      ]})
    }
    .height('100%')
    .width('100%')
    .backgroundColor('#F1F3F5')
  }
}
```

  ![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231121183907.38593676869309170092600423878398:50001231000000:2800:F6ECA5CC9F8BBF04FEFBB28E50FA44205ACFAA160717E12A1B164543363E0BDA.jpg?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true "点击放大")

## 设置标题栏模式

标题栏在界面顶部，用于呈现界面名称和操作入口，Navigation组件通过titleMode属性设置标题栏模式。

* Mini模式
  普通型标题栏，用于一级页面不需要突出标题的场景。图3 Mini模式标题栏
  ![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231121183907.59102527920379263325372420276760:50001231000000:2800:D87F6CC17572854649C298FC9781605E2AB18964645C1610815650C0219DD927.jpg?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true "点击放大")

```
Navigation() {
  ...
}
.titleMode(NavigationTitleMode.Mini)
```
* Full模式强调型标题栏，用于一级页面需要突出标题的场景。

  图4 Full模式标题栏
  ![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231121183907.73171298361761324502101951665906:50001231000000:2800:250158FAFABBD1E845790620AC33BA4E37436B915661625956474740789197ED.jpg?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true "点击放大")

```
Navigation() {
  ...
}
.titleMode(NavigationTitleMode.Full)
```

## 设置菜单栏

菜单栏位于Navigation组件的右上角，开发者可以通过menus属性进行设置。menus支持Array[[NavigationMenuItem](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/ts-basic-components-navigation-0000001478341133-V3#ZH-CN_TOPIC_0000001523648374__navigationmenuitem%E7%B1%BB%E5%9E%8B%E8%AF%B4%E6%98%8E)](%5BNavigationMenuItem%5D(https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/ts-basic-components-navigation-0000001478341133-V3#ZH-CN_TOPIC_0000001523648374__navigationmenuitem%E7%B1%BB%E5%9E%8B%E8%AF%B4%E6%98%8E))和[CustomBuilder](https://developer.harmonyos.com/cn/docs/documentation/doc-guides-V3/arkts-builder-0000001524176981-V3)两种参数类型。使用Array`<NavigationMenuItem>`类型时，竖屏最多支持显示3个图标，横屏最多支持显示5个图标，多余的图标会被放入自动生成的更多图标。

图5 设置了3个图标的菜单栏
![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231121183907.91167692619942929084265643358720:50001231000000:2800:7FAF3304722308D6ADD3DF6C36B6804FB42BA7975AE97C67A1FD48FC986567BF.jpg?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true "点击放大")

```
Navigation() {
  ...
}
.menus([{value: "", icon: "./image/ic_public_search.svg", action: ()=>{}},
        {value: "", icon: "./image/ic_public_add.svg", action: ()=>{}},
        {value: "", icon: "./image/ic_public_add.svg", action: ()=>{}}])
```

图6 设置了4个图标的菜单栏
![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231121183907.45474865840653783813126093822041:50001231000000:2800:3F2ED5EA3088DB0CD43B2FDD0D6662C21799699C1F1BCF4ABABD0D6AC187C3D2.jpg?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true "点击放大")

```
Navigation() {
  ...
}
.menus([{value: "", icon: "./image/ic_public_search.svg", action: ()=>{}},
        {value: "", icon: "./image/ic_public_add.svg", action: ()=>{}},
        {value: "", icon: "./image/ic_public_add.svg", action: ()=>{}},
        {value: "", icon: "./image/ic_public_add.svg", action: ()=>{}}])
```

## 设置工具栏

工具栏位于Navigation组件的底部，开发者可以通过toolBar属性进行设置。

图7 工具栏
![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231121183908.56418621467618143492588730370660:50001231000000:2800:C8AC414315A887F92949045773D4D989191FB5D83255E0B19B1297D6AFCBB39A.jpg?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true "点击放大")

```
Navigation() {
  ...
}
.toolBar({items:[
        {value: "func", icon: "./image/ic_public_highlights.svg", action: ()=>{}},
        {value: "func", icon: "./image/ic_public_highlights.svg", action: ()=>{}},
        {value: "func", icon: "./image/ic_public_highlights.svg", action: ()=>{}}]})
```

