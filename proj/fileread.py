f=open('D:\proj\pronouns.txt');
V=f.readline();
print V[2:len(V)-3].decode('utf-16');
while 1:
    V=f.readline();
    if not V:
        break;
    print V[1:len(V)-3].decode('utf-16');
f.close();
