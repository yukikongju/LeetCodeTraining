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

int countNumberOfNodesInLinkedList(struct Node *node) {
  struct Node *current = node;
  int count = 0;
  while (current != NULL) {
    count++;
    current = current->next;
  }
  return count;
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
  int numNodes = countNumberOfNodesInLinkedList(head);
  printf("Total Nodes: %d\n", numNodes);

  return 0;
}
