#include <stdio.h>

main()
{
    int fahr, celsius; 
    int lower, upper, step;

    lower = 0;
    upper = 300;
    step = 20;

    fahr = lower;
    while (fahr <= upper)
    {
	celsius = fahreinheit_to_celsius(fahr);
	printf("%3d\t%6d\n", fahr, celsius);
	fahr = fahr + step;
    }

}

int fahreinheit_to_celsius(int fahr)
{
    return  (5.0/9.0) * (fahr - 32.0) ;
}
