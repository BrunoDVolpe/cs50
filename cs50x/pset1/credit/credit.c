#include <cs50.h>
#include <stdio.h>
#include <math.h>

int main(void)
{
    // get creditcard number
    long card_number;
    do
    {
        card_number = get_long("Number: ");
    }
    while (card_number < 0);

    //Validar cálculo matemático
    //4003 6000 0000 0014 (13, 15, 16)
    int sum = 0;
    int i = 0;
    int num;
    do
    {
        i++;
        if (i%2 == 0)
        {
            num = (card_number % (long) pow(10,i) / (long) pow(10,i - 1)) * 2;
            if(num > 9)
            {
                sum += num/10;
                sum += num%10;
            }
            else
            {
                sum += num;
            }
        }
        else
        {
            sum += card_number % (long) pow(10,i) / (long) pow(10,i - 1);
        }
    } while(i<16);

    if(sum % 10 == 0)
    {
        // Validar dígitos do cartão
        //American Express - 15 dígitos - começam com 34 ou 37 (340360000000001 ou 370360000000001)
        //MasterCard - 16 dígitos - começa com 51, 52, 53, 54 ou 55 (5103600000000014 ou 5303600000000014)
        //Visa - 13 ou 16 dígitos - começam com 4 (4003600000000014)
        if (card_number / (long) pow(10,13) == 34 || card_number / (long) pow(10,13) == 37)
        {
            printf("AMEX\n");
        }
        else if (card_number / (long) pow(10,14) == 51 || card_number / (long) pow(10,14) == 52 || card_number / (long) pow(10,14) == 53 || card_number / (long) pow(10,14) == 54 || card_number / (long) pow(10,14) == 55){
            printf("MASTERCARD\n");
        }
        else if (card_number / (long) pow(10,12) == 4 || card_number / (long) pow(10,15) == 4)
        {
            printf("VISA\n");
        }
        else
        {
            printf("INVALID\n");
        }
    }
    else
    {
        printf("INVALID\n");
    }
}