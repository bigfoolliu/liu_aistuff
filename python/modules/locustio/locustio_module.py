#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: bigfoolliu


'''
主页： https://docs.locust.io/en/stable/

压力测试框架,有web ui
'''


from locust import HttpLocust, TaskSet, between, task


# 定义的用户行为集合
class UserBehavior(TaskSet):
    '''用户单次需要执行的任务'''

    def on_start(self):
        '''当所有任务集合开始之前调用'''
        self.login()
    
    def on_stop(self):
        '''当所有任务完成之后调用'''
        self.logout()
    
    # 定义的一些locust任务，参数是Locust类实例
    @task
    def login(self):
        self.client.post('/login', {'username': 'liu', 'password': 'liu941103'})
    
    @task
    def logout(self):
        self.client.post('/logout', {'username': 'liu', 'password': 'liu941103'})

    @task
    def index(self):
        self.client.get('/')

    @task
    def profile(self):
        self.client.get('/profile')


class WebsiteUser(HttpLocust):
    '''定义的一个虚拟用户，包含其需要执行的任务和每次执行任务的时间间隔'''
    task_set = UserBehavior
    wait_time = between(5.0, 9.0)
