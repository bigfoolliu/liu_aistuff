一个注册登录界面,可以提交表单交给后台进行验证


数据库模型设计:
    用户表:
        - 用户名
        - 密码
        - 邮箱
        - 性别
        - 创建时间

    路由设计:
        - 登录功能属于站点的一级功能,应该使用一级路由
        - 具体如下:

            URL             视图                              模板
            /index/         app_login.views.index()           index.html
            /login/         app_login.views.login()           login.html
            /register/      app_login.views.register()        register.html
            /logout/        app_login.views.logout()          不需要


Session会话:
    - 依赖Cookie！
    - 但与Cookie不同的地方在于Session将所有的数据都放在服务器端，用户浏览器的Cookie中只会保存一个非明文的识别信息，比如哈希值。
    - Django提供了一个通用的Session框架，并且可以使用多种session数据的保存方式：
        1. 保存在数据库内
        2. 保存到缓存
        3. 保存到文件内
        4. 保存到cookie内
    - 通常情况，没有特别需求的话，请使用保存在数据库内的方式，尽量不要保存到Cookie内,保障数据安全.
    参考网址: http://www.liujiangblog.com/course/django/111