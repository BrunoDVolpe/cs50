#include <cs50.h>
#include <stdio.h>
#include <ctype.h>

void exemplo_string(void);
void alterar_string_bug(void);

int main(void)
{
    /*int x = get_int("What's x? ");
    int y = get_int("What's y? ");

    if (x < y)
    {
        printf("x is less than y\n");
    }
    else if (x > y)
    {
        printf("x is greater than y\n");
    }
    else
    {
        printf("x is equal to y\n");
    } */
    printf("--exemplo_string--\n");
    exemplo_string();
    printf("--Alterar string. Altera para as duas:--\n");
    alterar_string_bug();

}

void exemplo_string(void)
{
    char *s = get_string("s: ");
    char *t = get_string("t: ");

    if(s == t)
    {
        printf("equal\n");
    }
    else
    {
        printf("different\n");
    }
    printf("diferentes porque estamos comparando endereços na memória\n");
    printf("%p\n", s);
    printf("%p\n", t);
}

void alterar_string_bug(void)
{
    char *s = get_string("s: ");
    char *t = s;

    t[0] = toupper(t[0]);

    printf("s (string): %s\n", s);
    printf("t (string): %s\n", t);
    printf("s - memory: %p\n", s);
    printf("t - memory: %p\n", t);
    printf("Veja como copiar em copy.c\n");
}