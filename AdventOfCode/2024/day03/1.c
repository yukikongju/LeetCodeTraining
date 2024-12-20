#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_LINE 10000000

int main() {
  // read file
  FILE *fptr;
  /* fptr = fopen("ins/ex.in", "r"); */
  fptr = fopen("ins/1.in", "r");

  // file length
  char row[MAX_LINE];
  char *ptr = row;
  int count = 0;
  for (char c = getc(fptr); c != EOF; c = getc(fptr)) {
    row[count] = c;
    count++;
  }

  /* printf("Num of chars: %d\n", count); */
  /* for (int i = 0; i < count; i++) { */
  /*   printf("%c", row[i]); */
  /* } */

  fseek(fptr, 0, SEEK_SET); // move pointer to start

  int total = 0;
  while ((ptr = strstr(ptr, "mul(")) != NULL) {
    ptr += 4; // skip "mul("

    // parse X
    char x_buffer[4] = {0};
    int i = 0;
    while (isdigit(*ptr) && i < 3) {
      x_buffer[i++] = *ptr++;
    }

    // parse ','
    if (*ptr != ',' || i == 0)
      continue;
    ptr++; // skip ','

    // parse Y
    char y_buffer[4] = {0};
    i = 0;
    while (isdigit(*ptr) && i < 3) {
      y_buffer[i++] = *ptr++;
    }

    // parse ')'
    if (*ptr != ')' || i == 0)
      continue;
    ptr++;

    // convert x, y to number
    int x = atoi(x_buffer);
    int y = atoi(y_buffer);
    total += x * y;
  }

  printf("Total: %d\n", total);

  return 0;
}
