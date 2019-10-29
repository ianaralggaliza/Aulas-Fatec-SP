#include <stdio.h>

void codifica(char msg[], char cod[]){
	int p; // declarando o primeiro digito
	int s; // declarando o segundo digito
	int char_int; // declarando o conversor de char para int
	for (int i=0; msg[i] != '\0'; i++){ 
		char_int = msg[i]; // converte o char para int
		p = char_int / 10; // primeiro digito do int
		s = char_int % 10; // segundo digito do int
		cod[2*i] = p + 48; // converte (0 a 9) int para char - 1o. digito
		cod[2*i+1] = s + 48; // converte (0 a 9) int para char - 2o. digito
	}
	
}

void decodifica(char cod[], char msg[]){
	int i=0;
	int p;
	int s;
	int d;
	int int_char;
	while (cod[2*i] != '\0'){
		int_char = cod[2*i];
		p = (int_char - 48) * 10;
		int_char = cod[2*i + 1];
		s = (int_char - 48);
		d = p + s;
		msg[i] = d;
		i++;
	}
}


int main (void)
{
	int limite_conteudo=50;
	char msg[limite_conteudo+1];
	char cod[2*limite_conteudo+1];

	printf("Insira uma mensagem de ate 50 caracteres.\n");

	gets(msg);

	//codifica(msg, cod);
	
	//printf("Mensagem Codificada:\n");
	puts(msg);

	//msg[0] = '0/'; // limpa msg para garantir que decodificacao funciona.
	//decodifica(cod, msg);

	//printf("Mensagem Decodificada:\n");
	//puts(msg);

	return 0;
}

