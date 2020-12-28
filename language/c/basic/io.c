/**********************************
Author: bigfoolliu
Description:
**********************************/



#include <sys/types.h>
#include <sys/stat.h>

#include <fcntl.h>  // for open
#include <unistd.h>  // for close
#include <stdio.h>



int open_demo(){
    int fd=open("./hello.c",O_RDWR+O_CREAT);
    if(fd==-1){
        printf("can not open the file\n");
        return 1;
    }
    printf("successful to open the file, fd: %d\n", fd);
    close(fd);
    return 0;
}


int main(void)
{
    open_demo();
    return 0;
}
