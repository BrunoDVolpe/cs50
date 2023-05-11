#include "helpers.h"
#include <math.h>

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    RGBTRIPLE img_cp[height][width];
    int average;

    // creating an image copy
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j <= width; j++)
        {
            img_cp[i][j] = image[i][j];
        }
    }

    // Getting average for each pixel
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            average = (int) round((img_cp[i][j].rgbtBlue + img_cp[i][j].rgbtGreen + img_cp[i][j].rgbtRed) / 3.0);

            // set the gray shade color
            image[i][j].rgbtBlue = average;
            image[i][j].rgbtGreen = average;
            image[i][j].rgbtRed = average;
        }
    }
    return;
}

// Convert image to sepia
void sepia(int height, int width, RGBTRIPLE image[height][width])
{
    // Cópia da imagem
    RGBTRIPLE img_cp[height][width];

    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            img_cp[i][j] = image[i][j];
        }
    }

    //Iterating over the copied image and changing the other
    int red, green, blue;

    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            // sepia Blue to the image
            blue = (int) round(.272 * img_cp[i][j].rgbtRed + .534 * img_cp[i][j].rgbtGreen + .131 * img_cp[i][j].rgbtBlue);

            if (blue > 255)
            {
                image[i][j].rgbtBlue = 255;
            }
            else
            {
                image[i][j].rgbtBlue = blue;
            }

            // sepia Green to the image
            green = (int) round(0.349 * img_cp[i][j].rgbtRed + 0.686 * img_cp[i][j].rgbtGreen + 0.168 * img_cp[i][j].rgbtBlue);

            if (green > 255)
            {
                image[i][j].rgbtGreen = 255;
            }
            else
            {
                image[i][j].rgbtGreen = green;
            }

            // sepia Red to the image
            red = (int) round(.393 * img_cp[i][j].rgbtRed + .769 * img_cp[i][j].rgbtGreen + .189 * img_cp[i][j].rgbtBlue);

            if (red > 255)
            {
                image[i][j].rgbtRed = 255;
            }
            else
            {
                image[i][j].rgbtRed = red;
            }
        }
    }
    return;
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    RGBTRIPLE temp;

    // for each line
    for (int i = 0; i < height; i++)
    {
        for (int j = 0, k = width - 1; j < k; j++, k--)
        {
            // getting a copy of the pixel
            temp.rgbtBlue = image[i][j].rgbtBlue;
            temp.rgbtGreen = image[i][j].rgbtGreen;
            temp.rgbtRed = image[i][j].rgbtRed;

            // swapping colors
            image[i][j].rgbtBlue = image[i][k].rgbtBlue;
            image[i][j].rgbtGreen = image[i][k].rgbtGreen;
            image[i][j].rgbtRed = image[i][k].rgbtRed;

            image[i][k].rgbtBlue = temp.rgbtBlue;
            image[i][k].rgbtGreen = temp.rgbtGreen;
            image[i][k].rgbtRed = temp.rgbtRed;
        }
    }
    return;
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    //Copiar a imagem para trabalhar numa imagem sem alteração de pixel
    RGBTRIPLE img_cp[height][width];

    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            img_cp[i][j] = image[i][j];
        }
    }

    float count;
    int temp[3];
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            //Pegando a média dos pixels
            count = 0.0;
            temp[0] = 0;
            temp[1] = 0;
            temp[2] = 0;
            for (int x = i - 1; x <= i + 1; x++)
            {
                for (int y = j - 1; y <= j + 1; y++)
                {
                    if (x < 0 || x >= height || y < 0 || y >= width)
                    {
                        continue;
                    }
                    else
                    {
                        temp[0] += img_cp[x][y].rgbtRed;
                        temp[1] += img_cp[x][y].rgbtGreen;
                        temp[2] += img_cp[x][y].rgbtBlue;
                        count++;
                    }
                }
            }

            //Alteração na imagem final
            image[i][j].rgbtRed = (int) round(temp[0] / count);
            image[i][j].rgbtGreen = (int) round(temp[1] / count);
            image[i][j].rgbtBlue = (int) round(temp[2] / count);
        }
    }
    return;
}
