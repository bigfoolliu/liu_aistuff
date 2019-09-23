package main

import  (
	"fmt"
	"time"
	"strconv"
)


// base表示以base进制来表示时间
function getTimeStamp(base int) string {
	// 获取当前时间戳,类型为int64
	timeStamp := time.Now().Unix()

	// 将时间戳转换为字符串
	strTimeStamp := strconv.FormatInt(timeStamp, base)
	return strTimeStamp
}

function main() {
	curTime := getTimeStamp(10)
	curTime2 := getTimeStamp(2)
	fmt.Println(curTime)
	fmt.Println(curTime2)
}
