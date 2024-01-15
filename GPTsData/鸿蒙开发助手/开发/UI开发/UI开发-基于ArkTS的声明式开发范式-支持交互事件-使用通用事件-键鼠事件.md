# 键鼠事件

更新时间: 2024-01-15 12:21

键鼠事件指键盘，鼠标外接设备的输入事件。

## 鼠标事件

支持的鼠标事件包含通过外设鼠标、触控板触发的事件。

鼠标事件可触发以下回调：

| 名称                                         | 描述                                                                                                                                                                  |
| :------------------------------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| onHover(event: (isHover: boolean) => void)   | 鼠标进入或退出组件时触发该回调。isHover：表示鼠标是否悬浮在组件上，鼠标进入时为true, 退出时为false。                                                                  |
| onMouse(event: (event?: MouseEvent) => void) | 当前组件被鼠标按键点击时或者鼠标在组件上悬浮移动时，触发该回调，event返回值包含触发事件时的时间戳、鼠标按键、动作、鼠标位置在整个屏幕上的坐标和相对于当前组件的坐标。 |

当组件绑定onHover回调时，可以通过[hoverEffect](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/ts-universal-attributes-hover-effect-0000001477981177-V3)属性设置该组件的鼠标悬浮态显示效果。

图1 鼠标事件数据流

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231121183921.70850655806679963120771428393706:50001231000000:2800:E21F7D619E0EC5BF87750A0ACEC8E802C37E84BDDCAB0FD6872A8613BEC50455.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)

鼠标事件传递到ArkUI之后，会先判断鼠标事件是否是左键的按下/抬起/移动，然后做出不同响应：

* 是：鼠标事件先转换成相同位置的触摸事件，执行触摸事件的碰撞测试、手势判断和回调响应。接着去执行鼠标事件的碰撞测试和回调响应。
* 否：事件仅用于执行鼠标事件的碰撞测试和回调响应。

说明

所有单指可响应的触摸事件/手势事件，均可通过鼠标左键来操作和响应。例如当我们需要开发单击Button跳转页面的功能、且需要支持手指点击和鼠标左键点击，那么只绑定一个点击事件（onClick）就可以实现该效果。若需要针对手指和鼠标左键的点击实现不一样的效果，可以在onClick回调中，使用回调参数中的source字段即可判断出当前触发事件的来源是手指还是鼠标。

### onHover

```
onHover(event: (isHover?: boolean) => void)
```

鼠标悬浮事件回调。参数isHover类型为boolean，表示鼠标进入组件或离开组件。该事件不支持自定义冒泡设置，默认父子冒泡。

若组件绑定了该接口，当鼠标指针从组件外部进入到该组件的瞬间会触发事件回调，参数isHover等于true；鼠标指针离开组件的瞬间也会触发该事件回调，参数isHover等于false。

说明

事件冒泡：在一个树形结构中，当子节点处理完一个事件后，再将该事件交给它的父节点处理。

```
// xxx.ets
@Entry
@Component
struct MouseExample {
  @State isHovered: boolean = false;

  build() {
    Column() {
      Button(this.isHovered ? 'Hovered!' : 'Not Hover')
        .width(200).height(100)
        .backgroundColor(this.isHovered ? Color.Green : Color.Gray)
        .onHover((isHover: boolean) => { // 使用onHover接口监听鼠标是否悬浮在Button组件上
          this.isHovered = isHover;
        })
    }.width('100%').height('100%').justifyContent(FlexAlign.Center)
  }
}
```

该示例创建了一个Button组件，初始背景色为灰色，内容为“Not Hover”。示例中的Button组件绑定了onHover回调，在该回调中将this.isHovered变量置为回调参数：isHover。

当鼠标从Button外移动到Button内的瞬间，回调响应，isHover值等于true，isHovered的值变为true，将组件的背景色改成Color.Green，内容变为“Hovered!”。

当鼠标从Button内移动到Button外的瞬间，回调响应，isHover值等于false，又将组件变成了初始的样式。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231121183921.41571006364317589443068562368603:50001231000000:2800:93B1DA82877F98228B05C61CEF05D101ED10D4FA9128BF49F4EE46B57A9DF250.gif?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)

### onMouse

```
onMouse(event: (event?: MouseEvent) => void)
```

鼠标事件回调。绑定该API的组件每当鼠标指针在该组件内产生行为（MouseAction）时，触发事件回调，参数为[MouseEvent](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/ts-universal-mouse-key-0000001478341101-V3#ZH-CN_TOPIC_0000001523648774__mouseevent%E5%AF%B9%E8%B1%A1%E8%AF%B4%E6%98%8E)对象，表示触发此次的鼠标事件。该事件支持自定义冒泡设置，默认父子冒泡。常见用于开发者自定义的鼠标行为逻辑处理。

开发者可以通过回调中的MouseEvent对象获取触发事件的坐标（screenX/screenY/x/y）、按键（[MouseButton](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/ts-appendix-enums-0000001478061741-V3#ZH-CN_TOPIC_0000001574248789__mousebutton)）、行为（[MouseAction](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/ts-appendix-enums-0000001478061741-V3#ZH-CN_TOPIC_0000001574248789__mouseaction)）、时间戳（timestamp）、交互组件的区域（[EventTarget](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/ts-universal-events-click-0000001477981153-V3#ZH-CN_TOPIC_0000001523488894__eventtarget8%E5%AF%B9%E8%B1%A1%E8%AF%B4%E6%98%8E)）、事件来源（[SourceType](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/ts-gesture-settings-0000001477981181-V3#ZH-CN_TOPIC_0000001523808714__sourcetype%E6%9E%9A%E4%B8%BE%E8%AF%B4%E6%98%8E)）等。MouseEvent的回调函数stopPropagation用于设置当前事件是否阻止冒泡。

说明

按键（MouseButton）的值：Left/Right/Middle/Back/Forward 均对应鼠标上的实体按键，当这些按键被按下或松开时触发这些按键的事件。None表示无按键，会出现在鼠标没有按键按下或松开的状态下，移动鼠标所触发的事件中。

```
// xxx.ets
@Entry
@Component
struct MouseExample {
  @State isHovered: boolean = false;
  @State buttonText: string = '';
  @State columnText: string = '';

  build() {
    Column() {
      Button(this.isHovered ? 'Hovered!' : 'Not Hover')
        .width(200)
        .height(100)
        .backgroundColor(this.isHovered ? Color.Green : Color.Gray)
        .onHover((isHover: boolean) => {
          this.isHovered = isHover
        })
        .onMouse((event: MouseEvent) => {    // 给Button组件设置onMouse回调
          this.buttonText = 'Button onMouse:\n' + '' +
          'button = ' + event.button + '\n' +
          'action = ' + event.action + '\n' +
          'x,y = (' + event.x + ',' + event.y + ')' + '\n' +
          'screenXY=(' + event.screenX + ',' + event.screenY + ')';
        })
      Divider()
      Text(this.buttonText).fontColor(Color.Green)
      Divider()
      Text(this.columnText).fontColor(Color.Red)
    }
    .width('100%')
    .height('100%')
    .justifyContent(FlexAlign.Center)
    .borderWidth(2)
    .borderColor(Color.Red)
    .onMouse((event: MouseEvent) => {    // 给Column组件设置onMouse回调
      this.columnText = 'Column onMouse:\n' + '' +
      'button = ' + event.button + '\n' +
      'action = ' + event.action + '\n' +
      'x,y = (' + event.x + ',' + event.y + ')' + '\n' +
      'screenXY=(' + event.screenX + ',' + event.screenY + ')';
    })
  }
}
```

在onHover示例的基础上，给Button绑定onMouse接口。在回调中，打印出鼠标事件的button/action等回调参数值。同时，在外层的Column容器上，也做相同的设置。整个过程可以分为以下两个动作：

1. 移动鼠标：当鼠标从Button外部移入Button的过程中，仅触发了Column的onMouse回调；当鼠标移入到Button内部后，由于onMouse事件默认是冒泡的，所以此时会同时响应Column的onMouse回调和Button的onMouse回调。此过程中，由于鼠标仅有移动动作没有点击动作，因此打印信息中的button均为0（MouseButton.None的枚举值）、action均为3（MouseAction.Move的枚举值）。
2. 点击鼠标：鼠标进入Button后进行了2次点击，分别是左键点击和右键点击。左键点击时：button = 1（MouseButton.Left的枚举值），按下时 action = 1（MouseAction.Press的枚举值），抬起时 action = 2（MouseAction.Release的枚举值）。

   右键点击时：button = 2（MouseButton.Right的枚举值），按下时 action = 1（MouseAction.Press的枚举值），抬起时 action = 2（MouseAction.Release的枚举值）。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231121183921.89991304960755308547060958051626:50001231000000:2800:4E959048BD64E93C258F9A801DBC15F4FA610E402487246C1321C0A9EEADFDDA.gif?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true "点击放大")

如果需要阻止鼠标事件冒泡，可以通过调用stopPropagation()方法进行设置。

```
Button(this.isHovered ? 'Hovered!' : 'Not Hover')
  .width(200)
  .height(100)
  .backgroundColor(this.isHovered ? Color.Green : Color.Gray)
  .onHover((isHover: boolean) => {
    this.isHovered = isHover;
  })
  .onMouse((event: MouseEvent) => {
    event.stopPropagation(); // 在Button的onMouse事件中设置阻止冒泡
    this.buttonText = 'Button onMouse:\n' + '' +
    'button = ' + event.button + '\n' +
    'action = ' + event.action + '\n' +
    'x,y = (' + event.x + ',' + event.y + ')' + '\n' +
    'screenXY=(' + event.screenX + ',' + event.screenY + ')';
  })
```

在子组件（Button）的onMouse中，通过回调参数event调用stopPropagation回调方法（如下）即可阻止Button子组件的鼠标事件冒泡到父组件Column上。

```
event.stopPropagation()
```

效果是：当鼠标在Button组件上操作时，仅Button的onMouse回调会响应，Column的onMouse回调不会响应。

### hoverEffect

```
hoverEffect(value: HoverEffect)
```

鼠标悬浮态效果设置的通用属性。参数类型为HoverEffect，HoverEffect提供的Auto、Scale、Highlight效果均为固定效果，开发者无法自定义设置效果参数。

表1 HoverEffect说明| HoverEffect枚举值 | 效果说明 |
| :- | :- |
| ------------------------------- |

| Auto      | 组件默认提供的悬浮态效果，由各组件定义。                                                                                           |
| --------- | ---------------------------------------------------------------------------------------------------------------------------------- |
| Scale     | 动画播放方式，鼠标悬浮时：组件大小从100%放大至105%，鼠标离开时：组件大小从105%缩小至100%。                                         |
| Highlight | 动画播放方式，鼠标悬浮时：组件背景色叠加一个5%透明度的白色，视觉效果是组件的原有背景色变暗，鼠标离开时：组件背景色恢复至原有样式。 |
| None      | 禁用悬浮态效果                                                                                                                     |

```
// xxx.ets
@Entry
@Component
struct HoverExample {
  build() {
    Column({ space: 10 }) {
      Button('Auto')
        .width(170).height(70)
      Button('Scale')
        .width(170).height(70)
        .hoverEffect(HoverEffect.Scale)
      Button('Highlight')
        .width(170).height(70)
        .hoverEffect(HoverEffect.Highlight)
      Button('None')
        .width(170).height(70)
        .hoverEffect(HoverEffect.None)
    }.width('100%').height('100%').justifyContent(FlexAlign.Center)
  }
}
```

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231121183921.58090470209236308277489980345227:50001231000000:2800:83B261F1A7118CB7CF683E2A4B78E38A0846AFD87976A40E5464B8E4B487FB08.gif?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)

Button默认的悬浮态效果就是缩放效果，因此Auto和Scale的效果一样，Highlight会使背板颜色变暗，None会禁用悬浮态效果。

## 按键事件

图2 按键事件数据流

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231121183921.25505103564641540285533826287924:50001231000000:2800:6FE6F31DC635BA359B8357056A039EA676D663D97ED8BC9AEFE166206048FECE.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)

按键事件由外设键盘等设备触发，经驱动和多模处理转换后发送给当前获焦的窗口。窗口获取到事件后，会先给输入法分发（输入法会消费按键用作输入），若输入法未消费该按键事件，才会将事件发给ArkUI框架。因此，当某输入框组件获焦，且打开了输入法，此时大部分按键事件均会被输入法消费，例如字母键会被输入法用来往输入框中输入对应字母字符、方向键会被输入法用来切换选中备选词。

按键事件到ArkUI框架之后，会先找到完整的父子节点获焦链。从叶子节点到根节点，逐一发送按键事件。

### onKeyEvent

```
onKeyEvent(event: (event?: KeyEvent) => void)
```

按键事件回调，当绑定该方法的组件处于[获焦状态](https://developer.harmonyos.com/cn/docs/documentation/doc-guides-V3/arkts-common-events-focus-event-0000001455502044-V3)下，外设键盘的按键事件会触发该API的回调响应，回调参数为[KeyEvent](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/ts-universal-events-key-0000001427744780-V3#ZH-CN_TOPIC_0000001523488578__keyevent%E5%AF%B9%E8%B1%A1%E8%AF%B4%E6%98%8E)，可由该参数获得当前按键事件的按键行为（[KeyType](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/ts-appendix-enums-0000001478061741-V3#ZH-CN_TOPIC_0000001574248789__keytype)）、键码（[keyCode](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/js-apis-keycode-0000001544703985-V3#ZH-CN_TOPIC_0000001523488694__keycode)）、按键英文名称（keyText）、事件来源设备类型（[KeySource](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/ts-appendix-enums-0000001478061741-V3#ZH-CN_TOPIC_0000001574248789__keysource)）、事件来源设备id（deviceId）、元键按压状态（metaKey）、时间戳（timestamp）、阻止冒泡设置（stopPropagation）。

```
// xxx.ets
@Entry
@Component
struct KeyEventExample {
  @State buttonText: string = '';
  @State buttonType: string = '';
  @State columnText: string = '';
  @State columnType: string = '';

  build() {
    Column() {
      Button('onKeyEvent')
        .width(140).height(70)
        .onKeyEvent((event: KeyEvent) => { // 给Button设置onKeyEvent事件
          if (event.type === KeyType.Down) {
            this.buttonType = 'Down';
          }
          if (event.type === KeyType.Up) {
            this.buttonType = 'Up';
          }
          this.buttonText = 'Button: \n' +
          'KeyType:' + this.buttonType + '\n' +
          'KeyCode:' + event.keyCode + '\n' +
          'KeyText:' + event.keyText;
        })

      Divider()
      Text(this.buttonText).fontColor(Color.Green)

      Divider()
      Text(this.columnText).fontColor(Color.Red)
    }.width('100%').height('100%').justifyContent(FlexAlign.Center)
    .onKeyEvent((event: KeyEvent) => { // 给父组件Column设置onKeyEvent事件
      if (event.type === KeyType.Down) {
        this.columnType = 'Down';
      }
      if (event.type === KeyType.Up) {
        this.columnType = 'Up';
      }
      this.columnText = 'Column: \n' +
      'KeyType:' + this.buttonType + '\n' +
      'KeyCode:' + event.keyCode + '\n' +
      'KeyText:' + event.keyText;
    })
  }
}
```

上述示例中给组件Button和其父容器Column绑定onKeyEvent。应用打开页面加载后，组件树上第一个可获焦的非容器组件自动获焦，该应用只有一个Button组件，因此该组件会自动获焦，由于Button是Column的子节点，Button获焦也同时意味着Column获焦。获焦机制见[焦点事件](https://developer.harmonyos.com/cn/docs/documentation/doc-guides-V3/arkts-common-events-focus-event-0000001455502044-V3)。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231121183921.74209484332555094655296163918479:50001231000000:2800:6D9527B0C719538826FF13DA4FB631A7D9985D2A903B02C1ABDDDC9AF80509E3.gif?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)

打开应用后，依次在键盘上按这些按键：“空格、回车、左Ctrl、左Shift、字母A、字母Z”。

1. 由于onKeyEvent事件默认是冒泡的，所以Button和Column的onKeyEvent都可以响应。
2. 每个按键都有2次回调，分别对应KeyType.Down和KeyType.Up，表示按键被按下、然后抬起。

如果要阻止冒泡，即仅Button响应键盘事件，Column不响应，在Button的onKeyEvent回调中加入event.stopPropagation()方法即可，如下：

```
Button('onKeyEvent')
  .width(140).height(70)
  .onKeyEvent((event: KeyEvent) => {
    // 通过stopPropagation阻止事件冒泡
    event.stopPropagation();
    if (event.type === KeyType.Down) {
      this.buttonType = 'Down';
    }
    if (event.type === KeyType.Up) {
       this.buttonType = 'Up';
    }
     this.buttonText = 'Button: \n' +
     'KeyType:' + this.buttonType + '\n' +
     'KeyCode:' + event.keyCode + '\n' +
     'KeyText:' + event.keyText;
})
```

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231121183922.83404024110731712946703172523019:50001231000000:2800:B61DBAE64F20F8B5EDD709772EC5C21C5342E633DBB46A28F03B124D2F709ED5.gif?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)

