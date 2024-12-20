#include <ctype.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_LINE 1000000

int main() {

  // read file
  FILE *fptr;
  /* fptr = fopen("ins/ex2.in", "r"); */
  fptr = fopen("ins/1.in", "r");

  //
  char row[MAX_LINE];
  char *ptr = row;
  int count = 0;
  char c;
  for (c = getc(fptr); c != EOF; c = getc(fptr)) {
    row[count] = c;
    count++;
  }
  row[count] = '\0';

  /* printf("Num of chars: %d\n", count); */
  /* for (int i = 0; i < count; i++) { */
  /*   printf("%c", row[i]); */
  /* } */

  // process
  int total = 0;
  bool isMultEnabled = true;
  while (*ptr) {
    // skip
    while (*ptr && !isalpha(*ptr)) {
      ptr++;
    }

    //
    if (strncmp(ptr, "do()", 4) == 0) {
      ptr += 4;
      isMultEnabled = true;
    } else if (strncmp(ptr, "don't()", 7) == 0) {
      ptr += 7;
      isMultEnabled = false;
    } else if (strncmp(ptr, "mul(", 4) == 0) {
      ptr += 4;

      // parse X
      int i = 0;
      char x_buffer[4] = {0};
      while (isdigit(*ptr) && i < 3) {
        x_buffer[i++] = *ptr++;
      }

      // parse ','
      if (*ptr != ',' || i == 0)
        continue;
      ptr++;

      // parse Y
      i = 0;
      char y_buffer[4] = {0};
      while (isdigit(*ptr) && i < 3) {
        y_buffer[i++] = *ptr++;
      }

      // parse ')'
      if (*ptr != ')' || i == 0)
        continue;
      ptr++;

      // compute
      int x = atoi(x_buffer);
      int y = atoi(y_buffer);

      if (isMultEnabled) {
        total += x * y;
        /* printf("%d %d\n", x, y); */
        /* isMultEnabled = false; */
      }

    } else {
      ptr++;
    }
  }

  printf("Total: %d\n", total);

  return 0;
}
