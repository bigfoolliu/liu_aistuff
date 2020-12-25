// 数组和字符串示例

#include <stdio.h>


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
}