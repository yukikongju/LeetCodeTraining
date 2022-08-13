#include <stdio.h>

int main() {
    int nt = 0;	    // num tabs
    int nb = 0;	    // num blanks
    int nl = 0;	    // num new lines

    // get user inputs with fgets()
    printf("Please enter a sentence \n");
    char words[20];
    fgets(words, 20, stdin);

    int arrayLength = sizeof words / sizeof words[0];

    for (int i = 0; i < arrayLength ; ++i) {
	char c = words[i];
	switch (c) {
	    case ' ':
		++nb;
		break;
	    case '\n':
		++nl;
		break;
	    case '\t':
		++nt;
		break;
	}
    }

    printf("The sentence '%s' has ", words);
    printf("%d tabs, %d blanks, %d new lines \n", nt, nb, nl);

    return(0);
}
