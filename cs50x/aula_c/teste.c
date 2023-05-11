// strings são conjuntos de arrays. O compilador entende que a array termina quando encontra um \0.
// Por isso, posso pegar letra por letra da string como um 'char'. Porém quando especifico que é um 'char' o computador
// interpreta os 0's e 1's de uma forma; quando digo que são 'integers' ele interpreta como números. Abaixo essa
// demonstração.

#include <cs50.h>
#include <stdio.h>

int main(void)
{
    string name = get_string("What's your name? ");

    int n = 0;
    while(name[n] != '\0')
    {
        printf("%c -> %i\n", name[n], name[n]);
        n++;
    }
}

