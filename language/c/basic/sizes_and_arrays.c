/**********************************
Author: bigfoolliu
Description:
**********************************/


// 大小和数组的示例

#include <stdio.h>

int main(int argc, char *argv[]){
    int areas[] = {1, 2, 4, 5};
    char name[] = "tony";

    printf("the size of int is %ld\n", sizeof(int));  // 占用空间大小，单位为字节, 注意

    printf("the size of areas is %ld\n", sizeof(areas));

    printf("the size of name is %ld\n", sizeof(name));

}