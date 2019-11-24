#!/usr/bin/env python3
# -*- coding:utf-8 -*-


"""
k8s deploy：python3 -m invoke k8s-220
"""

from jinja2 import Template, Environment, FileSystemLoader
import requests
from host_manager.driver import docker_registry_util
from invoke import task
import os
import docker
from docker.models.images import Image

DIR = os.path.dirname(os.path.abspath(__file__))
user_name = os.environ.get('USER')


def update_env(**kwargs):
    for key, value in kwargs.items():
        os.environ[key] = value


client = docker.DockerClient("tcp://127.0.0.1:2375")
remote_client = docker.DockerClient("tcp://192.168.6.200:2375")
#remote_deploy = RemoteDeploy(timeout=120)
history_path = os.path.join(DIR, 'invoke.k8s_deploy.history')
registry_client = docker_registry_util.DockerRegistryUtil("http://registry.jiangxingai.com:8080")


def limit_tag(client: docker.DockerClient, image_name, limit_count=1):
    images = client.images.list()
    matched_list = []
    image: Image
    seen_tags = set()
    for image in images:

        for tag in image.tags:
            if image_name not in tag:
                continue
            _, _, name_part = tag.partition("/")
            name, _tag = name_part.split(":", 1)
            if name == image_name and tag not in seen_tags:
                matched_list.append((image, name, tag, image.attrs['Created']))
                seen_tags.add(tag)

    matched_list = sorted(matched_list, key=lambda x: x[3], reverse=True)
    # print("all_list:{}".format(matched_list))
    removed_list = matched_list[limit_count:]
    for ele in removed_list:
        print("remove_local_registry", ele[2])
        client.images.remove(ele[2])
        # for tag in ele[0].tags:
        #    client.images.remove(tag)


def save_version(v):
    with open(history_path, 'w') as f:
        f.write(str(v))


@task
def k8s_deploy(c, v=0):

    old_version = 0
    if v > 0:
        if not os.path.exists(history_path):
            old_version = v - 1
        old_version = open(history_path).read()
        try:
            old_version = int(old_version)
        except Exception:
            old_version = v - 1
    else:
        v = int(open(history_path).read()) + 1

    BASE_REPO = "registry.jiangxingai.com:5000"
    DEPLOY_REPO = '{}/iotedge/host-manager:{}'.format(BASE_REPO, v)
    env_kwargs = dict(PROJ_DIR="{}".format(DIR),
                      PYTHON="{}/venv/bin/python".format(DIR),
                      USER=user_name,
                      CELERY="{}/venv/bin/celery".format(DIR),
                      ASYNC_TEST_TIMEOUT="3600")
    update_env(**env_kwargs)
    registry_client = docker_registry_util.DockerRegistryUtil("http://registry.jiangxingai.com:8080")
    # login user with docker
    print("========login with group docker=============")
    print("========begine {}=============".format(DEPLOY_REPO))
    res = c.run("docker build . -f Dockerfile -t {}".format(DEPLOY_REPO))
    print(res)
    res = c.run("docker push {}".format(DEPLOY_REPO))
    print("=================complete deploy deploy-engine============")
    del res

    registry_client.limit_tag("host-manager", max_count=3)

    limit_tag(client, "host-manager")
    # remote_client = docker.DockerClient("tcp://10.53.1.220:2375")
    limit_tag(remote_client, "host-manager", limit_count=2)
    res = c.run('ansible-playbook {}/playbook/200.yaml -e version={} -e old_version={} -e ansible_sudo_pass=123456'.format(DIR, v, v -1))
    # res = c.run('ansible-playbook {}/playbook/files/host-manager-remove.yml --extra-vars "old_version={}"'.format(DIR, v - 1))
    file_path = 'playbooks/src/host-manager.yaml'
    # _env = Environment(loader=FileSystemLoader(DIR))
    # temp = _env.get_template(file_path)
    # content = temp.render(deploy_version=v)
    # remote_deploy.deploy(content)
    # remove_content = _env.get_template('playbooks/src/host-manager.yaml').render(deploy_version=v - 1)
    # remote_deploy.deploy(remove_content, state='absent')
    save_version(v)


def limit_image(image_name):
    limit_tag(client, image_name)
    limit_tag(remote_client, image_name, limit_count=2)
    registry_client.limit_tag(image_name, max_count=3)


@task
def k8s_220(c):

    old_version = 0
    v = int(open(history_path).read()) + 1
    old_version = v - 1

    BASE_REPO = "registry.jiangxingai.com:5000"
    DEPLOY_REPO = '{}/iotedge/host-manager:{}'.format(BASE_REPO, v)
    registry_client = docker_registry_util.DockerRegistryUtil("http://registry.jiangxingai.com:8080")
    # login user with docker
    print("========login with group docker=============")
    print("========begine {}=============".format(DEPLOY_REPO))
    res = c.run("docker build . -f Dockerfile -t {}".format(DEPLOY_REPO))
    print(res)
    res = c.run("docker push {}".format(DEPLOY_REPO))
    print("=================complete deploy deploy-engine============")
    del res

    registry_client.limit_tag("host-manager", max_count=3)

    limit_tag(client, "host-manager")
    remote_client = docker.DockerClient("tcp://10.53.1.220:2375")
    limit_tag(remote_client, "host-manager", limit_count=2)
    m = {
        "version": v,
        "old_version": v -1,
        "ansible_sudo_pass": "123456",
        "event_ip": "10.208.1.3",
        "mongo_uri": "mongodb//10.208.1.3/host-manager",
        "host_manager_ip": "10.208.1.3",
        "kubeconfig": "kubeconfig220",
        "host_manager_host":"10.208.1.3",
        "mongo_ip":"10.53.1.220"
    }


    res = c.run('ansible-playbook {}/playbook/200.yaml {}'.format(DIR, get_map_extra(m)))
    save_version(v)


@task
def deploy_test(c):
    v = int(open(history_path).read()) + 1
    file_path = 'k8s_yaml/src/src_200.yaml'
    _env = Environment(loader=FileSystemLoader(DIR))
    temp = _env.get_template(file_path)
    content = temp.render(deploy_version=v)
    remote_deploy.deploy(content)


@task
def build_ubuntu(c):
    c.run('docker build . -f Docker/Dockerfile.ubuntu -t ubuntu_deploy_engine')
    c.run("docker tag ubuntu_deploy_engine registry.jiangxingai.com:5000/ubuntu:deploy_engine")
    c.run("docker push registry.jiangxingai.com:5000/ubuntu:deploy_engine")


@task
def run_test(c, deploy=True):
    env_kwargs = dict(PROJ_DIR="{}".format(DIR),
                      PYTHON="{}/venv/bin/python".format(DIR),
                      USER=user_name,
                      CELERY="{}/venv/bin/celery".format(DIR),
                      LOCAL_DEBUG="1",
                      MONGO_HOST="localhost",
                      REDIS_HOST="localhost",
                      RABBIT_URL="amqp://guest:guest@localhost:5672/",
                      HOST_MANAGER_HOST="localhost",
                      EVENT_IP="192.168.6.200",
                      TEST_HOST="http://127.0.0.1:8001",
                      ASYNC_TEST_TIMEOUT="3600",
                      COMPOSE_PORT="9002",
                      TEST='1',
                      DEBUG="1")
    print("env_kwargs:{}".format(env_kwargs))
    update_env(**env_kwargs)
    if deploy:
        c.run("ansible-playbook {}/local_deploy/deploy_engine.yml".format(DIR))
    c.run('ansible localhost -m supervisorctl -a "name=de:cron state=stopped"')
    c.run(f"{env_kwargs['PYTHON']} -m unittest test/test_test*.py -f  -c")
    c.run(f"{env_kwargs['PYTHON']} -m unittest test/test_compose/test*.py -f  -c")
    c.run(f"{env_kwargs['PYTHON']} -m unittest test/test_k8s/test*.py -f  -c")
    c.run('ansible localhost -m supervisorctl -a "name=de:cron state=restarted"')
    c.run(f"{env_kwargs['PYTHON']} -m unittest test/test_cron*.py -f  -c")


@task
def re_de(c):
    c.run("supervisorctl restart de: ")
    c.run("supervisorctl stop de:cron")


def get_map_extra(map_d):
    lines = []
    for key, value in map_d.items():
        lines.append("-e {}={}".format(key, value))
    return " ".join(lines)
        


@task
def run_test_forever(c):
    while 1:
        env_kwargs = dict(PROJ_DIR="{}".format(DIR),
                          PYTHON="{}/venv/bin/python".format(DIR),
                          USER=user_name,
                          CELERY="{}/venv/bin/celery".format(DIR),
                          LOCAL_DEBUG="1",
                          MONGO_HOST="localhost",
                          REDIS_HOST="localhost",
                          RABBIT_URL="amqp://guest:guest@localhost:5672/",
                          HOST_MANAGER_HOST="localhost",
                          EVENT_IP="192.168.6.200",
                          ASYNC_TEST_TIMEOUT="3600",
                          TEST_HOST="http://127.0.0.1:8001",
                          COMPOSE_PORT="9002",
                          DEBUG="1")
        print("env_kwargs:{}".format(env_kwargs))
        update_env(**env_kwargs)
        c.run("ansible-playbook {}/local_deploy/deploy_engine.yml".format(DIR))
        f = c.run(f"{env_kwargs['PYTHON']} -m unittest -f --locals -c")
        lines = f.stderr.split("\n")
        if not lines[-2].strip().startswith("OK"):
            print("[run_test_forever], report_email_for_stderrr：{}".format(f.__dict__))
            res = requests.post("http://localhost:10001/send_email", json={"body": f.stderr + "\n\nLast-Line=============\n" + lines[-2],
                                                                           "subject": "deploy-engine-test-failed_stderr"})
            if res.status_code != 200:
                raise Exception('{}, {}'.format(res.status_code, res.text))


@task
def local_deploy(c):
    env_kwargs = dict(PROJ_DIR="{}".format(DIR),
                      PYTHON="{}/venv/bin/python".format(DIR),
                      USER=user_name,
                      CELERY="{}/venv/bin/celery".format(DIR),
                      LOCAL_DEBUG="1",
                      MONGO_HOST="localhost",
                      REDIS_HOST="localhost",
                      RABBIT_URL="amqp://guest:guest@localhost:5672/",
                      HOST_MANAGER_HOST="localhost",
                      EVENT_IP="192.168.6.200",
                      ASYNC_TEST_TIMEOUT="3600",
                      TEST_HOST="http://127.0.0.1:8001",
                      COMPOSE_PORT="9002",
                      DEBUG="1")
    print("env_kwargs:{}".format(env_kwargs))
    update_env(**env_kwargs)
    c.run("apidoc -i deploy_engine/ -o apidoc/")
    c.run("ansible-playbook {}/local_deploy/deploy_engine.yml".format(DIR))


@task
def run_one_test(c):
    env_kwargs = dict(PROJ_DIR="{}".format(DIR),
                      PYTHON="{}/venv/bin/python".format(DIR),
                      USER=user_name,
                      CELERY="{}/venv/bin/celery".format(DIR),
                      LOCAL_DEBUG="1",
                      MONGO_HOST="localhost",
                      REDIS_HOST="localhost",
                      RABBIT_URL="amqp://guest:guest@localhost:5672/",
                      HOST_MANAGER_HOST="localhost",
                      EVENT_IP="192.168.6.200",
                      ASYNC_TEST_TIMEOUT="3600",
                      TEST_HOST="http://127.0.0.1:8001",
                      DEBUG="1")
    print("env_kwargs:{}".format(env_kwargs))
    update_env(**env_kwargs)
    # c.run("ansible-playbook {}/local_deploy/deploy_engine.yml".format(DIR))
    c.run(f"{env_kwargs['PYTHON']} -m unittest test.test_test_start_worker_app")


@task
def deploy_200(c):
    PROJ_DIR = "{}".format("/home/ubuntu/deploy/deploy_engine")
    env_kwargs = dict(PROJ_DIR=PROJ_DIR,
                      PYTHON="{}/venv/bin/python".format(PROJ_DIR),
                      USER="ubuntu",
                      CELERY="{}/venv/bin/celery".format(PROJ_DIR),
                      LOCAL_DEBUG="1",
                      MONGO_HOST="localhost",
                      REDIS_HOST="localhost",
                      RABBIT_URL="amqp://guest:guest@localhost:5672/",
                      HOST_MANAGER_HOST="localhost",
                      EVENT_IP="192.168.6.200",
                      ASYNC_TEST_TIMEOUT="3600",
                      TEST_HOST="http://127.0.0.1:8001",
                      DEBUG="1")
    update_env(**env_kwargs)
    c.run("ansible-playbook .200_deploy/200.yaml")
