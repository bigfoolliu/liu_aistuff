package main

import (
	"log"
	"net/http"
	"time"

	"./setting"
	"gopkg.in/macaron.v1"
)

// Person 示例
type Person struct {
	Name string `json:"id"`
	Age  int    `json:"age"`
	Sex  string `json:"sex"`
}

func main() {
	m := macaron.Classic()
	m.Use(macaron.Static("static"))
	m.Use(macaron.Renderer())

	m.Get("/", myHandler)
	m.Get("/hello", helloHandler)
	m.Get("/json", jsonHandler)

	log.Println("server is running on ", setting.Server)
	// log.Println(http.ListenAndServe("0.0.0.0:4000", m))
	log.Println(http.ListenAndServe("127.0.0.1:4000", m))
}

func myHandler(ctx *macaron.Context) string {
	return "the result path is: " + ctx.Req.RequestURI
}

func helloHandler(ctx *macaron.Context) {
	ctx.Data["time"] = time.Now().UTC()
	ctx.HTML(200, "hello")
}

func jsonHandler(ctx *macaron.Context) {
	p := Person{"tony", 20, "male"}
	ctx.JSON(200, &p)
}
