// Tipo simples do que poderia ser uma criptografia, com command-line
#include <cs50.h>
#include <stdio.h>

int main(int argc, string argv[])
{
//    string name = get_string("What's your name? ");
    string name = argv[1];
    int i = 0;
    while(name[i] != '\0')
    {
        printf("%c", (name[i] + 5));
        i++;
    }
    printf("\n");
}