/* Fiz esse exercício por conta própria, como uma forma de usar pointers de uma forma diferente.
A idéia era comparar duas strings. Como char * é um pointer, quando comparo um pointer com outro sempre dará diferente
já que cada um aponta para um endereço. Quando eu uso o dereference, eu comparo o char em si.*/

#include <stdio.h>
#include <cs50.h>
#include <string.h>
#include <ctype.h>

int main(void)
{
    char *s = get_string("s: ");
    char *t = get_string("t: ");
/*
    Modelo mostrando o erro ao comparar dois pointers
    if (s == t)
    {
        printf("Same\n");
    }
    else
    {
        printf("Different\n");
    }
*/
/*Modelo que eu fiz*/
/*
    int i = 0;
    while(true)
    {
        if (*(s+i) != *(t+i))
        {
            printf("Different\n");
            return 1;
        }
        if (*(s+i) == 0 && *(t+i) == 0)
        {
            printf("Same\n");
            return 0;
        }
        i++;
    }
*/
/*Usando strcmp()*/
/*Essa função retorna 0 quando são strings iguais e >0 ou <0 na primeira comparação de char que forem diferentes*/
/*
    if (strcmp(s, t) == 0)
    {
        printf("Same\n");
    }
    else
    {
        printf("Different\n");
    }
*/

}