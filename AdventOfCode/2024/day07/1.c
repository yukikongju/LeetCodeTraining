#include <ctype.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_LINE 100000
typedef long long ll;

ll computeNumberCalibration(ll target, int *numbers, int k) {
  ll total = 0;

  int tmp[MAX_LINE] = {0};
  tmp[0] = 0;
  int tmp_size = 1;

  /* int *tmp = malloc(MAX_LINE * sizeof(int)); */
  /* int *new_tmp = malloc(MAX_LINE * sizeof(int)); */
  /* int tmp_size = 1; */

  for (int i = 0; i < k; i++) {
    int new_tmp[MAX_LINE] = {0};
    int new_tmp_size = 0;
    for (int j = 0; j < tmp_size; j++) {
      // generate possibility: addition and multiplication
      new_tmp[new_tmp_size++] = tmp[j] * numbers[i];
      new_tmp[new_tmp_size++] = tmp[j] + numbers[i];
    }
    memcpy(tmp, new_tmp, new_tmp_size * sizeof(int));
    tmp_size = new_tmp_size;
  }

  for (int i = 0; i < tmp_size; i++) {
    if (tmp[i] == target) {
      total++;
    }
  }

  /* free(tmp); */
  /* free(new_tmp); */
  return total;
}

int main() {
  // read file
  /* FILE *fptr = fopen("ins/ex.in", "r"); */
  FILE *fptr = fopen("ins/1.in", "r");
  /* FILE *fptr = fopen("ins/2.in", "r"); */
  /* FILE *fptr = fopen("ins/3.in", "r"); */

  // compute total calibration result
  ll total = 0;
  char row[MAX_LINE];
  while (fgets(row, sizeof(row), fptr)) {
    // extract target and numbers => <Target>: <num1> <num2> ...

    char *p1 = row;
    char *p2 = strstr(row, ":");
    if (p2 == NULL)
      continue;

    /* printf("%s %s\n", p1, p2); */

    // read target
    /* char target_buffer[10]; */
    /* size_t len = p2 - p1; // length of target substring */
    /* strncpy(target_buffer, p1, len); */
    /* target_buffer[len] = '\0'; */
    /* int target = atoi(target_buffer); */
    *p2 = '\0';
    ll target = strtoll(p1, NULL, 10);
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

    printf("%lld %d\n", target, k);
    for (int i = 0; i < k; i++) {
      printf("%d ", numbers[i]);
    }
    printf("\n");

    // compute number of calibrations
    int numCalibrations = computeNumberCalibration(target, numbers, k);
    if (numCalibrations > 0) {
      total += target;
    }
  }

  printf("Total: %lld\n", total);

  return 0;
}
