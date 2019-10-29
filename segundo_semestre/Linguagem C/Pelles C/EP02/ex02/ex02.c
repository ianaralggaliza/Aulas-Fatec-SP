# include <stdio.h>

void push(TPilha *p, char x);

int main (void){
	typedef struct pilha {
			char vet[10];
			int topo;
		} TPilha;
}

void push(TPilha *p, char x)
{
	if (isfull(p) {
		printf("overflow\n");
		abort();
	}
	p->topo++;
	p->vet[p->topo] = x;
}
