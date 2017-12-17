//gcc fmt.c -no-pie -m32 -o hiddenLevel
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int key1 = 123, key2 = 456;

void init()
{
	setbuf(stdin, 0);
	setbuf(stdout, 0);
	setbuf(stderr, 0);

	printf("\n");
	printf("[*]Wow you're so lucky to find this hidden level.\n");
	printf("[*]It's a simple format string bug.\n");
	printf("[*]M4x think you can make it after ten-minute googling.\n");
	printf("[*]If you solve this, you will get 100 bonus.\n");
	printf("[*]Come on!\n\n");
	printf("[!]Submit this flag to pwn100.\n\n");
}

int main() 
{
	init();
  int key3 = 789;
  char s[100];

  printf("%p\n", &key3);
  do
  {
	  scanf("%s", s);
	  printf(s);
	  printf("\n");
  }
  while(strcmp(s, "pwn!"));

  if(key1 == 2)
  {
	  printf("Level 1 Clear!\n");
	  if(key2 == 0x12345678)
	  {
		  printf("Level 2 Clear!\n");
		  if(key3 == 16)
		  {
			  printf("Level 3 Clear!\n");
			  printf("Congratulations!\n");
			  system("/bin/sh");
		  }
	  }
  }

  printf("Failed!\n");

  return 0;
}
