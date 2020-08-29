// 变量使用，变量声明使用let来替换var

// 布尔值
let isPass: Boolean = true;


// 数字，typescript里面所有的数字都是浮点数
let num: number = 10;
let num1: number = 0.5;

// 字符串
let str1: string = "hello";

// 数组
let l1: number[] = [1, 3, 4];
let l2: Array<number> = [2, 3, 4]


// 元组
let t1: [string, number];

// 枚举类型
enum Color {red=1, green=2, yellow=3};
let c: Color = Color.green;

// 不知道类型时候的任意类型
let x: any = 4;
let lx: any[] = ["a", 2];

// 函数返回值没有类型
function logName(): void {
    console.log("No name");
}

// null和undefined，是所有类型的子类型
let u: undefined = undefined;
let n: null = null;


// never，表示那些永远不存在的值的类型
// object表示非原始类型

console.log(isPass, num, num1, str1, l1[1], c);
logName();
