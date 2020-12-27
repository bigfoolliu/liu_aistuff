/**********************************
Author: bigfoolliu
Description: 进制转换
**********************************/


#include <stdio.h>


// 输入年龄，输出一共的秒数
float count_age_seconds(int age) {
    float seconds = age * 365 * 24 * 3600;
    return seconds;
}



int main(int argc, char const *argv[])
{

    // 格式化输出展示
    int x = 100;
    printf("dec十进制：%d\n", x);  // 100
    printf("oct八进制：%o\n", x);  // 144
    printf("hex十六进制：%x\n", x);  // 64

    // 显示0和0x前缀
    printf("oct八进制：%#o\n", x);  // 0144
    printf("hex十六进制：%#x\n", x);  // 0x64

    // long long y = 100000000000000000;
    // printf("%lf", y);


    // 输入ascii码值，输出对应字符
    printf("%c\n", 65);  // A

    printf("\a");


    int my_age = 20;
    float ret = count_age_seconds(my_age);
    printf("seconds: %.fs\n", ret);

    return 0;
}
