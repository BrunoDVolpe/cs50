#include <stdio.h>
#include <cs50.h>

int main(void)
{
    int start_size;
    int end_size;
    do
    {
     // TODO: Solicite o valor inicial ao usuário
        start_size = get_int("Valor inicial: ");
    } while(start_size < 9);

     // TODO: Solicite o valor final ao usuário
    do
    {
        end_size = get_int("Valor final: ");
    } while (end_size < start_size);

     // TODO: Calcule o número de anos até o limite
    int years = 0;
    while(start_size < end_size)
    {
        start_size = start_size + start_size/3 - start_size/4;
        years++;
    }

     // TODO: Imprima o número de anos
    printf("Years: %i\n", years);
}