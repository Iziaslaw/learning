#include <stdio.h>

int main(void)
{
    printf("Hello, World3!\n");    
    int value = getchar();
    int res = putchar(value);
    printf("\n%d %c\n", res, res);
    return 0;
}