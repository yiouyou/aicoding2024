p = [
    'UI开发-方舟开发框架（ArkUI）概述.md',
    'UI开发-基于ArkTS的声明式开发范式-UI开发（ArkTS声明式开发范式）概述.md',
    'UI开发-基于ArkTS的声明式开发范式-开发布局-布局概述.md',
    'UI开发-基于ArkTS的声明式开发范式-开发布局-构建布局-线性布局.md',
    'UI开发-基于ArkTS的声明式开发范式-开发布局-构建布局-层叠布局.md',
    'UI开发-基于ArkTS的声明式开发范式-开发布局-构建布局-弹性布局.md',
    'UI开发-基于ArkTS的声明式开发范式-开发布局-构建布局-相对布局.md',
    'UI开发-基于ArkTS的声明式开发范式-开发布局-构建布局-栅格布局.md',
    'UI开发-基于ArkTS的声明式开发范式-开发布局-构建布局-媒体查询.md',
    'UI开发-基于ArkTS的声明式开发范式-开发布局-构建布局-创建列表.md',
    'UI开发-基于ArkTS的声明式开发范式-开发布局-构建布局-创建网格.md',
    'UI开发-基于ArkTS的声明式开发范式-开发布局-构建布局-创建轮播.md',
    'UI开发-基于ArkTS的声明式开发范式-开发布局-改善布局性能.md',
    'UI开发-基于ArkTS的声明式开发范式-添加组件-添加常用组件-按钮.md',
    'UI开发-基于ArkTS的声明式开发范式-添加组件-添加常用组件-单选框.md',
    'UI开发-基于ArkTS的声明式开发范式-添加组件-添加常用组件-切换按钮.md',
    'UI开发-基于ArkTS的声明式开发范式-添加组件-添加常用组件-进度条.md',
    'UI开发-基于ArkTS的声明式开发范式-添加组件-添加常用组件-文本显示.md',
    'UI开发-基于ArkTS的声明式开发范式-添加组件-添加常用组件-文本输入.md',
    'UI开发-基于ArkTS的声明式开发范式-添加组件-添加常用组件-自定义弹窗.md',
    'UI开发-基于ArkTS的声明式开发范式-添加组件-添加常用组件-视频播放.md',
    'UI开发-基于ArkTS的声明式开发范式-添加组件-添加常用组件-XComponent.md',
    'UI开发-基于ArkTS的声明式开发范式-添加组件-添加气泡和菜单-气泡提示.md',
    'UI开发-基于ArkTS的声明式开发范式-添加组件-添加气泡和菜单-菜单.md',
    'UI开发-基于ArkTS的声明式开发范式-设置页面路由和组件导航-页面路由.md',
    'UI开发-基于ArkTS的声明式开发范式-设置页面路由和组件导航-组件导航-Navigation.md',
    'UI开发-基于ArkTS的声明式开发范式-设置页面路由和组件导航-组件导航-Tabs.md',
    'UI开发-基于ArkTS的声明式开发范式-显示图形-显示图片.md',
    'UI开发-基于ArkTS的声明式开发范式-显示图形-绘制几何图形.md',
    'UI开发-基于ArkTS的声明式开发范式-显示图形-使用画布绘制自定义图形.md',
    'UI开发-基于ArkTS的声明式开发范式-使用动画-动画概述.md',
    'UI开发-基于ArkTS的声明式开发范式-使用动画-页面内的动画-布局更新动画.md',
    'UI开发-基于ArkTS的声明式开发范式-使用动画-页面内的动画-组件内转场动画.md',
    'UI开发-基于ArkTS的声明式开发范式-使用动画-页面内的动画-弹簧曲线动画.md',
    'UI开发-基于ArkTS的声明式开发范式-使用动画-页面间的动画-放大缩小视图.md',
    'UI开发-基于ArkTS的声明式开发范式-使用动画-页面间的动画-页面转场动画.md',
    'UI开发-基于ArkTS的声明式开发范式-支持交互事件-交互事件概述.md',
    'UI开发-基于ArkTS的声明式开发范式-支持交互事件-使用通用事件-触屏事件.md',
    'UI开发-基于ArkTS的声明式开发范式-支持交互事件-使用通用事件-键鼠事件.md',
    'UI开发-基于ArkTS的声明式开发范式-支持交互事件-使用通用事件-焦点事件.md',
    'UI开发-基于ArkTS的声明式开发范式-支持交互事件-使用手势事件-绑定手势方法.md',
    'UI开发-基于ArkTS的声明式开发范式-支持交互事件-使用手势事件-单一手势.md',
    'UI开发-基于ArkTS的声明式开发范式-支持交互事件-使用手势事件-组合手势.md',
    'UI开发-基于ArkTS的声明式开发范式-性能提升的推荐方法.md',
]


# for i in p:
#     with open(i, 'w', encoding='utf-8') as f:
#         f.write('')
# exit()

def readF(fn):
    with open(fn, 'r', encoding='utf-8') as f:
        # li = f.readlines()
        # for i in li:
        #     if i.startswith('  图'):
        #         print(fn, i)
        out = f.read()
        out1 = out.replace('[]()[]()', '')
        out2 = out.replace('**', '')
        if out != out1:
            print(fn, '[]()[]()')
        if out != out2:
            print(fn, '**')
        return out
                
str = ''
for i in p:
    # print(i)
    str += readF(i) + "\n\n"

# print(str)

with open('cat.txt', 'w', encoding='utf-8') as f:
    f.write(str)

