from jinja2 import Environment, PackageLoader

# env = Environment(loader=PackageLoader("jinja_demo"))
# print(env)

# print(env.list_templates())

# template = env.get_template("base.html")
# content = template.render(client="大家")
# print(content, type(content))


def get_template(template_file_path, **kwargs):
    print(kwargs)
    env = Environment(loader=PackageLoader("jinja_demo"))
    template = env.get_template(template_file_path)
    content = template.render(kwargs)
    print(content)


get_template("base.html", client="haha")
