/* Exercice 2-1: Write a program to determine the ranges of char, short, int and  */
/*       long variables, both for signed and unsigned */
/* Why are there no unsigned float: https://stackoverflow.com/questions/512022/why-doesnt-c-have-unsigned-floats */

#include <stdio.h>
#include <limits.h>
#include <float.h>

int main(){
    // signed
    printf("Signed char min: %d\n", SCHAR_MIN);
    printf("Signed char max: %d\n", SCHAR_MAX);
    printf("Signed short min: %d\n", SHRT_MIN);
    printf("Signed short max: %d\n", SHRT_MAX);
    printf("Signed int min: %d\n", INT_MIN);
    printf("Signed int max: %d\n", INT_MAX);
    printf("Signed long min: %ld\n", LONG_MIN);
    printf("Signed long max: %ld\n", LONG_MAX);
    printf("Signed float min: %f\n", FLT_MAX);
    printf("Signed float max: %f\n", FLT_MIN);

    // unsigned
    printf("Unsigned char max: %d\n", UCHAR_MAX);
    printf("Unsigned short max: %d\n", USHRT_MAX);
    printf("Unsigned int max: %d\n", UINT_MAX);
    printf("Unsigned long max: %ld\n", ULONG_MAX);

    return(0);
}
