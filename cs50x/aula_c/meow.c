#include <stdio.h>

int main(void)
{
    printf("conditional 'while':\n");
    int i = 0;
    while (i < 3)
    {
        printf("meow\n");
        i++;
    }

    printf("\nconditional 'for':\n");
    for(int j = 0; j < 3; j++)
    {
        printf("meow\n");
    }

    printf("\nconditional 'forever loop':\n");
    /*CTRL + C para cancelar a iteração*/
    while (true)
    {
        printf("meow\n");
    }
}