/* Exercice 2-2: Write a loop equivalent to the for loop above without && and || */
/* Original loop:  */
/* for (i=O ; i < lim - 1 && (c = getchar()) != '\n'; ++i) */

#include <stdio.h>
#include <stdbool.h>

int main(){
    bool is_valid = true;
    int limit = 10;
    int i = 0;
    while (is_valid) {
	if (i > limit) { is_valid = false; }
	++i;
	printf("Please insert a character. Press 'q' to quit.\n");
	char c = getchar();
	if (c == 'q') { is_valid = false; }
    }

    return(0);
}
