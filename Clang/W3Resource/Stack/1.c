#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>

#define MAX_SIZE 100

typedef struct {
  int arr[MAX_SIZE];
  int size;
} Stack;

bool isFull(Stack *stack) { return stack->size == MAX_SIZE - 1; }

bool isEmpty(Stack *stack) { return stack->size == 0; }

void initialize(Stack *stack) { stack->size = 0; }

int pop(Stack *stack) {
  if (isEmpty(stack)) {
    perror("Stack is Empty, nothing to remove!");
    return -1;
  }
  int popped = stack->arr[stack->size];
  stack->size--;
  return popped;
}

int peek(Stack *stack) {
  if (isEmpty(stack)) {
    perror("Stack is Empty, nothing to see!");
    return -1;
  }

  int peeked = stack->arr[stack->size];
  return peeked;
}

void push(Stack *stack, int val) {
  if (isFull(stack)) {
    perror("Stack is full, cannot add anything!");
  }

  stack->arr[stack->size++] = val;
}

void displayStack(Stack *stack) {
  if (isEmpty(stack)) {
    printf("Stack is empty!");
  }

  for (int i = 0; i < stack->size; i++) {
    printf("%d ", stack->arr[i]);
  }
  printf("\n");
}

int main() {
  // dummy data to push
  int nums[10] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};

  // init stack
  Stack stack;
  initialize(&stack);

  // push to stack
  for (int i = 0; i < 10; i++) {
    push(&stack, nums[i]);
  }

  // print
  displayStack(&stack);

  return 0;
}
