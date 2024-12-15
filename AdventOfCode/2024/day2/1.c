#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define btoa(x) ((x) ? "true" : "false")

bool isSafeDecreasing(int *lst, int n) {
  for (int i = 1; i < n; i++) {
    /* if ((lst[i] >= lst[i - 1]) || (lst[i - 1] - lst[i] > 3)) */
    if ((lst[i - 1] - lst[i] < 1) || (lst[i - 1] - lst[i] > 3))
      return false;
  }

  return true;
}

bool isSafeIncreasing(int *lst, int n) {
  for (int i = 1; i < n; i++) {
    /* if ((lst[i] < lst[i - 1]) || (lst[i] - lst[i - 1] > 3) || */
    /*     (lst[i] - lst[i - 1] > 0)) */
    if ((lst[i] - lst[i - 1] < 1) || (lst[i] - lst[i - 1] > 3))
      return false;
  }
  return true;
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

  // ---- PART 1 ----
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
    bool isSD = isSafeDecreasing(numbers, count);
    bool isSI = isSafeIncreasing(numbers, count);
    bool isSafe = isSD || isSI;
    printf("%s: %s => SD: %s; SI: %s\n", row, btoa(isSafe), btoa(isSD),
           btoa(isSI));
    if (isSafe)
      total++;
  }

  printf("%s: %d\n", "Total", total);

  fclose(fptr);

  return 0;
}
