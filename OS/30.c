#include <stdio.h>
#include <stdlib.h>

//연결리스트를 구현할 구조체
typedef struct NODE{
	int data;
	struct NODE* next;
}node;


int main(void) {
	node* head = (node*)malloc(sizeof(node)); //헤드(시작)노드 생성
    head->next=NULL;
    node* node1 = (node*)malloc(sizeof(node));
	node1->next = head->next;
	node1->data = 10;
	head->next = node1;

	node* node2 = (node*)malloc(sizeof(node));
	node2->next = node1->next;
	node2->data = 20;
	node1->next = node2;

	node* curr = head->next; //순회용 노드 생성
	while(curr != NULL){
		printf("%d\n", curr->data);
		curr = curr->next;
	}

	free(head);
	free(node1);
	free(node2);
	return 0;
}