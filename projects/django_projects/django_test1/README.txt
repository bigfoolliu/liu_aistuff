django基础知识:
    文件含义:
        - 外层的django_test1/目录与Django无关，只是你项目的容器，可以任意命名。
        - manage.py：一个命令行工具，用于与Django进行不同方式的交互脚本，非常重要！
        - 内层的django_test1/目录是真正的项目文件包裹目录，它的名字是你引用内部文件的包名，例如：django_test1.urls。
        - django_test1/__init__.py:一个定义包的空文件。
        - django_test1/settings.py:项目的主配置文件，非常重要！
        - django_test1/urls.py:路由文件，所有的任务都是从这里开始分配，相当于Django驱动站点的内容表格，非常重要！
        - django_test1/wsgi.py:一个基于WSGI的web服务器进入点，提供底层的网络通信功能，通常不用关心。


    project和App的区别:
        - 它们的区别就是一个是配置另一个是代码：
        - 一个project包含很多个Django app以及对它们的配置。
        - project的作用是提供配置文件，比方说哪里定义数据库连接信息, 安装的app列表， TEMPLATE_DIRS ，等等
            一个app是一套Django功能的集合，通常包括模型和视图，按Python的包结构的方式存在。
        - 例如，Django本身内建有一些app，例如注释系统和自动管理界面。 app的一个关键点是它们是很容易移植到其他project和被多个project复用。


    常用命令:
        1. 创建超级用户, 用来管理后台:
            python manage.py createsuperuser
        2. 启动开发服务器(开发服务器是不同于真正的Ngnix的线上服务器的):
            python manage.py runserver
        3. 指定ip端口的启动开发服务器:
            - python manage.py runserver 0.0.0.0:8000
            - django运行在8000端口,整个局域网都可以访问该站点
            - django开发服务器具有自动重载功能,即当代码发生更改时,每隔一段时间服务器将自动更新,但是比如增加文件是不会触发服务器重载的,需要手动重启
        4. 开始自动化测试
            python manage.py test appName
        5. 创建数据表(真正的数据迁移)
            python manage.py migrate
        6. 创建暂时的数据迁移
            python manage.py makemigrations appName
        7. 进入Python shell(写入django的环境变量,便于django的模块导入)
            python manage.py shell
        8. 创建一个新的app
            python manage.py startapp appName


    模板文件相关知识:
        1. 变量标签
            {{变量名}}

        2. if/else标签, 且接收and or not
            {% if condition %}
                ...display1
            {% elif condition2 %}
                ...display2
            {% end if %}

        3. for标签
            - 可迭代继而可重复显示display
            {% for item in items %}
                ...display
            {% endfor %}

        4. ifequal标签
            - 比较两个值是否相等
            {% ifequal a b %}
                ...display
            {% endifequal %}

        5. 注释标签
            {# 注释内容 #}

        6. 模板过滤器
            - 可在变量被显示之前修改它
            https://www.runoob.com/django/django-template.html

        7. 继承
            - 允许模板中包含其他模板的内容,类似python中的模块,互相导入代码复用
            https://www.cnblogs.com/yxwang/p/7847191.html


    修改模型时的操作分三步：
        1. 在models.py中修改模型；
        2. 运行python manage.py makemigrations为改动创建迁移记录；
        3. 运行python manage.py migrate，将操作同步到数据库。


    使用类视图的三步:
        1. 修改URLconf设置
        2. 删除一些旧的无用的视图
        3. 采用基于类视图的新视图


    文件目录:
        良好的目录结构是每个应用都应该创建自己的urls、views、models、templates和static，
        每个templates包含一个与应用同名的子目录，
        每个static也包含一个与应用同名的子目录。


django模型层:
    - 用python语法写语句,通过orm将其转换为sql语句,然后再通过pymysql去实际操作数据库
    - django自带ORM系统.
    - ORM:
        - 对象关系映射(object relational mapper)
        - 常见的如: SQLAlchemy
    - 一个Python的类，就是一个模型，代表数据库中的一张数据表

    - 常用字段类型:
        BooleanField            布尔值类型
        CharField               字符串类型
        DateField               日期类型
        EmailField              邮箱类型
        FileField               上传文件类型
        ImageField              图像类型
        IntegerField            整数类型
        GenericIPAddressField   ipv4或ipv6地址类型
        TextField               大量文本内容类型
        URLField                url地址字符串类型
        UUIDField               保存通用唯一识别码字段类型

