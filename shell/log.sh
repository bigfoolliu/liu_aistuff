#!/bin/bash
# log.sh，定义几个简单的log等级

_log_level=2

DIE(){
        echo "critical: $1" >&2
        exit 1
}

INFO(){
        [ $_log_level -ge 2 ] && echo "info: $1" >&2
}

ERROR(){
        [ $_log_level -ge 1 ] && echo "error: $1" >&2
}

# set -x
INFO "this is info log!"
ERROR "this is error log!"

