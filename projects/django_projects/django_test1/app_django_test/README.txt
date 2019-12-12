django app:
    - 一个包含模型,视图和django代码,并且形式为独立python包的完整django应用.

MVC模式:
    - 把数据存取逻辑、业务逻辑和表现逻辑组合在一起的概念有时被称为软件架构的 Model-View-Controller(MVC)模式。
    - M: 代表数据存取层, 由django数据库层(模型)处理
      V: 代表的是系统中选择显示什么和怎么显示的部分, 由视图和模板处理
      C: 系统中根据用户输入并视需要访问模型，以决定使用哪个视图的那部分, 由Django框架根据URLconf设置, 对给定URL调用适当的Python函数
    - 由于C由框架自行处理,因此django更关注(Model, Template, View),即也被称为 MTV 框架
        M: model,模型,即数据存取层
        T: template, 表现层
        V: View,业务逻辑层