from pwn import *

# pwntools method

elf = context.binary = ELF("./warm")

def method1():
	print(elf.string(next(elf.search(b"picoCTF{"))))

# just read the file method

def method2():
	file = open("warm","rb").read()

	base = file.find(b'picoCTF{')

	flag = ""

	for x in range(base, len(file)):
		if file[x] != 0:
			flag += chr(file[x]);
		else:
			break;

	print(flag) # could be more or less than 40 chars but just adjust it untill u get the whole thing

if __name__ == "__main__":
	#method1()
	method2()