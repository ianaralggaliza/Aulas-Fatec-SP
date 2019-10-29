#include<stdio.h>

void imp(int n);

int main(void)
{
	imp(15);
	return 0;
}


void imp(int n)
{
	if (n>0){
		imp(n/3);
		printf("%d ", 2*n);
		imp(n/3);
	}
}
