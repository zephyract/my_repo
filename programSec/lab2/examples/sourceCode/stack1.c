/* gcc stack1.c -o stack1 */
#include <stdio.h>

int main()
{
	char buf[0x10];
	int a = 0;
	int b = 0;
	int c = 0;
	int d = 0;
	printf("请输入长度在0x10内的字符串: ");
	scanf("%s", buf);
	if(d)
	{
		printf("d != 0 now.\n");
		if(c)
		{
			printf("c !- 0 now.\n");
			if(b)
			{
				printf("b != 0 now.\n");
				if(a)
				{
					printf("a != 0 now.\n");
				}
			}
		}
	}
	return 0;
}
