#!/usr/bin/env python3
# -*- coding:utf-8 -*-


import logging

# basicConfig() 在程序中只能被执行一次。如果你稍后想改变日志配置，就需要先
# 获取 root logger ，然后直接修改它。例如：
# logging.getLogger().level = logging.DEBUG

logging.basicConfig(
    filename="log.log",
    level=logging.ERROR  # 过滤参数，严重级别低于ERROR的都会被过滤
)


# 当从配置文件中读取logging的配置时候
# logging.config.fileConfig('logconfig.ini')


def main():
    hostname = 'www.python.org'
    item = 'spam'
    filename = 'data.csv'
    mode = 'r'

    # Example logging calls (insert into your program)
    # 严重级别是以降序排列
    logging.critical('Host %s unknown', hostname)
    logging.error("Couldn't find %r", item)
    logging.warning('Feature is deprecated')
    logging.info('Opening file %r, mode=%r', filename, mode)
    logging.debug('Got here')


if __name__ == '__main__':
    main()


import time
time.perf_counter()