#!/usr/bin/env python
#!coding:utf-8


"""
实时从摄像头中捕捉人脸
"""
import face_recognition as face_r
import cv2


SAMPLE_IMAGE = "./known_images/tongliya.jpeg"
print("[INFO]Use file {}".format(SAMPLE_IMAGE))

# 使用摄像头(注意虚拟机的话需要打开摄像头设备)
video_capture = cv2.VideoCapture(0)
print("[INFO]video_capture: {}".format(video_capture))

# 加载一张模板图片并辨别(可加载多张)
tongliya_image = face_r.load_image_file(SAMPLE_IMAGE)
tongliya_face_encoding = face_r.face_encodings(tongliya_image)[0]
print("[INFO]tonyliya_image: {},tongliya_face_encoding: {}".format(tongliya_image, tongliya_face_encoding))

# 创建已知图片面部的数组以及名字
known_face_encodings = [tongliya_face_encoding]
known_face_names = ["tongliya"]


# 初始化相关变量
print("[INFO]Begin to initialize some variables.")
face_locations = []
face_encodings = []
face_names = []
process_this_frame = True


print("[INFO]Begin to capture video")
while True:
    # 从摄像头抓取单帧并处理
    ret, frame = video_capture.read()
    print("[INFO]ret: {}, frame: {}".format(ret, frame))
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)  # 图片缩小
    rgb_small_frame = small_frame[:, :, ::-1]  # 将图片从BGR颜色(opencv使用)转换为rgb颜色(face_recognition使用)

    # 处理部分帧以节约时间
    if process_this_frame:
        face_locations = face_r.face_locations(rgb_small_frame)
        face_encodings = face_r.face_encodings(rgb_small_frame, face_locations)

        face_names = []
        for face_encoding in face_encodings:
            # 判断是否匹配已知的面部
            matches = face_r.compare_faces(known_face_encodings, face_encoding)
            name = "Unknown"

            # 如果有一个匹配,则使用第一个匹配的
            if True in matches:
                first_match_index = matches.index(True)
                name = known_face_names[first_match_index]

            face_names.append(name)

    process_this_frame = not process_this_frame

    # 展示结果
    for (top, right, bottom, left), name in zip(face_locations, face_names):
        top += 4
        right += 4
        bottom += 4
        left += 4

        # 在发现的面部画个方框
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

        # 放置一个面部的名字
        cv2.rectangle(frame, (left, bottom-35), (right, bottom), (0, 0, 255), cv2.FILLED)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, name, (left+6, bottom-6), font, 1.0, (255, 255, 255), 1)
    # 展示图片结果
    cv2.imshow("Video", frame)

    # 按q键来退出
    if cv2.waitKey(1) & 0xff == ord("q"):
        break

# 释放摄像头
video_capture.release()
cv2.destroyAllWindows()


