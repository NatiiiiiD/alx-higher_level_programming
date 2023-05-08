#include "lists.h"

/**
 * check_cycle - it will checks if a linked list is containing a cycle
 * @list: The linked list to check
 *
 * Return: if the list has a cycle 1 , if it doesn't 0
 */
int check_cycle(listint_t *list)
{
	listint_t *slow = list;
	listint_t *fast = list;

	if (!list)
		return (0);

	while (slow && fast && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;
		if (slow == fast)
			return (1);
	}

	return (0);
}
