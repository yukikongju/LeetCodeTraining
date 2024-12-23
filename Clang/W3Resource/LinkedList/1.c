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

int main() {
  // define values to add to linked list
  int nums[MAX_NUMS] = {5, 6, 7};

  // create the linked list with values
  struct Node *current = NULL;
  struct Node *head = NULL;

  for (int i = 0; i < MAX_NUMS; i++) {
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

  // display list
  displayLinkedList(head);

  return 0;
}
