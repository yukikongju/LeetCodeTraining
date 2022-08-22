/* - [ ] Exercice E: Write lower(s) => convert string to lowercase */

#include <stdio.h>
#include <ctype.h>
#include <string.h>

char lower(char c) {
    if (c >= 'A' && c <= 'Z')
	return (c + 'a' - 'A');
    else 
	return c;
}

int main() {
    char s[] = "tseTiG oSme StuFFs";

    int i = 0;
    for (i = 0; i < strlen(s); ++i) {
	s[i] = lower(s[i]);
    }

    printf("%s\n", s);

    return 0;
}
