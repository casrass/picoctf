import random

DATA = "灩捯䍔䙻ㄶ形楴獟楮獴㌴摟潦弸彥㜰㍢㐸㙽"

if __name__ == "__main__":
        output = ""

        for i in range(len(DATA)):
                output += chr(ord(DATA[i]) >> 8) + chr(ord(DATA[i]) - ((ord(DATA[i]) >> 8) << 8))

        print(output)