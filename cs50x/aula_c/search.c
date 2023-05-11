#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int numbers[] = {20, 500, 10, 5, 100, 1, 50};

    int n = get_int("Number: ");
    for(int i = 0; i < 7; i++)
    {
        if(numbers[i] == n)
        {
            printf("Found\n");
            return 0; //"int main" retorna 0 se for sucessedido ou diferente de 0 se for "erro". Por isso "int main..."
            //para checar, rodar o programa e, depois do resultado, colocar no terminal echo $?
            //Por padrão retorna 0, não precisava colocar, mas colocamos como reforço.
        }
    }
    printf("Not found\n");
    return 1;
}