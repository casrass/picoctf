

def decodeToFlag(string):
    flag = ""
 
    for i in range(len(string)):
        flag += chr((ord(string[i]) >> 8))
        #flag += chr(ord(string[i]) - (ord(string[i]) >> 8))
 
    return flag
 
 
print(decodeToFlag("灩捯䍔䙻ㄶ形楴獟楮獴㌴摟潦弸彥㜰㍢㐸㙽"))
    