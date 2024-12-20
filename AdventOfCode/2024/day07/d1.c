#include <ctype.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_LINE 100
#define MAX_NUMBERS 10

int evaluate_expression(int *numbers, int k, char *operators) {
  int result = numbers[0];
  for (int i = 0; i < k - 1; i++) {
    if (operators[i] == '+') {
      result += numbers[i + 1];
    } else if (operators[i] == '*') {
      result *= numbers[i + 1];
    }
  }
  return result;
}

int computeNumberCalibration(int target, int *numbers, int k) {
  int total = 0;

  int combinations = 1 << (k - 1);
  for (int i = 0; i < combinations; i++) {
    char operators[MAX_NUMBERS] = {0};
    for (int j = 0; j < k - 1; j++) {
      operators[j] = ((i >> j) & 1) ? '*' : '+';
    }

    int result = evaluate_expression(numbers, k, operators);
    if (result == target)
      total += 1;
  }

  return total;
}

int main() {
  // read file
  /* FILE *fptr = fopen("ins/ex.in", "r"); */
  FILE *fptr = fopen("ins/1.in", "r");
  /* FILE *fptr = fopen("ins/2.in", "r"); */

  // compute total calibration result
  int total = 0;
  char row[MAX_LINE];
  while (fgets(row, sizeof(row), fptr)) {
    // extract target and numbers => <Target>: <num1> <num2> ...

    char *p1 = row;
    char *p2 = strstr(row, ":");

    /* printf("%s %s\n", p1, p2); */

    // read target
    char target_buffer[10];
    size_t len = p2 - p1; // length of target substring
    strncpy(target_buffer, p1, len);
    target_buffer[len] = '\0';
    int target = atoi(target_buffer);
    /* printf("%d\n", target); */

    // read numbers
    p2++;
    int numbers[100];
    int k = 0;
    while (*p2 != '\0') {
      char digits[100];
      int i = 0;
      while (isdigit(*p2)) {
        digits[i++] = *p2++;
      }
      digits[i] = '\0';
      if (i > 0) {
        numbers[k++] = atoi(digits);
      }
      p2++;
    }

    /* printf("%d %d\n", target, k); */
    /* for (int i = 0; i < k; i++) { */
    /*   printf("%d ", numbers[i]); */
    /* } */
    /* printf("\n"); */

    // compute number of calibrations
    int numCalibrations = computeNumberCalibration(target, numbers, k);
    if (numCalibrations > 0) {
      total += target;
    }
  }

  printf("Total: %d\n", total);

  return 0;
}
