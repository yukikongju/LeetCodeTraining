#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_REMOVED 1
#define btoa(x) ((x) ? "true" : "false")

bool isSafeDecreasing(int *lst, int n) {
  for (int i = 1; i < n; i++) {
    if ((lst[i - 1] - lst[i] < 1) || (lst[i - 1] - lst[i] > 3))
      return false;
  }

  return true;
}

bool isSafeIncreasing(int *lst, int n) {
  for (int i = 1; i < n; i++) {
    if ((lst[i] - lst[i - 1] < 1) || (lst[i] - lst[i - 1] > 3))
      return false;
  }
  return true;
}

bool isSafeWithDampener(int *A, int n) {
  // try removing number and see if it's safe
  for (int i = 0; i < n; i++) {
    // building array without ith position
    int tmp[n - 1];
    int k = 0;
    for (int j = 0; j < n; j++) {
      if (i != j) {
        tmp[k++] = A[j];
      }
    }

    // testing if this subarray is safe
    bool isSD = isSafeDecreasing(tmp, n - 1);
    bool isSI = isSafeIncreasing(tmp, n - 1);
    if (isSD || isSI)
      return true;
  }
  return false;
}

int main() {
  // ---- read file ----
  FILE *fptr;
  /* fptr = fopen("ins/ex.in", "r"); */
  fptr = fopen("ins/1.in", "r");

  if (fptr == NULL) {
    perror("Error when opening file");
    return 1;
  }

  // number of lines in file
  char row[100];
  int rowCount = 0;
  while (fgets(row, sizeof(row), fptr)) {
    rowCount++;
  }
  fseek(fptr, 0, SEEK_SET);

  // ---- PART 2 ----
  int total = 0;
  while (fgets(row, sizeof(row), fptr)) {
    // store integers in row in array
    int numbers[10];
    int count = 0;
    char *token = strtok(row, " ");
    while (token != NULL) {
      numbers[count] = atoi(token); // convert token to integer
      count++;
      token = strtok(NULL, " "); // get next token
    }

    // determine if report is safe or unsafe
    /* printf("%s: %s => SD: %s; SI: %s\n", row, btoa(isSafe), btoa(isSD), */
    /*        btoa(isSI)); */
    if (isSafeWithDampener(numbers, count)) {
      total++;
    }
  }

  printf("%s: %d\n", "Total", total);

  fclose(fptr);

  return 0;
}
