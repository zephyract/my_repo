#include <stdio.h>
#include <stdlib.h>

int main()
{
	srand(0x61616161);
	for(int i = 0; i < 100; i++)
	{
		int v3 = rand();
		srand(v3);
		printf("%d, ", rand() % 4660 + 1);
	}

	return 0;
}
