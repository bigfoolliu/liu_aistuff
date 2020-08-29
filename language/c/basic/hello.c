// hello.c，介绍基础使用的文件

#include <stdio.h>
#include <stdlib.h>


void arrayDemo()
{
    int array[3] = {2, 3, 4};
    // printf("array: %d\n", array);
}


// 返回两个整数的和
int addFunc(int a, int b)
{
    int c;
    c = a + b;
    return c;
}


// 第一个void表示该函数无返回值
// 第二个void表示该函数不接受参数
void func1(void)
{
   printf("这个函数不接受参数，不返回值.\n");
}


// argc接受实参
int main(int argc, char * * argv)
{
    int a = 1;
    /* 我的第一个 C 程序 */
    printf("Hello, World! \n");
    printf("main: a=%d, argc=%d \n", a, argc);

    func1();

    int ret;
    ret = addFunc(a, argc);
    printf("ret: %d\n", ret);

    arrayDemo();

    return EXIT_SUCCESS;  // 定义在stdlib中
}



