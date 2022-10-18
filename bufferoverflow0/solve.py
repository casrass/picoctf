from pwn import *

elf = context.binary = ELF("./vuln")

OFFSET = 28

if __name__ == "__main__":
	

