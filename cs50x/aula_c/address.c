/*Aula 4 - Memory - https://www.youtube.com/watch?v=AcWIE9qazLI */
#include <cs50.h>
#include <stdio.h>

void example2(void);
void example3(void);

int main(void)
{
    int n = 50;
    printf("--Main--\n");
    printf("%p\n", &n);
    printf("--Example2--\n");
    example2();
    printf("--Example3--\n");
    example3();
}

/* %p vai referenciar um tipo de caractér que corresponde a memória */
/* & é o caractere que pede o lugar da memória onde está armazenado determinada variável, no exemplo a variável n */
/* A resposta vem com o prefixo '0x' que foi criado para indicar que o código que vem depois é um hexadecimal. */
/* Isso foi criado para evitar confusões entre decimal e hexadecimal para representações que podem ser lidas em ambos*/
/* Para cancelar o efeito de &n, podemos usar o * -> printf("%i\n", *&n); que seria o mesmo de printf("%i\n", n); */

/* Variável pointer */

void example2(void)
{
    int n = 50;
    int *p = &n;
    printf("%p\n", p);
}

void example3(void)
{
    string s = "HI!";
    printf("%s\n", s);
    printf("%p\n", &s);
    printf("-----\n");
    printf("%p\n", &s[0]);
    printf("%p\n", &s[1]);
    printf("%p\n", &s[2]);
}