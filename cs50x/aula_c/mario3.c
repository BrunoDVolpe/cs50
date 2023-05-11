#include <stdio.h>
#include <cs50.h>

void draw1(int h);
void draw2(int h);

int main(void)
{
    int height = get_int("Height: ");
    /*draw1(height);*/
    draw2(height);
}

void draw1(int h)
{
    /* usando loop, recurso da semana 2 */
    for (int i = 1; i <= h; i++)
    {
        for (int j = 1; j <= i; j++)
        {
            printf("#");
        }
        printf("\n");
    }
}

void draw2(int h)
{
    /* usando recursion */
    /* Correção do erro na memória */
    /*
    if (h == 0)
    {
        return;
    }
    */

    draw2(h - 1);

    for (int i = 0; i < h; i++)
    {
        printf("#");
    }
    printf("\n");
}