package main

import (
	"fmt"
	"io/ioutil"
	"log"
	"os/exec"
	"reflect"
	"strings"
)

func simpleOutPut(path string) {
	cmd := exec.Command("cat", path)
	out, err := cmd.Output()
	if err != nil {
		log.Printf("error: %s\n", err)
		return
	}
	fmt.Printf("out: %s\ntype: %s\n", out, reflect.TypeOf(out))

}

func getOutPut(path string) error {
	// c := fmt.Sprintf("ls %s", path)
	// fmt.Printf("command: %s\n", c)

	fmt.Printf("path: %s\n", path)
	cmd := exec.Command("ls", path)

	// 获取输出对象，从该对象中读取输出结果
	stdout, err := cmd.StdoutPipe()

	if err != nil {
		log.Printf("StdoutPipe error: %s\n", err)
		return err
	}

	// 保证关闭输出流
	defer stdout.Close()

	// 运行命令,start不会等待命令完成
	if err := cmd.Start(); err != nil {
		log.Printf("cmd start error: %s\n", err)
		return err
	}

	// 读取输出结果
	opBytes, err := ioutil.ReadAll(stdout)
	if err != nil {
		log.Printf("read error: %s\n", err)
		return err
	}

	fmt.Printf("opBytes: %s\n", string(opBytes))
	return err
}

func oldGetCamType(camPath string) (string, error) {
	c := fmt.Sprintf("udevadm info --query=all --name=%s | grep ID_VENDOR_ID", camPath)
	fmt.Printf("command: %s\n", c)

	cmd := exec.Command("/bin/bash", "-c", c)
	err := cmd.Run()

	if err != nil {
		log.Printf("query camtype failed, %s is offline\n", camPath)
		return "error", err
	}
	return "done", nil
}

func getCamType(camPath string) (string, error) {
	c := fmt.Sprintf("udevadm info --query=all --name=%s | grep ID_VENDOR_ID", camPath)
	cmd := exec.Command(c)
	fmt.Printf("command: %s\n", c)
	out, err := cmd.Output()
	if err != nil {
		return "", err
	}
	return string(out), err
}

// strSplit 对字符串进行分割操作
func strSplit(s string) {
	out := strings.Split(s, "=")
	fmt.Println("ret: ", out)
}

func main() {
	// camPath := "/dev/v4l/by-id/usb-C-ASPIRE_EP28WD_ASPIRE201907120017-video-index0"
	// ret, err := getCamType(camPath)
	// fmt.Printf("ret: %s\nerror: %s\n", ret, err)

	// path := os.Args[1]
	// err := getOutPut(path)
	// if err != nil {
	// 	fmt.Printf("get out put error: %s\n", err)
	// }

	// getCamType(path)

	s := "E: ID_VENDOR_ID=1871"
	strSplit(s)
}
