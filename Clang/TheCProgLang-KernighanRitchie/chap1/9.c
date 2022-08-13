#include <stdio.h>

/* Exercice 1-9: Write a program to copy its input to its output, replacing each string of one or more blanks by a single blank */

int main() {
    int sentenceLength = 20;
    char words[sentenceLength];

    printf("Please enter a sentence\n");
    fgets(words, sentenceLength, stdin);

    char new_words[sentenceLength];
    int pointer = 0;
    char prev = '\0';	// empty char
    for(int i = 0; i < sentenceLength; ++i){
	char current = words[i];
	if (prev == ' ' && current == ' ') {
	    continue;
	}
	else {
	    new_words[pointer] = current;
	    ++pointer;
	}
	prev = current;
    }

    printf("%s \n", new_words);

    return(0);
}
