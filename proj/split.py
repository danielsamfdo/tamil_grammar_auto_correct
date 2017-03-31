def search(a,filename,type):
    f1=open(filename);
    V=f1.readline();
    if(V[2:len(V)-3].decode('utf-16')==a):
        print type;
        return ;
    else:
        while 1:
            V=f1.readline();
            if not V:
                break;
            if(V[1:len(V)-3].decode('utf-16')==a):
                print type;
                return ;
    f1.close();
    
f=open('D:\split.txt');
V=f.readline();
S=V[2:len(V)-3].decode('utf-16').split();
for i in range(0,len(S)):
    print S[i];
    search(S[i],'pronouns.txt','PRONOUN');          
f.close();
