/**********************************
Author: bigfoolliu
Description:
**********************************/


// 数组和字符串示例

#include <stdio.h>
#include <string.h>

int string_demo(void){
    // 字符串操作示例
    char s1[] = "c is nice";
    char s2[] = "c ++";

    printf("length: %d\n", (unsigned int)strlen(s1));  // 字符串长度,注意中英文长度不一样
    printf("compare s1 s2: %d\n", strcmp(s1, s2));  // 比较字符串,会将字符串转换为ascii码比较

    // strcat(s1, s2);  // strcat在使用时s1与s2指的内存空间不能重叠，且s1要有足够的空间来容纳要复制的字符串
    // printf("strcat s1: %s s2: %s\n", s1, s2);
    return 0;
}


int array_demo(void){
    // 数组示例
    int arr[] = {2, 3, 5, 7, 11};

    // 一种计算长度的方式
    int arr_length = sizeof(arr)/sizeof(arr[0]);
    printf("arr length is: %d\n", arr_length);


    int i = 0;
    for(i=0;i<arr_length;i++){
        printf("&arr[%d] = %p\n", i, &arr[i]);  // 输出元素的地址,可以看到地址为递增的
    }

    return 0;
}



int main(int argc, char *argv[]) {  // argc表示传入参数的个数，*argv[]代表传入的具体参数，使用 ./hello arg1 arg2
    char numbers[5] = {2};

    char names[3] = {'a', 'b', 'x'};  // 实际是手动构造了一个字符串

    printf("numbers[0] is %d\n", numbers[0]);

    printf("names are %c\n", names[0]);
    printf("names is %s\n", names);


    // 循环输出传入的参数
    int i = 0;
    for (i = 1; i < argc; i++){
        printf("arg %d: %s\n", i, argv[i]);   
    }

    // string_demo();

    array_demo();
}

