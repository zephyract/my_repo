//gcc pwn300.c -fstack-protector-all -o0 -m32 -o pwn300
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <unistd.h>
#include <time.h>

static char username[10] = "M4x";
static int len = 6;

int main()
{
	setbuf(stdin, 0);
	setbuf(stdout, 0);
	setbuf(stderr, 0);

    char password;
	int seed = time(NULL);

	puts("先注册吧\n");
	puts("用户名:(不多于10位) ");
	read(0, &username, 0x16);
	puts("密码:(不多于6位的数字) ");
	read(0, &password, len);

	puts("接下来,猜对100次吧\n");
	int i;
	int guess;

	srand(seed);
	for(i = 0; i < 100; i++)
	{
		srand(rand());
		printf("第%d次\n", i);
		puts("随机种子已重置,接着猜吧\n");
		
		scanf("%d", &guess);
		if(guess != rand() % 0x1234 + 1)
		{
			puts("猜错了, gg\n");
			return 0;
		}
	}

	if(i == 100)
	{
		puts("猜对了100次, 老哥稳\n");
		system("/bin/sh");
	}
	return 0;

}
