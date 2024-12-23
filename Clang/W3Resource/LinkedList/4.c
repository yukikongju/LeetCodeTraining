#include <stdio.h>
#include <stdlib.h>

#define NUM_NODES_INIT 5

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

struct Node *insertToBeginning(struct Node *head, int val) {
  struct Node *newHead = (struct Node *)malloc(sizeof(struct Node *));
  newHead->next = head;
  newHead->val = val;
  return newHead;
}
void insertToEnd(struct Node *head, int val) {
  struct Node *current = head;
  struct Node *nextNode = (struct Node *)malloc(sizeof(struct Node *));
  nextNode->val = val;
  nextNode->next = NULL;
  while ((current->next != NULL)) {
    current = current->next;
  }
  current->next = nextNode;
}
void insertToMiddle(struct Node *head, int val) {
  struct Node *slow = head, *fast = head;
  while (fast->next != NULL) {
    fast = fast->next->next;
    slow = slow->next;
  }

  struct Node *tmp = slow->next;
  struct Node *nextNode = (struct Node *)malloc(sizeof(struct Node *));
  nextNode->next = tmp;
  nextNode->val = val;
  slow->next = nextNode;
}

int main() {
  //
  int nums[5] = {1, 2, 3, 4, 5};

  // add numbers to linked list
  struct Node *head = NULL;
  struct Node *current = NULL;
  for (int i = 0; i < NUM_NODES_INIT; i++) {
    // define new node
    struct Node *newNode = (struct Node *)malloc(sizeof(struct Node *));
    newNode->val = nums[i];
    newNode->next = NULL;

    if (head == NULL) {
      head = newNode;
      current = newNode;
    } else {
      current->next = newNode;
    }
    current = newNode;
  }

  printf("Init Linked List: ");
  displayLinkedList(head);

  // add to beginning
  printf("Add to Beginning: ");
  struct Node *newHead = insertToBeginning(head, 0);
  displayLinkedList(newHead);

  // add to end
  printf("Add to end: ");
  insertToEnd(newHead, 6);
  displayLinkedList(newHead);

  // add to middle
  printf("Add to middle: ");
  insertToMiddle(newHead, 14);
  displayLinkedList(newHead);

  return 0;
}
