#include <stdio.h>
#include <stdlib.h>

int main() {
  // ---- 1. read file
  FILE *ptr;
  /* ptr = fopen("ins/ex.in", "r"); */
  ptr = fopen("ins/1.in", "r");

  // number of lines
  char row[100];
  int rowCount = 0;
  while (fgets(row, sizeof(row), ptr)) {
    rowCount++;
  }
  fseek(ptr, 0, SEEK_SET); // move pointer back to beginning

  // read two lists
  int list1[rowCount], list2[rowCount];
  int num1, num2;
  int i = 0;
  while (fgets(row, sizeof(row), ptr)) {
    if (sscanf(row, "%d %d", &num1, &num2)) {
      list1[i] = num1;
      list2[i] = num2;
      i++;
    }
  }
  fclose(ptr);

  for (int i = 0; i < rowCount; i++) {
    printf("%d %d\n", list1[i], list2[i]);
  }

  // ---- PART 2 ----

  // find max values in both list
  int max1 = -1, max2 = -1;
  for (int i = 0; i < rowCount; i++) {
    max1 = max1 >= list1[i] ? max1 : list1[i];
    max2 = max2 >= list2[i] ? max2 : list2[i];
  }
  int max = max1 >= max2 ? max1 : max2;
  printf("%s: %d\n", "Max 1st", max1);
  printf("%s: %d\n", "Max 2nd", max2);
  printf("%s: %d\n", "Overall Max", max);

  // count number occurences in second list
  int counts[max + 1];
  for (int i = 0; i < max; i++)
    counts[i] = 0;
  for (int i = 0; i < rowCount; i++) {
    counts[list2[i]] += 1;
  }

  // compute total similarity score
  int score = 0;
  for (int i = 0; i < rowCount; i++) {
    int num = list1[i];
    score += num * counts[num];
  }

  printf("%s: %d\n", "Score", score);

  return 0;
}
