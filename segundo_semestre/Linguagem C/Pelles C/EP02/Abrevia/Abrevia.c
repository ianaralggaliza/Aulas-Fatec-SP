/*
------------------------------------------------------------------------------------------
Instituição		: Faculdade de Tecnologia de São Paulo
Departamento	: Tecnologia da Informação
Curso			: Análise e Desenvolvimento de Sistemas
Diciplina		: ILP-010
Turno			: Tarde
Aluno			: Ianara Leite Gonçalves Galiza
Matrícula		: 18203711
Aluno			: Karina Formentini Dinella
Matrícula		: 18211195
------------------------------------------------------------------------------------------
Programa 		: EP02.c - Abreviacao de Nomes
Línguagem		: ANSI C
Compilador		: Pelles C (8.00.60)
------------------------------------------------------------------------------------------
*/


#include <stdio.h>

int conta_espacos(char nome[]);
void abrevia(char nome[]);


int main (void)
{
	char nome[40];
	printf("Insira um nome completo: \n");
	gets(nome);
	abrevia(nome);
	return 0;
}

int conta_espacos(char nome[])
{
	int i;
	int cont=0;
	for(i=0; nome[i]!='\0'; i++){
		if (nome[i]==' '){
			cont += 1;
		}
	}
	return cont;
}

void abrevia(char nome[])
{
	int total_de_espacos;
	int i;
	int j;
	int k;
	int qtd_apagar=0;
	int num_de_espacos=0;
	total_de_espacos = conta_espacos(nome);
	if (total_de_espacos <= 1){  // Lida com o caso de apenas um nome e um sobrenome
		puts(nome);
	}
	else{
		for(i=0; ((nome[i]!= '\0') && (num_de_espacos<(total_de_espacos-1))); i++)
		{	
			if(nome[i]==' '){
				num_de_espacos++;
				qtd_apagar=0;
				if ((65<=(nome[i+1]) && (nome[i+1])<=90)){ // Verifica se e letra maiuscula
					nome[i+2]='.'; // Insere ponto apos letra maiuscula
					for(k=i+3; nome[k]!=' '; k++){
						qtd_apagar += 1; // Quantidade de letras do sobrenome a serem apagadas
					}
					for(j=i+3; nome[j+qtd_apagar]!='\0'; j++)
					{
						nome[j]=nome[j+qtd_apagar]; // Move para a esquerda o restante do sobrenome
					}
					nome[j]='\0'; // Reduz o tamanho da string
				}
			}
		}
		puts(nome);	
	}
}
