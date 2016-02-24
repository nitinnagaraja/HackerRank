#include <stdio.h>

typedef struct node {
	int data;
	struct node* next;
}node;

void add(node **p, int n) {
	node *temp, *r;
	temp = p;
	
	if (*p == NULL) {
		temp = malloc(sizeof(struct node));
		temp->data = n;
		temp->next = NULL;
		*p = temp;
	}
	else {
		temp = *p;
		while(temp->next != NULL) {
			temp = temp->next;
		}
		r = malloc(sizeof(struct node));
		r->data = n;
		temp->next = r;
		r->next = NULL;
	}
}

void print(node* head) {
	while(head != NULL) {
		printf("%d ", head->data);
		head = head->next;
	}
	printf("\n");
}

void delete(node **head, int n) {
	node *temp;
	while((*head) != NULL) {
		if ((*head)->data == n) {
			temp = (*head);
			*head = *head->next;
			free(temp);
			continue;
		}
		
		head = &((*head)->next);
	}
}

void main() {
	node *head;
	head = NULL;
	
	add(&head, 3);
	add(&head, 2);
	add(&head, 4);
	add(&head, 5);
	add(&head, 3);
	add(&head, 4);
	add(&head, 1);
	add(&head, 4);
	add(&head, 2);
	add(&head, 5);
	add(&head, 4);
	add(&head, 3);
	add(&head, 5);
	add(&head, 2);
	add(&head, 3);
	add(&head, 1);	
	add(&head, 2);
	add(&head, 4);
	add(&head, 6);
	
	print(head);
	
	delete(&head, 2);
	
	print(head);
}