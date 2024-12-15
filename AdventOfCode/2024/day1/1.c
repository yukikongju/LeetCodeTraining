#include <stdio.h>
#include <stdlib.h>

int compare(const void *a, const void *b) { return (*(int *)a - *(int *)b); }

int main() {
  FILE *fptr;
  fptr = fopen("ins/1.in", "r");

  // check if file exists
  if (fptr == NULL) {
    perror("Error opening file");
    return 1;
  }

  // move file pointer to the end of file to get file length
  /* fseek(fptr, 0, SEEK_END); */ // move pointer to the end
  /* long length = ftell(fptr); */
  /* fseek(fptr, 0, SEEK_SET); */ // move pointer to beginning
  char row[100];
  int rowCount = 0;
  while (fgets(row, sizeof(row), fptr)) {
    rowCount++;
  }
  /* printf("%s: %d\n", "Num of rows: ", rowCount); */

  fseek(fptr, 0, SEEK_SET);

  // read file
  int list1[rowCount], list2[rowCount];
  int num1, num2;
  int i = 0;

  while (fgets(row, sizeof(row), fptr)) {
    /* printf("%s", row); */
    if (sscanf(row, "%d %d", &num1, &num2) == 2) {
      list1[i] = num1;
      list2[i] = num2;
    }
    i++;
  }
  fclose(fptr);

  /* for (int i = 0; i < rowCount; i++) { */
  /*   printf("%d %d\n", list1[i], list2[i]); */
  /* } */

  // ---- PART 1 ----

  // sort lists
  qsort(list1, rowCount, sizeof(int), compare);
  qsort(list2, rowCount, sizeof(int), compare);

  // compute total distance
  int total = 0;
  for (int i = 0; i < rowCount; i++) {
    total += abs(list1[i] - list2[i]);
  }

  printf("%s: %d\n", "Total: ", total);

  return 0;
}
