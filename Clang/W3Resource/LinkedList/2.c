#include <stdio.h>
#include <stdlib.h>

#define MAX_NUMS 3

struct Node {
  int val;
  struct Node *next;
};

void displayLinkedList(struct Node *node) {
  struct Node *current = node;

  while (current != NULL) {
    printf("%d -> ", current->val);
    current = current->next;
  }
  printf("\n");
}

struct Node *reverseLinkedList(struct Node *head) {
  struct Node *prev = NULL;
  struct Node *current = head;

  while (current != NULL) {
    struct Node *tmp = current->next;
    current->next = prev;
    prev = current;
    current = tmp;
  }

  return prev;
}

int main() {
  // dummy values for linked list
  int nums[MAX_NUMS] = {5, 6, 7};

  // add numbers to linked list
  struct Node *head = NULL;
  struct Node *current = NULL;

  for (int i = 0; i < MAX_NUMS; i++) {
    // define next node
    struct Node *nextNode = (struct Node *)malloc(sizeof(struct Node *));
    if (nextNode == NULL) {
      perror("Failed to allocate memory for next node. exiting..");
      return 1;
    }

    nextNode->val = nums[i];
    nextNode->next = NULL;

    if (head == NULL) {
      head = nextNode;
      current = nextNode;
    } else {
      current->next = nextNode;
    }
    current = nextNode;
  }

  // display linked list
  printf("Linked List: ");
  displayLinkedList(head);

  // reverse linked list
  struct Node *reversedHead = reverseLinkedList(head);

  // display linked list
  printf("After Reversing Linked List: ");
  displayLinkedList(reversedHead);

  return 0;
}
