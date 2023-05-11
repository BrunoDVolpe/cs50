#include "helpers.h"
#include <math.h>
#include <stdio.h>

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
        for (int j = 0; j <= width; j++)
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

// Sepia (usando reflect porque não era parte do exercício)
void reflect2(int height, int width, RGBTRIPLE image[height][width])
{
    RGBTRIPLE sepia;
    int red;
    int green;
    int blue;

    // for each line
    for (int i = 0; i < height; i++)
    {
        // in each pixel
        for (int j = 0; j < width; j++)
        {
            // sepia Blue
            blue = round(.272 * image[i][j].rgbtRed + .534 * image[i][j].rgbtGreen + .131 * image[i][j].rgbtBlue);

            if (blue > 255)
            {
                sepia.rgbtBlue = 255;
            }
            else
            {
                sepia.rgbtBlue = blue;
            }

            // sepia Green
            green = round(0.349 * image[i][j].rgbtRed + 0.686 * image[i][j].rgbtGreen + 0.168 * image[i][j].rgbtBlue);

            if (green > 255)
            {
                sepia.rgbtGreen = 255;
            }
            else
            {
                sepia.rgbtGreen = green;
            }

            // sepia Red
            red = round(.393 * image[i][j].rgbtRed + .769 * image[i][j].rgbtGreen + .189 * image[i][j].rgbtBlue);

            if (red > 255)
            {
                sepia.rgbtRed = 255;
            }
            else
            {
                sepia.rgbtRed = red;
            }

            // set the sepia color
            image[i][j].rgbtBlue = sepia.rgbtBlue;
            image[i][j].rgbtGreen = sepia.rgbtGreen;
            image[i][j].rgbtRed = sepia.rgbtRed;
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

// Detect edges
void edges(int height, int width, RGBTRIPLE image[height][width])
{
    //Creating a copy of the image with a black border of 1px
    RGBTRIPLE img_cp[height + 2][width + 2], Gx, Gy;

    for (int i = 0; i < height + 2; i++)
    {
        for (int j = 0; j < width + 2; j++)
        {
            if (i == 0 || j == 0 || i == height + 1 || j == height + 1)
            {
                img_cp[i][j].rgbtRed = 0;
                img_cp[i][j].rgbtGreen = 0;
                img_cp[i][j].rgbtBlue = 0;
            }
            else
            {
                img_cp[i][j] = image[i - 1][j - 1];
            }
        }
    }

    // Calculating Gx and Gy for each color using the copied image;
    int xRed, yRed, red, xBlue, yBlue, blue, xGreen, yGreen, green;

    for (int i = 1; i < height + 2; i++)
    {
        for (int j = 1; j < width + 2; j++)
        {
            xRed = -img_cp[i - 1][j - 1].rgbtRed + img_cp[i - 1][j + 1].rgbtRed
                   - 2 * img_cp[i][j - 1].rgbtRed + 2 * img_cp[i][j + 1].rgbtRed
                   - img_cp[i + 1][j - 1].rgbtRed + img_cp[i + 1][j + 1].rgbtRed;

            xGreen = -img_cp[i - 1][j - 1].rgbtGreen + img_cp[i - 1][j + 1].rgbtGreen
                     - 2 * img_cp[i][j - 1].rgbtGreen + 2 * img_cp[i][j + 1].rgbtGreen
                     - img_cp[i + 1][j - 1].rgbtGreen + img_cp[i + 1][j + 1].rgbtGreen;

            xBlue = -img_cp[i - 1][j - 1].rgbtBlue + img_cp[i - 1][j + 1].rgbtBlue
                    - 2 * img_cp[i][j - 1].rgbtBlue + 2 * img_cp[i][j + 1].rgbtBlue
                    - img_cp[i + 1][j - 1].rgbtBlue + img_cp[i + 1][j + 1].rgbtBlue;

            yRed = -img_cp[i - 1][j - 1].rgbtRed - 2 * img_cp[i - 1][j].rgbtRed - img_cp[i - 1][j + 1].rgbtRed
                   + img_cp[i + 1][j - 1].rgbtRed + 2 * img_cp[i + 1][j].rgbtRed + img_cp[i + 1][j + 1].rgbtRed;

            yGreen = -img_cp[i - 1][j - 1].rgbtGreen - 2 * img_cp[i - 1][j].rgbtGreen - img_cp[i - 1][j + 1].rgbtGreen
                     + img_cp[i + 1][j - 1].rgbtGreen + 2 * img_cp[i + 1][j].rgbtGreen + img_cp[i + 1][j + 1].rgbtGreen;

            yBlue = -img_cp[i - 1][j - 1].rgbtBlue - 2 * img_cp[i - 1][j].rgbtBlue - img_cp[i - 1][j + 1].rgbtBlue
                    + img_cp[i + 1][j - 1].rgbtBlue + 2 * img_cp[i + 1][j].rgbtBlue + img_cp[i + 1][j + 1].rgbtBlue;

            //Calculating the modulus of each color;
            red = (int) round(sqrt(pow(xRed, 2) + pow(yRed, 2)));

            green = (int) round(sqrt(pow(xGreen, 2) + pow(yGreen, 2)));

            blue = (int) round(sqrt(pow(xBlue, 2) + pow(yBlue, 2)));

            //Validating if each color has the max of 255, if not, force to 255; and convert in the image
            if (red > 255)
            {
                image[i - 1][j - 1].rgbtRed = 255;
            }
            else
            {
                image[i - 1][j - 1].rgbtRed = red;
            }

            if (green > 255)
            {
                image[i - 1][j - 1].rgbtGreen = 255;
            }
            else
            {
                image[i - 1][j - 1].rgbtGreen = green;
            }

            if (blue > 255)
            {
                image[i - 1][j - 1].rgbtBlue = 255;
            }
            else
            {
                image[i - 1][j - 1].rgbtBlue = blue;
            }
        }
    }

    return;
}