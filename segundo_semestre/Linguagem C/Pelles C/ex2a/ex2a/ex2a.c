#include <stdio.h>
int main (void)
{
	float sb;
	float p = 0.11;
	float v = 640.00;
	printf("Insira o salario bruto: \n");
	scanf("%f", & sb);
	if((sb*p)>v){
		printf("Sera descontado o teto do INSS");
	}
	else{
		printf("Nao sera descontado o teto do INSS");
	}
	return 0;
}
