// 变量类型和格式化输出示例

#include <stdio.h>

int main() {
    int age = 10;
    printf("i am %d years old.\n", age);

    float distance = 1.23f;
    printf("the distance is %f.\n", distance);

    double power = 2323111.12;
    printf("the power is %f.\n", power);

    char a = 'A';  // 注意为单引号
    printf("the a is %c.\n", a);  // 注意为%c

    char name[] = "tony";  // c中的字符串就是字节数组
    printf("the name is %s.\n", name);  // %s

    char *name2 = "jane";
    printf("the name is %s.\n", name2);

    // 定义自己的数组
    char *names3[] = {"tony", "anna", "jane"};
    for (int i = 0; i < 3; i++) {
        printf("name is %s\n", names3[i]);
    }
}
