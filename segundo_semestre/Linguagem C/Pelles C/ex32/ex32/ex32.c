#include <stdio.h>
int ocorrencia(char s[], char ch);//prototipo

int ocorrencia(char s[], char ch){
	int i;
	int oc=0;
	
	for (i=0; s[i] != '\0'; i++){
		if (s[i] == ch){
			oc += 1;
		}
	}
	return oc;
}

int main (void)
{
	int resultado;
	char bla[] = "Ola sou a Ianara. Eu tenho 24 anos.!"; //definindo string
	char b = 'a'; //definindo o segundo parametro que entrara na funcao
	resultado = ocorrencia(bla, b);
	printf("A letra %c aparace %d vezes.\n", b,resultado);


	resultado = ocorrencia("Minha string", 't');
	printf("A letra %c aparace %d vezes.\n", 't',resultado);

	return 0;
}


