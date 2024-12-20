#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

/* https://www.youtube.com/watch?v=QKZXQc8EBDk&ab_channel=Ianertson */

#define N 100

typedef struct POSITION_STRUCT {
  int x, y;
} position_T;

// making dynamic list struct
typedef struct DYNAMIC_LIST_STRUCT {
  size_t item_size; // how much memory for each item
  size_t length;
  void **items;

} dynamic_list_T;

dynamic_list_T *init_dynamic_list(size_t item_size) {
  dynamic_list_T *list = calloc(1, sizeof(struct DYNAMIC_LIST_STRUCT));
  list->item_size = item_size;
  list->length = 0;
  list->items = (void *)0;
  return list;
}

void dynamic_list_append(dynamic_list_T *dynamic_list, void *item) {
  dynamic_list->length += 1;

  // allocate space in array
  dynamic_list->items =
      dynamic_list->items == (void *)0
          ? calloc(1, dynamic_list->item_size)
          : realloc(dynamic_list->items,
                    dynamic_list->length * dynamic_list->item_size);

  // add item to list
  dynamic_list->items[dynamic_list->length - 1] = item;
}

position_T *init_position(int x, int y) {
  position_T *position = calloc(1, sizeof(struct POSITION_STRUCT));
  position->x = x;
  position->y = y;
  return position;
}

bool checkHorizontalL2R(char **grid, int m, int n, const char *word,
                        position_T *pos) {
  if (pos->y + strlen(word) - 1 >= n) {
    return false;
  }

  printf("%d %d %ld\n", pos->x, pos->y, strlen(word));

  // see if XMAS is written
  /* for (int j = 0; j < strlen(word); j++) { */
  /*   if (grid[pos->x][pos->y + j] != word[j]) { */
  /*     return false; */
  /*   } */
  /* } */

  return true;
}

bool checkHorizontalR2L(char **grid, int m, int n, const char *word,
                        position_T *pos) {
  /* int m = sizeof(grid[0]); */
  /* if (pos->y < strlen(word)) { */
  /*   return false; */
  /* } */

  /* for (int j = 0; j < m; j++) { */
  /*   if (grid[pos->x][pos->y - j] != word[j]) { */
  /*     return false; */
  /*   } */
  /* } */

  return true;
}
bool checkVerticalT2B(char **grid, int m, int n, const char *word,
                      position_T *pos) {
  return true;
}
bool checkVerticalB2T(char **grid, int m, int n, const char *word,
                      position_T *pos) {
  return true;
}
bool checkDiagTL2BR(char **grid, int m, int n, const char *word,
                    position_T *pos) {
  return true;
}
bool checkDiagBR2TL(char **grid, int m, int n, const char *word,
                    position_T *pos) {
  return true;
}
bool checkDiagBL2TR(char **grid, int m, int n, const char *word,
                    position_T *pos) {
  return true;
}
bool checkDiagTR2BL(char **grid, int m, int n, const char *word,
                    position_T *pos) {
  return true;
}

int main() {
  // ---- read file ----
  FILE *fptr;
  fptr = fopen("ins/ex.in", "r");

  if (fptr == NULL) {
    perror("Error when opening the file");
    return 1;
  }

  char row[100];
  int m = 0, n;
  while (fgets(row, sizeof(row), fptr)) {
    if (m == 0) {
      n = strlen(row);
    }
    m++;
  }
  fseek(fptr, 0, SEEK_SET);

  printf("Shape: %d %d\n", m, n);

  // store word grid in matrix
  char grid[m][n];
  int i = 0;
  while (fgets(row, sizeof(row), fptr)) {
    for (int j = 0; j < n && j < strlen(row); j++) {
      grid[i][j] = row[j];
    }
    i++;
  }

  fclose(fptr);

  // WHY IS THIS NOT EQUIVALENT to snippet below?
  /* for (int i = 0; i < m; i++) { */
  /*   printf("%s", grid[i]); */
  /* } */

  /* for (int i = 0; i < m; i++) { */
  /*   for (int j = 0; j < n; j++) { */
  /*     printf("%c", grid[i][j]); */
  /*   } */
  /*   printf(""); */
  /* } */

  // ---- PART 1 ----

  // find X position
  dynamic_list_T *lst_positions =
      init_dynamic_list(sizeof(struct POSITION_STRUCT));
  for (int i = 0; i < m; i++) {
    for (int j = 0; j < n; j++) {
      if (grid[i][j] == 'X') {
        dynamic_list_append(lst_positions, init_position(i, j));
      }
    }
  }

  printf("Num of 'X': %zu\n", lst_positions->length);
  char XMAS[] = "XMAS";

  // iterate through them
  bool (*conditions[])(char **, int, int, const char *, position_T *) = {
      checkHorizontalL2R, checkHorizontalR2L, checkVerticalB2T,
      checkVerticalT2B,   checkDiagTR2BL,     checkDiagBL2TR,
      checkDiagTR2BL,     checkDiagBL2TR};
  int numConditions = 8;

  int counter = 0;
  for (int i = 0; i < lst_positions->length; i++) {
    position_T *pos = (position_T *)lst_positions->items[i];
    /* printf("%d %d\n", pos->x, pos->y); */

    for (int k = 0; k < numConditions; k++) {
      if (conditions[k](grid, m, n, XMAS, pos)) {
        counter++;
      }
    }
  }

  printf("Counter: %d\n", counter);

  return 0;
}
