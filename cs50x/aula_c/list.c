/*Exemplo aula 5 - estrutura de dados*/
#include <stdio.h>
#include <stdlib.h>

/*Prototype*/
int ex_realloc(void);

/*Criando lista de inteiros com array e imprimindo seus valores*/
/*
int main(void)
{
    int list[3];
    list[0] = 1;
    list[1] = 2;
    list[2] = 3;

    for (int i = 0; i < 3; i++)
    {
        printf("%i\n", list[i]);
    }
}
*/

/*Criando lista de inteiros com pointer e imprimindo seus valores*/
int main(void)
{
    int *list = malloc(3 * sizeof(int));
    /* error checking */
    if (list == NULL)
    {
        return 1;
    }

    /* demonstrando pointer arithmetic */
    *list = 1;
    *(list + 1) = 2;
    *(list + 2) = 3;

    /* demonstrando que alocação por colchetes, mais simples e fácil de interpretar*/
    list[0] = 1;
    list[1] = 2;
    list[2] = 3;

    /* simulando a necessidade de mais um número nessa sequência, usando a cópia para outro local */
    int *tmp = malloc(4 * sizeof(int));
    /*error checking*/
    if (tmp == NULL)
    {
        free(list);
        return 1;
    }

    for (int i = 0; i < 3; i++)
    {
        tmp[i] = list[i];
    }

    /* de fato adicionando e atribuindo o 4º número */
    tmp[3] = 4;

    free(list);

    /* recaracterizando o nome das minhas variáveis */
    list = tmp;

    for (int i = 0; i < 4; i++)
    {
        printf("%i\n", list[i]);
    }

    free(list);

    printf("\n----Exemplo realloc----\n");
    ex_realloc();
}

/* Aumentando uma lista usando função realloc */
int ex_realloc(void)
{
    int *lista = malloc(3 * sizeof(int));
    /* error checking */
    if (lista == NULL)
    {
        return 1;
    }

    lista[0] = 1;
    lista[1] = 2;
    lista[2] = 3;

    /* simulando a necessidade de mais um número nessa sequência, usando a cópia para outro local através de realloc */
    int *temp = realloc(lista, 4 * sizeof(int));
    /*error checking*/
    if (temp == NULL)
    {
        free(lista);
        return 1;
    }

    /* realloc redimensionou e fez a cópia, então eu atribuo o 4º número */
    temp[3] = 4;

    /* eu implementei porque vi um erro */
    printf("list: %p\n", lista);
    printf("tmp: %p\n", temp);
    printf("&list: %p\n", &lista);
    printf("&tmp: %p\n", &temp);

    if (lista != temp)
    {
        free(lista);
        return 1;
    }

    /*free(lista);
    lista = temp; */

    for (int i = 0; i < 4; i++)
    {
        printf("%i\n", lista[i]);
    }

    /*liberar a memória*/
    free(lista);
    return 0;

    /*não liberei tmp porque ao atribuir list = tmp, quando limpar o list eu já estou liberando aquele espaço da memória*/
    /* não liberamos o nome da variável / pointer, mas sim o espaço da memória para o qual estamos apontando */
    /*Correção: Ao rodar o programa dele, estava dando errado. Quando limpávamos o lista e depois lista = temp,
    na verdade dava erro e limpava nossos dados. Percebi com alguns testes que ao usar realloc, ele estava apontando
    o mesmo endereço, então ao usar temp, ele já estava com o mesmo de lista = temp, apontavam para a mesma memória.
    Por isso não precisava mais limpar a memória, senão apagava tudo. Além disso, se esse é o comportamento, não preciso
    do temp, realloc sozinho está cuidando disso pra mim, posso então falar que lista = realloc(...), reatribuindo à lista
    a mudança na memória */
}

/*Os exemplos acima todos dependem bigO de n, programas grandes seriam demorados.*/
/* list2 mostra um exemplo com linked list, mais otimizado para adicionar espaço nas listas.*/