#!/bin/bash

# ubuntu安装docker

# 卸载原始的版本
sudo apt-get remove docker \
    docker-engine \
    docker.io

# 安装必要的依赖
sudo apt-get update
sudo apt-get install apt-transport-https \
    ca-certificates \
    curl \
    software-properties-common

# 安装docker-ce
sudo apt-get install docker-ce