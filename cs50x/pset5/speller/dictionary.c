//Alterei Makefile colocando -gdwarf-4 depois de clang. Assim o valgrind funcionou.
// Implements a dictionary's functionality

#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <strings.h>

#include "dictionary.h"

// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
}
node;

// Number of buckets in hash table
#define N 676
//original: const unsigned int N = 1;

//Contador de palavras
int word_count = 0;

// Hash table
//forcei o número de N ao invés da variável N em si, porque com N está dando erro
node *table[N];

// Returns true if word is in dictionary, else false
bool check(const char *word)
{
    // TODO
    for (node *tmp = table[hash(word)]; tmp != NULL; tmp = tmp->next)
    {
        if (strcasecmp(word, tmp->word) == 0)
        {
            return true;
        }
    }
    return false;
}

// Hashes word to a number
unsigned int hash(const char *word)
{
    // TODO
    if (word[0] >= 97 && word[0] <= 122)
    {
        if (word[1] >= 97 && word[1] <= 122)
        {
            return ((int) word[0] - 97) * 25 + (int) word[1] - 97;
        }
        else if (word[1] >= 65 && word[1] <= 90)
        {
            return ((int) word[0] - 97) * 25 + (int) word[1] - 65;
        }
        else
        {
            return (int) word[0] - 97;
        }
    }
    else if(word[0] >= 65 && word[0] <= 90)
    {
        if (word[1] >= 97 && word[1] <= 122)
        {
            return ((int) word[0] - 65) * 25 + (int) word[1] - 97;
        }
        else if (word[1] >= 65 && word[1] <= 90)
        {
            return ((int) word[0] - 65) * 25 + (int) word[1] - 65;
        }
        else
        {
            return (int) word[0] - 65;
        }
    }
    //Se não for maiúscula ou minúscula, retorna o módulo
    else
    {
        return (int) word[0] % N;
    }
}

// Loads dictionary into memory, returning true if successful, else false
bool load(const char *dictionary)
{
    // TODO
    //Open dictionary file
    FILE *dict = fopen(dictionary,"r");
    if (dict == NULL)
    {
        return false;
    }
    //Read strings from file
    char word_buffer[LENGTH + 1];
    node *n = NULL;
    node *tmp = NULL;
    int index;

    while(fscanf(dict, "%s", word_buffer))
    {
        //Read string from file
        if (feof(dict)!= 0)
        {
            break;
        }

        //Create the node
        n = malloc(sizeof(node));
        if (n == NULL)
        {
            fclose(dict);
            return false;
        }
        strcpy(n->word, word_buffer);
        n->next = NULL;

        index = hash(n->word);
        tmp = table[index];
        table[index] = n;
        table[index]->next = tmp;

        /*
        anterior
        n->next = table[index];
        table[index] = n;
        */

        word_count++;
    }
    fclose(dict);
    return true;
}

// Returns number of words in dictionary if loaded, else 0 if not yet loaded
unsigned int size(void)
{
    // TODO
    if (word_count > 0)
    {
        return word_count;
    }

    return 0;
}

// Unloads dictionary from memory, returning true if successful, else false
bool unload(void)
{
    // TODO
    int contador = 0;
    for (int i = 0; i < N; i++)
    {
        while (table[i] != NULL)
        {
            node *tmp = table[i]->next;
            free(table[i]);
            table[i] = tmp;
            contador++;
        }
    }
    //printf("Contador apagou %i palavras.\n", contador);
    if (contador == word_count)
    {
        return true;
    }
    return false;
}
