#include <stdio.h>
#include <stdlib.h>

int main(void)
{
	static char *tai[4] = {"Finlandia", "EUA", "Suecia", "Japao"};
	char **p = tai;
	
	system("CLS");


	printf("%s\n", tai[0]);		
	printf("%s\n", *(p + 2));
	printf("%s\n", p[3]);
/*   
	printf("%d\n", p);
	printf("%s\n", *(p+2));
    printf("%s\n", p[2]);
    printf("\n");
*/
//	printf("%s\n", p[3]);
    printf("%d\n", *p[3]);
	printf("%d\n", &p[2]);
	printf("%d\n", &p[3]);
    printf("\n");
//	printf("%d\n", tai);
//	printf("%s\n", *tai);
//	printf("%d\n", &tai);
//	printf("\n");
//	printf("%d\n", tai[0]);
    printf("%d\n", *tai[3]);
	printf("%d\n", &tai[2]);
	printf("%d\n", &tai[3]);

	

	system("PAUSE");

	return 0;
}
