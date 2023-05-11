#include <stdio.h>
#include <cs50.h>
#include <stdlib.h>
#include <ctype.h>
#include <string.h>

int main(void)
{
    char *s = get_string("s: ");

    char *t = malloc(strlen(s) + 1);
    if (t == NULL)
    {
        return 1;
    }

    /* fazendo manualmente */
    for (int i = 0, n = strlen(s); i <= n; i++)
    {
        *(t + i) = *(s + i);
        /* t[i] = s[i]; */
    }

    /* Simplificando o loop com uma função: strcpy() */
    /* strcpy(t, s) */

    if (strlen(t) > 0)
    {
        t[0] = toupper(t[0]);
    }

    printf("s: %s\n", s);
    printf("t: %s\n", t);
    printf("s - memory: %p\n", s);
    printf("t - memory: %p\n", t);

    free(t);
}