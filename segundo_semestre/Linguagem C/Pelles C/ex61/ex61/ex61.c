#include <stdio.h>

//float soma_termos(int n);

//#define MAX(x, y) (x>y ? x : y)

//#define TO_LOWER(ch) (65<=ch && ch<=90 ? ch+32 : ch)

void decimal_hexa(int n);

void decimal_hexa(int n)
{
	if (n/16 == 0){
		n=n%16;
		printf("%X", n);
	}
	else{
		decimal_hexa(n/16);
		printf("%X", (n%16));
	}
}

int main (void)
{
	int n;
	printf("Insira um numero");
	scanf("%d", &n);
	decimal_hexa(n);
	return 0;
}


/*
int main (void)
{
	char ch;
	char resultado;
	printf("Insira um char");
	scanf("%c", &ch);
	resultado = TO_LOWER(ch);
	printf("Resultado: %c", resultado);
	return 0;
}


int main (void)
{
	float x;
	float y;
	float resultado;
	printf("Insira um numero x");
	scanf("%f", &x);
	printf("Insira um numero y");
	scanf("%f", &y);
	resultado = MAX(x,y);
	printf("Resultado: %f", resultado);
	return 0;
}


int main (void)
{
	int n;
	float resultado;
	printf("Insira um numero");
	scanf("%d", &n);
	resultado = soma_termos(n);
	printf("Resultado: %f", resultado);
	return 0;
}

float soma_termos(int n)
{
	if (n==1){
		return 1.0;
	}
	return ((1.0/n) + soma_termos(n-1));
}
*/
