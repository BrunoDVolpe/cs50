#include <stdio.h>
#include <stdlib.h>

int main(void)
{
    char *s = malloc(3);
    /*char *s = malloc(4);*/
    s[0] = 'H';
    s[1] = 'I';
    s[2] = '!';
    s[3] = '\0';
    printf("%s\n", s);
    /*free(s);*/

    /* O código compila e 'check50' não acusaria erro, mas tem 2 erros gritantes aqui
     O primeiro é que a memória está menor do que deveria (deveria ser 4 bytes)
     O segundo é porque não estamos encerrando o malloc com a função free()
     Rodar o valgrind e analisar o retorno dele: valgrind ./memory
     Erro de read / write por conta da memória que estamos mexendo além do que pedimos; e erro de memory leak,
    ou seja, uso de memória sem liberar ela ao final do programa */

    /* Comparar o valgrind quando o programa está correto
     - mudar malloc para 4 bytes
     - inserir free(s) depois de print, antes de terminal o programa */
}