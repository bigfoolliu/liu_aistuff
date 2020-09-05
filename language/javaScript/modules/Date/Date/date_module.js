// 需要实例化之后使用
let cur_date = new Date();
console.log('当前时间为' + cur_date);

// 带参数就是指定的时间
let date = new Date(2020, 6, 1, 12, 0, 0);
console.log(date);

// 传递时间其他格式
let date1 = new Date('2020/08/12 12:00:05');
let date2 = new Date('2020-07-08');

const date3 = new Date(1591950413388);

// getFullYear()	获取年份	
// getMonth()	获取月： 0-11	0代表一月
// getDate()	获取日：1-31	获取的是几号
// getDay()	获取星期：0-6	0代表周日，1代表周一
// getHours()	获取小时：0-23	
// getMinutes()	获取分钟：0-59	
// getSeconds()	获取秒：0-59	
// getMilliseconds()	获取毫秒	
