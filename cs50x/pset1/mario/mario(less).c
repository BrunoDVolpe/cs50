#include <cs50.h>
#include <stdio.h>

int main(void)
{
    // get size between 1 and 8
    int size;
    do
    {
        size = get_int("Size: ");
    }
    while (size < 1 || size > 8);


    //print blocks
    for(int i = 0; i < size; i++)
    {
        for(int j = 0; j < size; j++)
        {
            if(j < (size - (i + 1)))
            {
                printf(" ");
            }
            else
            {
                printf("#");
            }
        }
        printf("\n");
    }
}