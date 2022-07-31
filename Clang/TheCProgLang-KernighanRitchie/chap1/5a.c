#include <stdio.h>

main() 
{

    for(int fahr=0; fahr<=300; fahr += 20){
	float celsius = (5.0/9.0) * (fahr - 32.0);
	printf("%3.0d\t%6.1f\n", fahr, celsius);
    }


}
