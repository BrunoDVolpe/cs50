#include <stdio.h>

/* Prototype */
void swap(int a, int b);
void swap2(int *a, int *b);

int main(void)
{
    int x = 1;
    int y = 2;

    printf("x is %i, y is %i\n", x, y);
    swap(x,y);
    printf("x is %i, y is %i\n", x, y);
    swap2(&x, &y);
    printf("x is %i, y is %i\n", x, y);
}

void swap(int a, int b)
{
    int tmp = a;
    a = b;
    b = tmp;
    /* A função nesse estilo não funciona. Ela pega os valores de x e y, copia eles para a e b.
    As variáveis a e b tem seus valores trocados e assim que a função swap termina, automaticamente os valores a e b
    sao consideradas garbage values. Portanto, para que funcione essa função, podemos trabalhar com pointers */
}

void swap2(int *a, int *b)
{
    int tmp = *a;
    *a = *b;
    *b = tmp;
}