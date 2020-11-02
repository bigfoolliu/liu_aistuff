#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: bigfoolliu


import sys
import os

print(sys.path)

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

print(sys.path)


from package1.module_p1 import test_pkg1



print(f'package2 module_p2: {__name__}')


if __name__ == '__main__':
    test_pkg1()

