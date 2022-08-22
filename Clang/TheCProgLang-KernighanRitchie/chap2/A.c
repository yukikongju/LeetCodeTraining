/* - [ ] Exercice a: Return length of a string */

#include <stdio.h>

int main(){
    char s[] = "Testing some stuffs";
    int i = 0;
    while (s[i] != '\0') {
	++i;
    }

    printf("The length of the string is %d\n", i);

    return i;
}
