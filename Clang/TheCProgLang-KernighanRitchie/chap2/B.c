#include <stdio.h>
#include <stdbool.h>
#include <ctype.h>

bool isLeap(int year) {
    return (year % 4 == 0 && year % 100 != 0) || (year % 400 == 0);
}

/* bool isInputDigit(char[] s); */

int main() {
    // 1. get user input
    /* char s[4]; */
    /* fgets(s, 4, stdin); */
    int year = 2019;

    // 2. check if year is leap
    if (isLeap(year))
	printf("%d is a leap year\n", year);
    else
	printf("%d is not a leap year\n", year);

}
