#include <stdio.h>
#include <cs50.h>
#include <string.h>
#include <ctype.h>

int main(int argc, string argv[])
{
    if (argc != 2)
    {
        printf("Usage: ./substitution key");
        return 1;
    }
    else if (strlen(argv[1]) != 26)
    {
        printf("The key must have 26 characters\n");
        return 1;
    }
    //validar se cada letra repete uma vez e que só tenha letras.
    for (int i = 0, n = strlen(argv[1]); i < n; i++)
    {
        if (isalpha(argv[1][i]))
        {
            //validar se repete.
            for (int j = i + 1; j < n; j++)
            {
                if (argv[1][i] == argv[1][j])
                {
                    printf("Substitution key must not contain repeated chars\n");
                    return 1;
                }
            }
        }
        else
        {
            printf("Substitution key must contain only alphabetical chars\n");
            return 1;
        }
    }

    //Getting plain text
    string text = get_string("plaintext: ");

    //cipher process
    printf("ciphertext: ");
    int indice;
    for (int i = 0, n = strlen(text); i < n; i++)
    {
        //iterando no texto
        if (isalpha(text[i]))
        {
            //lowercase char from text
            if (islower(text[i]))
            {
                // transforma em int, tira 97 e será o índice da cifra. Pega a cifra e converte para lower.
                indice = (int) text[i] - 97;
                printf("%c", tolower(argv[1][indice]));
            }
            //uppercase char from text
            else
            {
                // transforma em int, tira 65 e será o índice da cifra. Pega a cifra e converte para upper.
                indice = (int) text[i] - 65;
                printf("%c", toupper(argv[1][indice]));
            }
        }
        else
        {
            //não texto
            printf("%c", text[i]);
        }
    }

    printf("\n");
    return 0;
}