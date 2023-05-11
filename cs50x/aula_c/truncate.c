#include <stdio.h>
#include <cs50.h>

int main(void)
{
    //get numbers from user
    int x = get_int("x: ");
    int y = get_int("y: ");

    //divide x by y
//    float z = x / y conta sai errada, porque ele primeiro divide dois inteiros, descartando a parte decimal.
    float z = (float) x / (float) y;
    printf("%f\n", z);
}