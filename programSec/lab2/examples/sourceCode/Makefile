all:
	@gcc stack1.c -o ../elf/stack1
	@echo "stack1 Ready."
	@gcc stack2.c -fno-stack-protector -no-pie -o ../elf/stack2
	@echo "stack2 Ready."
	@gcc stack3.c -fno-stack-protector -no-pie -o ../elf/stack3
	@echo "stack3 Ready."
	@echo "All elf are in ../elf"

clean:
	@rm ../elf/*
	@echo "remove stack* over"
