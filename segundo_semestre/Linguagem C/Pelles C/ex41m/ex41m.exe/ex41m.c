#include <stdio.h>
void dig_esq_par(int n);
int main (void) 
{
	int n;
	printf("digite n:");
	scanf("%d", &n);
	dig_esq_par(n);
	return 0;
}


void dig_esq_par(int n)
{
	if((n/10)==0){
		if ((n%2)==0){
			printf("sim \n");
		}
		else{
			printf("nao \n");
		}
	}
	else{ 
		dig_esq_par(n/10);
	}
}
