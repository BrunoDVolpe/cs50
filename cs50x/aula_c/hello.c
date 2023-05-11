/*biblioteca e manual de C:manual.cs50.io*/
#include <stdio.h>
#include <cs50.h>

int main(void)
{
    string answer = get_string("What's your name? ");
    printf("hello, %s!\n", answer);
}