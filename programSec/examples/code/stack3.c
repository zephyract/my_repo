/* gcc stack3.c -fno-stack-protector -no-pie -o stack3 */
#include <stdio.h>
#include <stdlib.h>

void vuln()
{
	printf("Enjoy your shell!\n");
	system("/bin/sh");
}

int main()
{
	setbuf(stdin, 0);
	setbuf(stdout, 0);
	setbuf(stderr, 0);
	char buf[0x10] = {0};
	printf("Give me your payload: ");
	scanf("%s", buf);
	printf("your payload is: %s", buf);
	return 0;
}
