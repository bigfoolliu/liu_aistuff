#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: bigfoolliu


from app import factory


app = factory.create_app()


if __name__ == '__main__':
    app.run()
