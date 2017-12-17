#include <stdio.h>
#include <string.h>

int main()
{
	char* flag = "flag{Have_u_tried_GDB?}";
	int len = strlen(flag);
	char encrypted[len];
	for(int i = 0; i < len; i++)
		encrypted[i] = (2 * i) ^ flag[i];

	/* printf("%d\n", len); */
	/* printf("%s\n", encrypted); */
	/* printf("%d\n", strlen(encrypted)); */
	for(int i = 0; i < len; i++)
		printf("%x %c\n", encrypted[i], encrypted[i]);
	return 0;
}
