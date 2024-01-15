p = [
    '快速入门-开发准备.md',
    '快速入门-构建第一个ArkTS应用（Stage模型）.md',
    '开发基础知识-应用程序包基础知识-应用程序包概述.md',
    '开发基础知识-应用程序包基础知识-应用程序包结构-Stage模型应用程序包结构.md',
    '开发基础知识-应用程序包基础知识-应用程序包多HAP机制-多HAP机制设计目标.md',
    '开发基础知识-应用程序包基础知识-应用程序包多HAP机制-多HAP构建视图.md',
    '开发基础知识-应用程序包基础知识-应用程序包多HAP机制-多HAP的开发调试与发布部署流程.md',
    '开发基础知识-应用程序包基础知识-应用程序包多HAP机制-多HAP使用规则.md',
    '开发基础知识-应用程序包基础知识-应用程序包多HAP机制-多HAP运行机制及数据通信方式.md',
    '开发基础知识-应用程序包基础知识-共享包-共享包概述.md',
    '开发基础知识-应用程序包基础知识-共享包-HAR.md',
    '开发基础知识-应用程序包基础知识-共享包-HSP-应用内HSP开发指导.md',
    '开发基础知识-应用程序包基础知识-应用程序包快速修复-快速修复概述.md',
    '开发基础知识-应用程序包基础知识-应用程序包快速修复-快速修复命令行调试开发指导.md',
    '开发基础知识-应用程序包基础知识-应用程序包更新流程.md',
    '开发基础知识-应用配置文件（Stage模型）-应用配置文件概述（Stage模型）.md',
    '开发基础知识-应用配置文件（Stage模型）-app.json5配置文件.md',
    '开发基础知识-应用配置文件（Stage模型）-module.json5配置文件.md',
    '学习ArkTS语言-初始ArkTS语言.md',
    '学习ArkTS语言-状态管理-状态管理概述.md',
    '学习ArkTS语言-基本语法-基本语法概述.md',
    '学习ArkTS语言-基本语法-声明式UI描述.md',
    '学习ArkTS语言-基本语法-自定义组件-创建自定义组件.md',
    '学习ArkTS语言-基本语法-自定义组件-页面和自定义组件生命周期.md',
    '学习ArkTS语言-基本语法-Builder装饰器.md',
    '学习ArkTS语言-基本语法-BuilderParam装饰器.md',
    '学习ArkTS语言-基本语法-Styles装饰器.md',
    '学习ArkTS语言-基本语法-Extend装饰器.md',
    '学习ArkTS语言-基本语法-stateStyles.md',
    '学习ArkTS语言-状态管理-管理组件拥有的状态-State装饰器.md',
    '学习ArkTS语言-状态管理-管理组件拥有的状态-Prop装饰器.md',
    '学习ArkTS语言-状态管理-管理组件拥有的状态-Link装饰器.md',
    '学习ArkTS语言-状态管理-管理组件拥有的状态-Provide装饰器和Consume装饰器.md',
    '学习ArkTS语言-状态管理-管理组件拥有的状态-Observed装饰器和ObjectLink装饰器.md',
    '学习ArkTS语言-状态管理-管理应用拥有的状态-管理应用拥有的状态概述.md',
    '学习ArkTS语言-状态管理-管理应用拥有的状态-LocalStorage.md',
    '学习ArkTS语言-状态管理-管理应用拥有的状态-AppStorage.md',
    '学习ArkTS语言-状态管理-管理应用拥有的状态-PersistentStorage.md',
    '学习ArkTS语言-状态管理-管理应用拥有的状态-Environment.md',
    '学习ArkTS语言-状态管理-其他状态管理-其他状态管理概述.md',
    '学习ArkTS语言-状态管理-其他状态管理-Watch装饰器.md',
    '学习ArkTS语言-状态管理-其他状态管理-$$语法.md',
    '学习ArkTS语言-渲染控制-渲染控制概述.md',
    '学习ArkTS语言-渲染控制-条件渲染.md',
    '学习ArkTS语言-渲染控制-循环渲染.md',
    '学习ArkTS语言-渲染控制-数据懒加载.md',
]

def readF(fn):
    with open(fn, 'r', encoding='utf-8') as f:
        # li = f.readlines()
        # for i in li:
        #     if i.startswith('  图'):
        #         print(fn, i)
        return f.read()
                
str = ''
for i in p:
    # print(i)
    str += readF(i) + "\n\n"

print(str)

with open('cat.txt', 'w', encoding='utf-8') as f:
    f.write(str)

