#include <stdio.h>

int main (void)
{
/*	float a = 20.0, b = 125.0, c = 1000.0, d = 1700.5;

	printf("\n %8.1f %8.1f", a, b);
	printf("\n %8.1f %8.1f", c, d);
	printf("\n %-8.1f %-8.1f", a, b);
	printf("\n %-8.1f %-8.1f", c, d);
	printf("\n %04d", 10);
	printf("\n %d %c", 97, 97);
	printf("\n %d", 'A' + 'A');
*/
/*
	printf("\nUm\n\tDois\n\t\tTres");
	printf("\nDecimal %03d corresponde %02XHexa", 10, 10);
	printf("\nDecimal %03d corresponde %02xhexa", 10, 10);
*/
/*	int x = 2, y = 1, z = 0;
	int resultado;
	resultado = !0 && y || z; 
	printf("resultado: %d", resultado);
*/
	int x=2, int y=3, int z=4, int k;
	int resultado;
	resultado = (k = x == (y=z)) ; 
	printf("resultado: %d", resultado);

	return 0;
}
