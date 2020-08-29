#!/bin/bash

# 侦测整个网络的主机是否有响应,每个主机的响应时间只等1s

for siteip in $(seq 1 254)
do
    site="192.168.1.${siteip}"
    ping -c1 -W1 ${site} &> /dev/null
    if [ "$?" == "0" ]; then
        echo "$site is up"
    else
        echo "$site is down"
    fi
done
