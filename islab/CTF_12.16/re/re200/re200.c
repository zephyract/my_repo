//gcc re200.c -no-pie -masm=intel -o re200
#include <stdio.h>
#include <string.h>

#define junk \
    __asm__ ("  push     rax      \n"\
             "  xor      eax, eax \n"\
             "  jz       islab   \n"\
             "  add      rsp, 4   \n"\
             "islab:             \n"\
             "  pop      rax      \n");

char* encrypted = "fneasBmxuMaIlhu{D}cbj\x15Q";
char input[50];

int check()
{
	junk;
		int len = strlen(input);
		char flag[50];

		for(int i = 0; i < len; i++)
			flag[i] = (2 * i) ^ encrypted[i];
	
		if(!strncmp(flag, input, len) && len == 23)
			return 1;

		__asm__(
		" jmp bitss	\n"
		" call rax	\n"
		" pop rax	\n"
		" add rsp,	5	\n"
		"rep stos dword ptr [edi]	\n"
		"bitss:	\n"
		" mov rax, 0	\n"
	   );


		return 0;
}

int main()
{
	printf("Give me your flag: ");
	scanf("%s", input);

	if(check())
		printf("log, when!\n");
	else
		printf("Wrong input\n");

	return 0;
}
