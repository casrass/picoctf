from pwn import *

elf = context.binary = ELF("./vuln")

if __name__ == "__main__":
	do_nothing_address = elf.functions["doNothing"].address

	print(elf.disasm(do_nothing_address, 16))

	#elf.asm(do_nothing_address + 16, """
	#	call 0xf7ddc0d0;
	#""")

	#print(do_nothing_address)