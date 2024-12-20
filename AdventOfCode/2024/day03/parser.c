
// ex: MUL -> LPAREN -> NUMBER(2) -> COMMA -> NUMBER(4) -> RPAREN

#include <ctype.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_LINE 100000

typedef enum {
  TOKEN_NUMBER,
  TOKEN_MUL, // mul
  TOKEN_DO,  // do
  TOKEN_DONT,
  TOKEN_COMMA,  // ,
  TOKEN_LPAREN, // (
  TOKEN_RPAREN, // )
  TOKEN_INVALID,
  TOKEN_EOF,

} TokenType;

typedef struct {
  TokenType type;
  char value[10];
} Token;

Token get_next_token(char **ptr) {
  Token token = {0};

  while (**ptr) {
    if (**ptr == '\0') {
      token.type = TOKEN_EOF;
      return token;
    } else if (**ptr == '(') {
      token.type = TOKEN_LPAREN;
      (*ptr)++;
      return token;
    } else if (**ptr == ')') {
      token.type = TOKEN_RPAREN;
      (*ptr)++;
      return token;
    } else if (**ptr == ',') {
      token.type = TOKEN_COMMA;
      (*ptr)++;
      return token;
    } else if (strncmp(*ptr, "do()", 4) == 0) {
      (*ptr) += 4;
      token.type = TOKEN_DO;
      return token;
    } else if (strncmp(*ptr, "don't()", 7) == 0) {
      *ptr += 7;
      token.type = TOKEN_DONT;
      return token;
    } else if (strncmp(*ptr, "mul", 3) == 0) {
      *ptr += 3;
      token.type = TOKEN_MUL;
      return token;
    } else if (isdigit(**ptr)) {
      int i = 0;
      while (isdigit(**ptr) && i < 3) {
        token.value[i++] = **ptr;
        (*ptr)++;
      }
      token.value[i] = '\0';
      token.type = TOKEN_NUMBER;
      return token;
    } else {
      token.type = TOKEN_INVALID;
      (*ptr)++;
    }
  }

  token.type = TOKEN_EOF;
  return token;
}

int main() {
  // read file
  FILE *fptr;
  fptr = fopen("ins/1.in", "r");

  // count number of characters
  char row[MAX_LINE];
  char *ptr = row;
  int count = 0;
  char c;
  while ((c = getc(fptr)) != EOF) {
    row[count++] = c;
  }
  row[count] = '\0';
  fclose(fptr);

  // parse and compute total
  int total = 0;
  bool isMultEnabled = true;
  Token token = {0};
  while (token.type != TOKEN_EOF) {
    token = get_next_token(&ptr);
    if (token.type == TOKEN_INVALID) {
      continue;
    } else if (token.type == TOKEN_EOF) {
      break;
    } else if (token.type == TOKEN_DO) {
      isMultEnabled = true;
    } else if (token.type == TOKEN_DONT) {
      isMultEnabled = false;
    } else if (token.type == TOKEN_MUL) {
      // parse '('
      token = get_next_token(&ptr);
      if (token.type != TOKEN_LPAREN)
        continue;

      // parse x
      token = get_next_token(&ptr);
      if (token.type != TOKEN_NUMBER)
        continue;
      int x = atoi(token.value);

      // parse ,
      token = get_next_token(&ptr);
      if (token.type != TOKEN_COMMA)
        continue;

      // parse y
      token = get_next_token(&ptr);
      if (token.type != TOKEN_NUMBER)
        continue;
      int y = atoi(token.value);

      // parse ')'
      token = get_next_token(&ptr);
      if (token.type != TOKEN_RPAREN)
        continue;

      // add to total
      if (isMultEnabled) {
        total += x * y;
      }
    }
  }

  printf("Total: %d\n", total);

  return 0;
}
