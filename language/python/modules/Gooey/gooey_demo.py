#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: bigfoolliu


from gooey import Gooey, GooeyParser

@Gooey
def main():
    parser = GooeyParser(description='gooey demo gui')
    parser.add_argument("file_name", widget='FileChooser')
    args = parser.parse_args()
    print(args)


if __name__ == '__main__':
    main()
