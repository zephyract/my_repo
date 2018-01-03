/* gcc stack2.c -fno-stack-protector -no-pie -o stack2 */
#include <stdio.h>
#include <stdlib.h>

void vuln()
{
	printf("You're not supposed to enter this function!\n");
}

int main()
{
	char buf[0x10] = {0};
	printf("Give me your payload: ");
	scanf("%s", buf);
	printf("your payload is: %s", buf);
	return 0;
}
