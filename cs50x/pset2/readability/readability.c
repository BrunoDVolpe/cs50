#include <stdio.h>
#include <cs50.h>
#include <string.h>
#include <ctype.h>
#include <math.h>

int main(void)
{
    string s = get_string("Texto: ");
    int letras = 0, palavras = 1, sentencas = 0;

    for (int i = 0, n = strlen(s); i < n; i++)
    {
        if(isalpha(s[i]))
        {
            letras++;
        }
        else if (isspace(s[i]))
        {
            palavras++;
        }
        else if (s[i] == '.' || s[i] == '!' || s[i] == '?')
        {
            sentencas++;
        }
    }

//    printf("Letras: %i\nPalavras: %i\nSentencas: %i\n", letras, palavras, sentencas);
    float L = (float) letras / palavras * 100;
    float S = (float) sentencas / palavras * 100;
    int indice = round(0.0588 * L - 0.296 * S - 15.8);
//    printf("L: %f\nS: %f\n", L, S);

    if (indice >= 16)
    {
        printf("Grade 16+\n");
    }
    else if (indice < 1)
    {
        printf("Before Grade 1\n");
    }
    else
    {
        printf("Grade %i\n", indice);
    }
}