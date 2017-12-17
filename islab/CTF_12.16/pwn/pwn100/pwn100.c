//gcc pwn100.c -fno-stack-protector -o pwn100
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void getShell()
{
	printf("Simple pwn. Enjoy your shell.\n");
	system("/bin/sh");
}

int main()
{	
	setbuf(stdin, 0);
	setbuf(stdout, 0);
	setbuf(stderr, 0);
	char buf[40];
	printf("This is an easy stackOverFlow challenge.\n\n");
	printf("All you need to do is ret to %p\n\n", getShell);
	printf("Give me your payload: ");
	scanf("%s", buf);
	printf("Now your ret address is %c%c%c%c%c%c%c%c", buf[0x38 + 7], buf[0x38 + 6], buf[0x38 + 5], buf[0x38 + 4], buf[0x38 + 3], buf[0x38 + 2], buf[0x38 + 1], buf[0x38]);

	return 0;
}
