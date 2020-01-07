let ws = require("nodejs-websocket")

let server = ws.createServer((conn) => {
    // console.log("a client connected")

    // 服务端接受数据
    conn.on("text", (str)=>{
        console.log(str)
    })


    // 服务端发送数据
    setTimeout(()=>{
        conn.sendText("message from server")
    }, 5000)

}).listen(2333, () =>{
    console.log("the server is listening on 2333")
})
