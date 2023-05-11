#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>

//Defining a byte
typedef uint8_t BYTE;

int main(int argc, char *argv[])
{
    //Ensure proper usage
    if (argc != 2)
    {
        printf("Usage: ./recover image\n");
        return 1;
    }

    //remember filename
    char *infile = argv[1];

    //Open input file
    FILE *memoryCard = fopen(infile, "r");

    //Validating input file
    if (memoryCard == NULL)
    {
        printf("Could not open %s\n", infile);
        return 1;
    }

    // Creating 512 bytes buffer, count control, if is reading any jpg file and img to write a file
    BYTE buffer[512];
    int count = 0;
    int is_reading = 0;
    char filename[8];
    FILE *img;

    while(fread(buffer, sizeof(BYTE), 512, memoryCard))
    {
        //Looking for JPEG beginning
        // 4th byte: 0xff 0xd8 0xff 0xe0 , 0xe1 , 0xe2 , 0xe3 , 0xe4 , 0xe5 , 0xe6 , 0xe7 , 0xe8 , 0xe9 , 0xea , 0xeb , 0xec , 0xed , 0xee ou 0xef .
        // Dito de outra forma, os primeiros quatro bits do quarto byte são 1110 e do 0xf0 é 1111 0000
        if (buffer[0] == 0xff && buffer[1] == 0xd8 && buffer[2] == 0xff && (buffer[3] & 0xf0) == 0xe0)
        {
            //For first jpg found
            if (is_reading == 0)
            {
                is_reading = 1;
                sprintf(filename, "%03i.jpg", count);
                img = fopen(filename, "w");

                //Checking if could create the file
                if (img == NULL)
                {
                    printf("Could not create %s\n", filename);
                    return 1;
                }

                //Write the content from buffer to img in chuncks of 512 bytes
                fwrite(buffer, sizeof(BYTE), 512, img);
            }
            else
            {
                // if found another image, close the previous, start another one
                fclose(img);
                count++;
                sprintf(filename, "%03i.jpg", count);
                img = fopen(filename, "w");
                if (img == NULL)
                {
                    printf("Could not create %s\n", filename);
                    return 1;
                }
                fwrite(buffer, sizeof(BYTE), 512, img);
            }
        }
        else
        {
            //keep writting if is reading memory and found at least one jpg, i.e. didn't match the begining of jpg.
            if (is_reading != 0)
            {
                fwrite(buffer, sizeof(BYTE), 512, img);
            }
        }
    }

    //Close files
    fclose(img);
    fclose(memoryCard);

    return 0;
}