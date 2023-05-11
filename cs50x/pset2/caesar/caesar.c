#include <stdio.h>
#include <cs50.h>
#include <ctype.h>
#include <string.h>
#include <stdlib.h>

int main(int argc, string argv[])
{
    // checking the arguments of the commandline. Must be one positive integer.
    if (argc != 2)
    {
        printf("Usage: ./caesar key\n");
        return 1;
    }
    for (int i = 0, n = strlen(argv[1]); i < n; i++)
    {
        if (isdigit(argv[1][i]) == false)
        {
            printf("Use: ./caesar key\n");
            return 1;
        }
    }

    // getting k and converting to a range up to 26 (alphabet range)
    int k = atoi(argv[1]);
    k = k % 26;

    //Getting plain text
    string text = get_string("plaintext: ");
    printf("ciphertext: ");

    //cipher process
    int int_char;
    for (int i = 0, n = strlen(text); i < n; i++)
    {
        if (isalpha(text[i]))
        {
            //resolving for uppercase
            if ((int) text[i] >= 65 && (int) text[i] <= 90)
            {
                int_char = (int) text[i] + k;
                if (int_char > 90)
                {
                    int_char -= 26;
                }
                printf("%c", (char) int_char);
            }
//            else if ((int) text[i] >= 97 && (int) text[i] <= 122)
            else
            {
                //resolving for lower case
                int_char = (int) text[i] + k;
                if (int_char > 122)
                {
                    int_char -= 26;
                }
                printf("%c", (char) int_char);
            }
        }
        else
        {
            printf("%c", text[i]);
        }
    }
    printf("\n");
    return 0;
}