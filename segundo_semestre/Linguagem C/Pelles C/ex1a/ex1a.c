#include <stdio.h>
 int main (void)
 {
	float area;
	float b;
	float a;
	printf("Insira o tamanho da base: \n");
	scanf("%f", &b);
	printf("Insira o tamanho da altura: \n");
	scanf("%f", &a);
	area = (b*a)/2;
	printf("Area = %.2f", area);
	return 0;
 }
