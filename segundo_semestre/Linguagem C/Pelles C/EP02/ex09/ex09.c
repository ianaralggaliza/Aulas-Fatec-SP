#include <stdio.h>
#include <stdlib.h>

struct DATA{
	int dia;
	int mes;
	int ano;
};

struct FUNCIONARIO{
	char nome[25];
	float salario;
	struct DATA ad;
	struct DATA desl;
};



int main(void)
{
	int size;
	int sizenome;
	int sizesalario;
	int sizedata;

	struct FUNCIONARIO f={
		"Maria",
		7000.00,
		{1,7,2005},
		{2,3,2018}
	};
	
	printf("Nome: %s\n", f.nome);
	printf("Salario: %.2f\n", f.salario);
	printf("Data de admissao: %d, %d, %d\n", f.ad.dia, f.ad.mes, f.ad.ano);
	printf("Data de desligamento: %d, %d, %d\n", f.desl.dia, f.desl.mes, f.desl.ano);

	sizenome = sizeof(f.nome);
	printf("Tamanho nome: %d\n", sizenome);

	sizesalario = sizeof(f.salario);
	printf("Tamanho salario: %d\n", sizesalario);

	sizedata = sizeof(struct DATA);
	printf("Tamanho data: %d\n", sizedata);

	size = sizeof(struct FUNCIONARIO);
	printf("Tamanho: %d\n", size);

	f.salario = f.salario * 2;
	printf("Salario: %.2f\n", f.salario);

	f.desl.dia = f.ad.dia;
	f.desl.mes = f.ad.mes;
	f.desl.ano = f.ad.ano + 2;
	printf("Data de desligamento: %d, %d, %d", f.desl.dia, f.desl.mes, f.desl.ano);

	struct FUNCIONARIO *p;

	p = &f;

	struct FUNCIONARIO v[50];

	return 0;
}
