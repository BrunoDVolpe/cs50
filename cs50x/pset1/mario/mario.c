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
        for(int j = 0; j < 2* size + 2; j++)
        {
            if(j < (size - (i + 1)))
            {
                printf(" ");
            }
            else if(j < size)
            {
                printf("#");
            }
            else if (j == size || j == size + 1)
            {
                printf(" ");
            }
            else if(j < (size + 2 + i + 1))
            {
                printf("#");
            }
//            else
//          {
//                printf(" ");
//            }
        }
        printf("\n");
    }
}