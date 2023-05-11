#include <stdio.h>

#include <stdio.h>

int main() {

    /*
    short i = 0xe7;
    short j = 0xf0;
    short n = i & j;
    printf("Output = %x\n", n);

    char filename[8];
    int count = 0;
    sprintf(filename, "%03i.jpg", count);
    printf("Name: %s\n", filename);
    */

/*Teste com pointers*/
    char *name;
    name = "Bruno";
    printf("------------- char *name -------------------\n");
    printf("name: %s\n", name); /*me mostra a string desse endereço*/
    printf("&name: %p\n", &name); /* me mostra o endereço do pointer name, que armazena o nome 'name'... mais inútil*/
    printf("pointer: name: %p\n", name); /* me mostra o endereço (pointer) que name está apontando*/
    printf("*name: %c\n", *name); /* imprime o char que está dentro do endereço que name está guardando */
    printf("*&name: %p\n", *&name); /* me mostra o endereço do que tem dentro do endereço name. Poderia ser "%p" e "name" */
    printf("&*name: %p\n", &*name); /* mesmo que o de cima, só ficou confuso.*/
    printf("%c\n", name[0]); /* me mostra o char do primeiro byte */
    printf("%p\n", &name[0]); /* me mostra um endereço do char do primeiro byte. Neste caso é o mesmo que a string armazena*/
    printf("%c\n", *name);
    printf("%c\n", name[1]);
    printf("%p\n", &name[1]);
    printf("%c\n", *(name+1));
    printf("%c\n", name[2]);
    printf("%p\n", &name[2]);
    printf("%c\n", *(name+2));

    printf("------------- char name2[6] -------------------\n");

    char name2[6] = {'B','r','u','n','o'};
    printf("String: %s\n", name2);
    printf("Endereço: %p\n", &name2);
    printf("Char (*): %c\n", *name2);
    printf("Char (&*): %p\n", &*name2);
    printf("[0]: %c\n", name2[0]);
    printf("[0]: %p\n", &name2[0]);
    printf("%c\n", name2[1]);
    printf("%p\n", &name2[1]);
    printf("%c\n", name2[2]);
    printf("%p\n", &name2[2]);
    printf("[5]: %c\n", name2[5]);
    printf("[5]: %p\n", &name2[5]);
    printf("------------- char *name3 -------------------\n");
    char* name3;
    name3 = "Bruneco";
    printf("String: %s\n", name3);

    return 0;
}