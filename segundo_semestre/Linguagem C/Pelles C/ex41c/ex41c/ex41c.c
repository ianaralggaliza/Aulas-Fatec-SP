#include <stdio.h>
float pot (float b, int n);
int main (void)
{
	float b;
	int n;
	printf("digite b:");
	scanf("%f", &b);
	printf("digite n:");
	scanf("%d", &n);
	printf("resultado: %f ", pot(b,n));
	return 0;
}


float pot (float b, int n)
{
	if (n==0) return 1;
	return b * pot(b, n-1);
}
