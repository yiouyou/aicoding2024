# 文本输入（TextInput/TextArea）

更新时间: 2024-01-15 12:20

TextInput、TextArea是输入框组件，通常用于响应用户的输入操作，比如评论区的输入、聊天框的输入、表格的输入等，也可以结合其它组件构建功能页面，例如登录注册页面。具体用法参考[TextInput](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/ts-basic-components-textinput-0000001427584864-V3)、[TextArea](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/ts-basic-components-textarea-0000001427902464-V3)。

## 创建输入框

TextInput为单行输入框、TextArea为多行输入框。通过以下接口来创建。

```
TextArea(value?:{placeholder?: ResourceStr, text?: ResourceStr, controller?: TextAreaController})
```

```
TextInput(value?:{placeholder?: ResourceStr, text?: ResourceStr, controller?: TextInputController})
```

* 单行输入框

```
TextInput()
```

  ![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231121183900.60105743670591572432693151922254:50001231000000:2800:D34F5E468BE91ABB83F0D8B7667CBE833F826C653032986F1B35ADE9F70255B2.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)
* 多行输入框

```
TextArea()
```

  ![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231121183901.18787163973979756192018624158969:50001231000000:2800:4EDAF7C46C1E024009A883976D7BA7D1D411DDE3824046878082CF6B0B1A5192.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)

  多行输入框文字超出一行时会自动折行。

```
TextArea({text:"我是TextArea我是TextArea我是TextArea我是TextArea"}).width(300)
```

  ![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231121183901.54124870910132494382915045969135:50001231000000:2800:342C3C6EAA62875216855A64AFA7E9D81E4ADAAA306171634F3EAB0390673209.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)

## 设置输入框类型

TextInput有5种可选类型，分别为Normal基本输入模式、Password密码输入模式、Email邮箱地址输入模式、Number纯数字输入模式、PhoneNumber电话号码输入模式。通过type属性进行设置：

* 基本输入模式（默认类型）

```
TextInput()
  .type(InputType.Normal)
```

  ![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231121183901.88243555708157205155533778486989:50001231000000:2800:B54E79DB74C92AA39BC0DB90EA9D008F7987DF67D4AB76A4A366F056A51A31C5.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)
* 密码输入模式

```
TextInput()
  .type(InputType.Password)
```

  ![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231121183901.57353881986755179431735971058548:50001231000000:2800:C8CD01FF872720462A5501DD6A796FA948BD73512E5C1B66730179A1DF07DA06.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)

## 自定义样式

* 设置无输入时的提示文本。TextInput({placeholder:'我是提示文本'})

```
TextInput({placeholder:'我是提示文本'})
```

  ![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231121183901.71449742475743655727732278465084:50001231000000:2800:14D0F29F147212DF3B3FB5E791F6C6587154148AC2B07FA8AF2526E5E6224DEE.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)

* 设置输入框当前的文本内容。

```
TextInput({placeholder:'我是提示文本',text:'我是当前文本内容'})
```

  ![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231121183901.58953168371699324434886289553484:50001231000000:2800:B5B67240785653DB4E60A7FDEA8FF095246F844F1E3C148A458D543D413B7BD6.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)
* 添加backgroundColor改变输入框的背景颜色。

```
TextInput({placeholder:'我是提示文本',text:'我是当前文本内容'})
  .backgroundColor(Color.Pink)
```

  ![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231121183901.46258544254859938677826376725522:50001231000000:2800:6207A8927B48EEDE7F058FA8BDC4AD955F8840679E89D12CA93B8175916958F1.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)

  更丰富的样式可以结合[通用属性](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/ts-universal-attributes-size-0000001428061700-V3)实现。

## 添加事件

文本框主要用于获取用户输入的信息，把信息处理成数据进行上传，绑定onChange事件可以获取输入框内改变的内容。用户也可以使用通用事件来进行相应的交互操作。

```
TextInput()
  .onChange((value: string) => {
    console.info(value);
  })
  .onFocus(() => {
    console.info('获取焦点');
  })
```

## 场景示例

用于表单的提交，在用户登录/注册页面，用户的登录或注册的输入操作。

```
@Entry
@Component
struct TextInputSample {
  build() {
    Column() {
      TextInput({ placeholder: 'input your username' }).margin({ top: 20 })
        .onSubmit((EnterKeyType)=>{
          console.info(EnterKeyType+'输入法回车键的类型值')
        })
      TextInput({ placeholder: 'input your password' }).type(InputType.Password).margin({ top: 20 })
        .onSubmit((EnterKeyType)=>{
          console.info(EnterKeyType+'输入法回车键的类型值')
        })
      Button('Sign in').width(150).margin({ top: 20 })
    }.padding(20)
  }
}
```

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231121183901.49165210017560003257249200742946:50001231000000:2800:7ACF303A0C57C6E852CA461278472AD4CD6B436183351B664B31195D6261B87F.gif?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)

