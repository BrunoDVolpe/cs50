#include <cs50.h>
#include <stdio.h>
#include <math.h>

int main(void)
{
    // get positive number
    int number;
    do
    {
        float change = get_float("Change owed: ");
        number = round(change * 100);
    }
    while (number < 1);

    int coins = 0;
    do
    {
        if (number >= 25)
        {
            number-=25;
            coins++;
        }
        else if (number >= 10)
        {
            number-=10;
            coins++;
        }
        else if (number >= 5)
        {
            number-=5;
            coins++;
        }
        else
        {
            number-=1;
            coins++;
        }
    }
    while (number > 0);
    printf("%i\n", coins);
}