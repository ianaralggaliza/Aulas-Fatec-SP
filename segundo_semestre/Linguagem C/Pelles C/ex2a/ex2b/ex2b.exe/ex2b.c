# include <stdio.h>
int main (void)
{
	int i;
	int n;
	int soma = 0;
	printf("Insira o valor de n: \n");
	scanf("%d", & n);
	for(i=1; i<=(n+1); i++){
		if ((n%i)==0){
			soma += i;
		}
	}
	printf("Soma = %d", soma);
	return 0;
}
