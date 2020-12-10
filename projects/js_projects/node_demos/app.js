// node.js官方示例

const http = require('http');
const process = require('process')

const hostname = '127.0.0.1';
const port = 3001;

const server = http.createServer((req, res) => {
  res.statusCode = 200;
  res.setHeader('Content-Type', 'text/plain');
  res.end('Hello World');
});

// server.listen(port, hostname, () => {
//   console.log(`Server running at http://${hostname}:${port}/`);
// });


console.log('start');

console.log(Number);

// process, 强制退出
process.exitCode = 1;
process.exit();

console.log('exit');

