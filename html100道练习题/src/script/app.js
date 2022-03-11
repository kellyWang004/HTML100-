const express = require("express");
const app = express();
// 创建路由规则：
//request 是对请求报文的封装；
//response 是对响应报文的封装；
app.get("/server",(request,response)=>{
    // 设置响应头,设置允许跨域
    response.setHeader("Access-Control-Allow-Origin","*");
    // 设置响应体
    response.send("Hello Ajax");
});
// 监听端口启动服务
app.listen(8849,()=>{
    console.log("服务器已启动，8849端口监听中......");
});