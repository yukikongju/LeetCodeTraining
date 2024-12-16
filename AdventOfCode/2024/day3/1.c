#include <stdio.h>
#include <stdlib.h>
#include <string.h>

/* https://www.youtube.com/watch?v=QKZXQc8EBDk&ab_channel=Ianertson */

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
    for (int j = 0; j < n; j++) {
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

  // iterate through them
  for (int i = 0; i < lst_positions->length; i++) {
    // TODO
  }

  return 0;
}
