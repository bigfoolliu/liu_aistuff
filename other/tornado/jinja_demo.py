#!/usr/bin/env python3
# -*- coding:utf-8 -*-


from jinja2 import PackageLoader,Environment
import os
from jinja2 import Template


# template = Template('Hello {{ name }}!')
# ret = template.render(name='John Doe')
# print(ret)


env = Environment(loader=PackageLoader('tornado', 'templates'))
print(env)

template = env.get_template("base.html")
print(template.render(name="tony"))
