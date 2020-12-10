// 输出
const x = 'x';
console.log(x);


// 数组输出
const oranges = ['orange', 'orange']
const apples = ['just one apple']
oranges.forEach(fruit => {
  console.count(fruit)
})
apples.forEach(fruit => {
  console.count(fruit)
})



// 查看调用堆栈
const function2 = () => console.trace()
const function1 = () => function2()
function1()


// 计算耗时
const doSomething = () => console.log('test')
const measureDoingSomething = () => {
  console.time('doSomething()')
  //do something, and measure the time it takes
  doSomething()
  console.timeEnd('doSomething()')
}
measureDoingSomething()


// 让输出带颜色
const chalk = require('chalk')
console.log(chalk.yellow('hi!'))
