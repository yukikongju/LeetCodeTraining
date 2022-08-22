#include <stdio.h>
#include <stdbool.h>
#include <string.h>
#include <ctype.h>

bool isLeap(int year) {
    return (year % 4 == 0 && year % 100 != 0) || (year % 400 == 0);
}

bool isInputDigit(char s[]) {
    int i = 0;
    while (s[i] != '\0') 
	if (!isdigit(s[i]))
	    return false;
    return true;
}

int main() {
    // 1. get user input
    /* char s[4]; */
    /* fgets(s, 4, stdin); */
    int year = 2019;
    char s[] = "2019";

    // 2. check if year is leap
    if (!isInputDigit(s))
	printf("Input is invalid. Please input a number\n");
    else if (isLeap(year))
	printf("%d is a leap year\n", year);
    else
	printf("%d is not a leap year\n", year);

}
