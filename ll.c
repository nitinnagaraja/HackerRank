#include<stdio.h>

struct node
{
int a;
struct node *link;
};

void add(struct node **p,int n)
{
struct node *temp,*r;
temp=*p;
if(*p==NULL)
{
temp=malloc(sizeof(struct node));
temp->a=n;
temp->link=NULL;
*p=temp;

}
else
{ temp=*p;
while(temp->link!=NULL)
{
temp=temp->link;
}
r=malloc(sizeof(struct node));
r->a=n;
temp->link=r;
r->link=NULL;

}
}

void display(struct node *a)
{
while(a!=NULL)
{
printf("%d",a->a);
a=a->link;
}
}

void delete(struct node **a,int n)
{
struct node *temp,*temp1;
temp=*a;
temp1=temp->link;
if(temp->a==n)
{
temp->link=NULL;
*a=temp1;
}
else
{
while(temp->link!=NULL)
{
if((temp->link->a)==n)
{
temp->link=temp->link->link;

}
temp=temp->link;
temp1=temp1->link;

}

}

}


void RemoveNodesWithValue(struct node** head, int k) {
struct node* toDelete;
while((*head) != NULL) {
if ((*head)->a == k) {
toDelete = (*head);
*head = (*head)-> link;
//delete toDelete;
continue;
}
head = &((*head)->link);

}}

void main()
{
struct node *p;
p=NULL;

add(&p,5);
add(&p,7);
add(&p,7);
add(&p,6);
add(&p,7);
add(&p,7);
add(&p,7);
add(&p,7);
add(&p,7);
add(&p,7);
add(&p,7);
add(&p,8);
add(&p,7);
add(&p,7);
display(p);
//delete(&p,7);
RemoveNodesWithValue(&p, 7);
printf("\n");
printf("\n");
display(p);
printf("\n");
printf("\n");
}
