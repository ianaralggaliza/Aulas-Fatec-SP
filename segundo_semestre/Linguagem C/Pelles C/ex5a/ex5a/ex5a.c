#include<stdio.h>

int menor_ind(int a[], int tam);

int main(void)
{
	int tam = 2;
	int a[2] = {3,1};
	int resposta;
	resposta = menor_ind(a, tam);
	printf("Menor indice: %d \n", resposta);
	return 0;
}


int menor_ind(int a[], int tam)
{
	int ind_mn = 0;
	int i=0;
	int menor_elemento = a[0];
	for(i=0; i<tam; i++){
		if (a[i] < menor_elemento){
			menor_elemento = a[i];
			ind_mn = i;
		}
	}
	return ind_mn;
}
