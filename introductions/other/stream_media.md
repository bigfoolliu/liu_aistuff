# 流媒体知识介绍

<!-- TOC -->

- [流媒体知识介绍](#流媒体知识介绍)
    - [流媒体协议-rtmp](#流媒体协议-rtmp)
        - [基础概念](#基础概念)
        - [RTMP地址规则](#rtmp地址规则)
    - [常用直播协议差别：](#常用直播协议差别)
    - [相关术语](#相关术语)
    - [流媒体介绍](#流媒体介绍)
        - [流媒体网络播放方式](#流媒体网络播放方式)
        - [流媒体文件格式](#流媒体文件格式)
        - [流媒体编码解码技术](#流媒体编码解码技术)
        - [流媒体节目制作](#流媒体节目制作)
    - [ffmpeg](#ffmpeg)
        - [处理RTMP流媒体命令大全](#处理rtmp流媒体命令大全)
        - [码率控制](#码率控制)

<!-- /TOC -->

## 流媒体协议-rtmp

### 基础概念

1. 应用层协议
2. 用于通过因特网在Flash播放器和服务器之间传输音频，视频和数据，默认使用TCP端口号1935。
3. 相对于 HLS 来说，采用 RTMP 协议时，从采集推流端到流媒体服务器再到播放端是一条数据流，因此在服务器不会有落地文件。这样 RTMP 相对来说就有这些优点：

    - 延时较小，通常为 1-3s。
    - 基于 TCP 长连接，不需要多次建连。
    - 因此业界大部分直播业务都会选择用 RTMP 作为流媒体协议。通常会将数据流封装成 FLV 通过 HTTP 提供出去。但是这样也有一些问题需要解决：iOS 平台没有提供原生支持 RTMP 或 HTTP-FLV 的播放器，这就需要开发支持相关协议的播放器。

### RTMP地址规则

1. rtmp://域名或ip:端口(没有则默认为1935)/应用名/串流名称
2. rtmp://域名或ip:端口(没有则默认为1935)/串流名称

## 常用直播协议差别：

- HLS：HTTP Live Streaming；基于短连接 HTTP；集合一段时间的数据生成 ts 切片文件，更新 m3u8 文件；延时 25s+。
- RTMP：Real Time Messaging Protocal；基于长连接TCP；每个时刻收到的数据立即转发；延时 1~3s。
- HTTP-FLV: RTMP over HTTP；基于长连接 HTTP；每个时刻收到的数据立即转发，使用 HTTP 协议；延时 1~3s。

## 相关术语

推流：将直播内容推送至服务器的过程
拉流：服务器已有直播内容，用指定地址拉取的过程

`编码格式`：

- 视频文件通常由视频和音频组成。常见的视频编码格式有AVC/H264，MPEG1，MPEG2等。

`码流/码率`：

- 视频文件在单位时间使用的数据流量，即取样率，单位为Kb/s或Mb/s。
- 同样分辨率下，码率越大则压缩比越小，画面质量越高，处理出来的文件越接近原始文件，同时要求播放设备的解码能力要越高

`采样率`：

- 定义了每秒从连续信号中提取并组成离散信号的采样个数，单位为Hz
- 类似于动态影像的帧数，采样率越高则听到的声音和看到的图像越连贯

`比特率`：

- 每秒传输的比特(bit)数，单位为bps(bit/s)
- 比特率越高则传送的数据越大，音视频的质量则越好
- 表示经过编码后（常见的为 VBR, ABR, CBR）的音视频每秒钟要多少个比特来表示

| 分辨率  | 码率    |
| --------|: -----:|
| 360p    | 400    |
| 480p    | 600    |
| 540p    | 700    |
| 720p    | 1000   |
| 1080p   | 1500   |

`帧速率`：

- 每秒钟刷新的图片帧数，单位为FPS(frame/s)
- 帧率越高则画面越流畅

`分辨率`：

- 常说的600*400,1920*1080
- 分辨率影响视频图像的大小，与视频图像大小成正比，分辨率越大则图像越大，对应的视频文件越大

## 流媒体介绍

### 流媒体网络播放方式

1. 单播(Singlecast)，一个服务器对应一个客户机
2. 组播(Multicast)，网络中的所有客户端共享同一流
3. 点播(Unicast)，用户通过选择内容项目来初始化客户端连接，用户可以开始，停止，后退，快进或暂停流
4. 广播(Broadcast)，客户端接收流，但不能控制流
5. 点播单播，客户端连接到服务器接收特定内容
6. 广播单播，客户端通过发布点上的别名访问流
7. 广播组播，被动的用户通过监视特定的IP地址接收组播ASF流

### 流媒体文件格式

多媒体压缩格式：.mpeg, .avi, .mp4等
流媒体格式：.rm, .rmvb, .asf等，是将多媒体格式切割成多块进行传输

### 流媒体编码解码技术

流媒体的质量和网络带宽矛盾，因此编解码技术至关重要。

标准一：国际电联(ITU-T)的标准，H.261, H.263, H.264等
标准二：ISO的标准，Mpeg-1, Mpeg-2, Mpeg-4等

### 流媒体节目制作

常用数字视频格式：

- AVI格式(.avi), 使用开放性的标准，扩充性好，兼容性好，调用方便，图像质量好，相对文件尺寸较大
- MPEG格式(.mpeg, .mpg, .dat等)，广泛应用于VCD制作以及视频片段网络下载
- RM/RMVB格式(.rm, .rmvb)，主要用于在低速率的网络上实时传输影像
- ASF格式/WMV格式(.asf, .wmv)，流行的网络流媒体格式
- MOV格式(.mov), 主要用于Mac平台，视频编码性能优良
- SWF(.swf)，使用Flash的一种发布格式，体积小，功能强，交互能力好，主要用于MTV，网上游戏，动画等
- 其他

## ffmpeg

### 处理RTMP流媒体命令大全

```shell
# 1.将文件当作直播送至live
ffmpeg -re -i localfile.mp4 -c copy -f flv rtmp://server/live/streamName

# 2.将直播媒体保存至本地文件
ffmpeg -i rtmp://server/live/streamName -c copy dump.flv

# 3.将其中的一个直播流，视频改用h264压缩，音频不变，送至另外一个直播服务流
ffmpeg -i rtmp://server/live/streamName -c:a copy -c:v libx264 -vpre slow -f flv rtmp://server/live/h264Stream

# 4.将其中的一个直播流，视频改用h264压缩，音频改用faac压缩，送至另外一个直播流
ffmpeg -i rtmp://server/live/streamName -c:a libfaac -ar 44100 -ab 48k -c:v libx264 -vpre slow -vpre baseline -f flv rtmp://server/live/h264stream

# 5.将其中的一个直播流，视频不变，音频改用faac压缩，送至另外一个直播流
ffmpeg -i rtmp://server/live/streamName -acodec libfaac -ar 44100 -ab 48k -vcodec copy -f flv rtmp://server/live/h264_acc_stream

# 6.将一个高清流复制为几个不同视频清晰度的流重新发布，其中音频不变
ffmpeg -re -i rtmp://server/live/high_stream -acodec copy -vcodec x264lib -s 640x360 -b 500k -vpre medium -vpre baseline rtmp://server/live/baseline_500k -acodec copy -vcodec x264lib -s 480x272 -b 300k -vpre medium -vpre baseline rtmp://server/live/baseline__300k -acodec copy -vcodec x264lib -s 320×200 -b 150k -vpre medium -vpre baseline rtmp://server/live/baseline_150k -acodec libfaac -vn -ab 48k rtmp://server/live/audio_only_AAC_48k

# 7.将当前摄像头及音频通过DSSHOW采集，视屏h264，音频faac压缩后发布
ffmpeg -r 25 -f dshow -s 640x480 -i video="video_source_name":audio="audio_source_name" -vcodec libx264 -b 600k -vpre slow -acodec libfaac -ab 128k -f flv rtmp://server/live/streamName

# 8.将普通流视频改为h264压缩，音频不变，送至高清流服务器
ffmpeg -i rtmp://server/live/streamName -c:a copy -c:v libx264 -vpre slow -f flv rtmp://server/live/h264stream
```

### 码率控制

VBR：动态码率
CBR：静态码率

[动态码率参考博文](https://slhck.info/video/2017/03/01/rate-control.html)

```shell
ffmpeg -i input.mp4 -c:v libx264 -x264-params "nal-hrd=cbr" -b:v 1M -minrate 1M -maxrate 1M -bufsize 2M output.ts
```
