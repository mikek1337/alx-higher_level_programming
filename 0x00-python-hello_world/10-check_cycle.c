#include "lists.h"


void hash(listint_t **address)
{
	printf("%p",&address);
	/**return (address);*/
}

int hash_table_insert(listint_t *node)
{
	hash(&node);

	return 1;
}


/**
 * check_cycle - checks if a linked list is cyclic or not
 * @list: head of the list listint_t pointer
 * Return: 0 if no cycle, 1 cycle
 */
int check_cycle(listint_t *list)
{
	hash_table_insert(list);
	return (1);
}
