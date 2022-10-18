from pwn import *

elf = context.binary = ELF("./matrix")

if __name__ == "__main__":
	data = elf.read(0x20f0, 0x5d1) # read matrix into string

	print(data)