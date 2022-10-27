#include <stdio.h>

double calculatePerimeter(double height, double width){
    return 2 * height + 2 * width;
}

double calculateArea(double height, double width){
    return height * width;
}

void printRectangle(){
    int height = 5;
    int width = 15;

    double perimeter = calculatePerimeter(height, width);
    float area = calculateArea(height, width);

    printf("The perimeter of the rectangle is %f \n", perimeter);
    printf("The area of the rectangle is %f \n", area);
}

void printDaysToYears(int numDays){
    /* 8. Write a C program to convert specified days into years, weeks and days. Go to the editor. Note: Ignore leap year.  */

    int years = numDays / 365;
    int weeks = (numDays % 365) / 7;
    int days = (numDays % 365) % 7;

    printf("Num Days: %d; Years: %d; Weeks: %d; Days: %d \n", numDays, years, weeks, days);
}


int main(){
    /* printRectangle(); */
    /* printDaysToYears(1329); */
    /* sumOfFiveOdds(); */
    return 0;
}
