#include "student.c"
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_TOKENS 10

void addStudent(StudentNode *studentNode, char *name, char *age, char *sex,
                char *mark) {
  static int id_count = 0;

  // TODO: convert types
  /* printf("%s %s %s %s", name, age, sex, mark); */

  // TODO: check if student exist before adding
  bool existStudent = false;
  if (existStudent) {
    // TODO: add mark to marks list
    return;
  }

  // ----  add student if doesnt exist ----

  // initialize student
  enum Sex s_sex = *sex == 'F' ? SEX_F : SEX_M;

  // init linked list mark with
  MarkNode *marks = (MarkNode *)malloc(sizeof(MarkNode));
  marks->mark = atoi(mark);

  Student student = {
      id_count++,
      atoi(age),
      s_sex,
      marks,
  };

  StudentNode *nextStudent;
  nextStudent->next = NULL;
  nextStudent->student;

  // TODO: add to list in alphabetical order
  StudentNode *current = studentNode;
  while (studentNode->next != NULL) {
    current = current->next;
  }
  current->next = nextStudent;

  return;
}

int main() {
  // read file
  FILE *fptr = fopen("ins/students.txt", "r");
  if (fptr == NULL) {
    perror("Error when opening file, exiting..");
    return 1;
  }

  char row[100];
  StudentNode *headStudentNode = (StudentNode *)malloc(sizeof(StudentNode));
  StudentNode *studentLastNode = headStudentNode;

  fgets(row, sizeof(row), fptr); // skip header
  while (fgets(row, sizeof(row), fptr)) {
    char *tokens[MAX_TOKENS];
    int token_count = 0;

    // separate line by separator ','
    char *token = strtok(row, ",");
    while (token != NULL && token_count < MAX_TOKENS) {
      tokens[token_count++] = token;
      token = strtok(NULL, ",");
    }

    /* for (int i = 0; i < token_count; i++) { */
    /*   printf("%s ", tokens[i]); */
    /* } */
    /* printf("\n"); */

    // creating student struct
    addStudent(headStudentNode, tokens[0], tokens[1], tokens[2], tokens[3]);
  }

  fclose(fptr);

  //

  return 0;
}
