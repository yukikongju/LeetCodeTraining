#include <stdio.h>
#include <string.h>

/* Exercice 1-19: Write a function `reverse()` that reverses the character string.  Use it to write a program that reverses its input a line at a time. */

int main()
{
    // get user input    
    char words[20];
    printf("Please enter a word\n");
    fgets(words, 20, stdin);

    // reverse string using two pointers
    int left = 0;					// first index  
    /* int right = sizeof words / sizeof words[0] - 1;	// last index */
    int right = strlen(words) - 1;	// last index

    while(left<right){
	char tmp = words[left];
	words[left] = words[right];
	words[right] = tmp;

	++left;
	--right;
    }

    printf("%s \n", words);
	
    return 0;
}
