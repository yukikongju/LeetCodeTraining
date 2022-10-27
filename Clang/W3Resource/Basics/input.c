#include <stdio.h>

int addUserInput(){
    int x, y;
    printf("First integer\n");
    scanf("%d", &x);
    printf("Second integer\n");
    scanf("%d", &y);
    int product = x*y;
    printf("Product: %d\n", product);

    return product;

}

int sumOfOddsUserInput(){

    // read user inputs
    int numbers[5];
    printf("input integers\n");
    for (int i = 0; i < 5; ++i) {
        /* scanf("%d\n", &numbers[i]); */
        scanf("%d", &numbers[i]);
    }

    // sum of odds
    int sum = 0;
    for (int i = 0; i < 5; ++i) {
	if (numbers[i] % 2 != 0) 
	    sum += numbers[i];
    }

    // print results
    for (int i = 0; i < 5; ++i) {
        printf("Number %d: %d\n", (i+1), numbers[i]);
    }
    printf("Sum of Odds: %d\n", sum);
    return sum;

}

int main(){
    /* int product = addUserInput(); */
    int sum = sumOfOddsUserInput();
    return 0;
}
