#include <stdio.h>
int main (void)
{
	int q;
	int v;
	int b;
	int t;
	printf("Insira a quantidade comprada: \n");
	scanf("%d", & q);
	v = q/100;
	b = v*5;
	t = q+b;
	printf("Total recebido: %d sabonetes", t);
	return 0;
}
