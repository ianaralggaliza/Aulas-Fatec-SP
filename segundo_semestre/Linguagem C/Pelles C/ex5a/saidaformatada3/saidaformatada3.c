#include <stdio.h>
int main(void)
{
	char x, a, b, ch = 'A';
	unsigned char c, d;

	x = 'A' + '0';
	a = ch + 62;
	b = 'A'+'A';
	c = 'A'+'A';
	d = ch+80;

	printf("\nSabemos que char em C e um numero\n");
	printf("\n %d, %d", ch, x);
	printf("\n %d, %d", ch, a);
	printf("\n %d, %d", ch, b);
	printf("\n %d, %d", ch, c);
	printf("\n %d, %d", ch, d);

	return 0;
}
