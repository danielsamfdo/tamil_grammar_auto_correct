Vowels=[];
Change=[];
Consonant=[];
Consonant.append(u'\u0B95\u0BCD');
Consonant.append(u'\u0B99\u0BCD');
Consonant.append(u'\u0B9A\u0BCD');
Consonant.append(u'\u0B9E\u0BCD');
Consonant.append(u'\u0B9F\u0BCD');
Consonant.append(u'\u0BA3\u0BCD');
Consonant.append(u'\u0BA4\u0BCD');
Consonant.append(u'\u0BA8\u0BCD');
Consonant.append(u'\u0BAA\u0BCD');
Consonant.append(u'\u0BAE\u0BCD');
Consonant.append(u'\u0BAF\u0BCD');
Consonant.append(u'\u0BB0\u0BCD');
Consonant.append(u'\u0BB2\u0BCD');
Consonant.append(u'\u0BB5\u0BCD');
Consonant.append(u'\u0BB4\u0BCD');
Consonant.append(u'\u0BB3\u0BCD');
Consonant.append(u'\u0BB1\u0BCD');
Consonant.append(u'\u0BA9\u0BCD');
Vowels.append(u'\u0B85');
Vowels.append(u'\u0B86');
Vowels.append(u'\u0B87');
Vowels.append(u'\u0B88');
Vowels.append(u'\u0B89');
Vowels.append(u'\u0B8A');
Vowels.append(u'\u0B8E');
Vowels.append(u'\u0B8F');
Vowels.append(u'\u0B90');
Vowels.append(u'\u0B92');
Vowels.append(u'\u0B93');
Vowels.append(u'\u0B94');
Change.append('');#dummy
Change.append(u'\u0BBE');
Change.append(u'\u0BBF');
Change.append(u'\u0BC0');
Change.append(u'\u0BC1');
Change.append(u'\u0BC2');
Change.append(u'\u0BC6');
Change.append(u'\u0BC7');
Change.append(u'\u0BC8');
Change.append(u'\u0BCA');
Change.append(u'\u0BCB');
Change.append(u'\u0BCC');
pulli=u'\u0BCD';
VERBsuffixes=[];
VERBsuffixes.append(u'\u0B8F\u0BA9\u0BCD');
VERBsuffixes.append(u'\u0B86\u0BAF\u0BCD');
VERBsuffixes.append(u'\u0B88\u0BB0\u0BCD\u0B95\u0BB3\u0BCD');
VERBsuffixes.append(u'\u0B86\u0BA9\u0BCD');
VERBsuffixes.append(u'\u0B86\u0BB0\u0BCD');
VERBsuffixes.append(u'\u0B85\u0BA4\u0BC1');
VERBsuffixes.append(u'\u0B89\u0BAE\u0BCD');
VERBsuffixes.append(u'\u0B93\u0BAE\u0BCD');
VERBsuffixes.append(u'\u0B88\u0BB0\u0BCD\u0B95\u0BB3\u0BCD');
VERBsuffixes.append(u'\u0B86\u0BB0\u0BCD\u0B95\u0BB3\u0BCD');
#for i in range(0,len(Consonant)):
  #  print Consonant[i];


def isVowels(a):
    for i in range(0,len(Vowels)):
        if(Vowels[i]==a):
            return i;
    return -1;


def join(A,B):
    if(A[len(A)-1]==pulli):
        x=isVowels(B[0]);
        if(x==0):
            return A[:len(A)-1]+B[1:];
        elif(x!=-1):
            return A[:len(A)-1]+Change[x]+B[1:];
        else:
            return -1;

        
def searchpresentW(S):
    link=u'\u0B95\u0BBF\u0BB1\u0BCD';
    for i in range(0,len(VERBsuffixes)):
                   print S+join(link,VERBsuffixes[i]);

def searchpresentS(S):
    link=u'\u0B95\u0BCD\u0B95\u0BBF\u0BB1\u0BCD';
    for i in range(0,len(VERBsuffixes)):
                   print S+join(link,VERBsuffixes[i]);

        
def searchfutureW(S):
    link=Consonant[13];
    for i in range(0,len(VERBsuffixes)):
                   print S+join(link,VERBsuffixes[i]);

def searchfutureS(S):
    link=Consonant[8]+Consonant[8];
    for i in range(0,len(VERBsuffixes)):
                   print S+join(link,VERBsuffixes[i]);


def findleng(Word):
    cnt=0;
    for i in range(0,len(Word)):
        letter=Word[i];
        for j in range(1,len(Change)):
            if(letter==Change[j]):
                cnt=cnt+1;
                break;
            if(letter==pulli):
                cnt=cnt+1;
                break;
    return len(Word)-cnt;


def findlen(Word):
    if(findleng(Word)==2):
        Lcnt=0;
        for i in range(0,len(Word)):
            letterz=Word[i];
            if(isLongVowelSound(letterz)):
                Lcnt+=1;
            elif(isLongVowel(letterz)):
                Lcnt+=1;
        if(Lcnt==0):
            return "short2";
        else:
            return "notshort2";
    return "notshort2";
        
def isSecondletterConsonant(Word):
    for i in range(0,len(Change)):
        if(Word[1]==Change[i]):
            if(len(Word)==4):
                if((Word[3]==u'\u0BCD')):
                    return 2;
                else:
                    return -1;
            else:
                return -1;
    if(Word[2]==u'\u0BCD'):
        return 1;
    return -1;

def checkforVowel1(letterx):
    for i in range(1,len(Change)):
        if(letterx==Change[i]):
            return 0;
    if(letterx==pulli):
        return 0;
    return 1;


def NoofSyllables(Word):
    scnt=0;
    for i in range(0,len(Word)):
        lettery=Word[i];
        for j in range(1,len(Change)):
            if(lettery==Change[j]):
                scnt+=1;
                continue;
        for k in range(0,len(Vowels)):
            if(lettery==Vowels[k]):
                scnt+=1;
        if(lettery==pulli):
            scnt+=1;
    return scnt;


def SuffixAdd(Word,Suffix):
    Vowelno=isVowels(Suffix[0]);
    if(Vowelno!=-1):
        if((Word[len(Word)-1]==Change[2]) | (Word[len(Word)-1]==Change[3]) | (Word[len(Word)-1]==Change[7]) | (Word[len(Word)-1]==Change[8]) ):
            return Word+join(Consonant[10],Suffix);
        if((checkforVowel1(Word[len(Word)-1])) | (Word[len(Word)-1]==Change[1]) | (Word[len(Word)-1]==Change[5]) | (Word[len(Word)-1]==Change[9]) | (Word[len(Word)-1]==Change[10]) | (Word[len(Word)-1]==Change[11])):
            return Word+join(Consonant[13],Suffix);
        if(Word[len(Word)-1]==Change[4]) :
            Wordlen=findlen(Word);
            if(Wordlen=='short2' ):
                    return Word+join(Consonant[13],Suffix);
            else:
                return Word[:len(Word)-1]+Change[Vowelno]+Suffix[1:len(Suffix)];
        if(findlen(Word)=="short2" ) :
            index=isSecondletterConsonant(Word);
            #print index;
            if(index!=-1):
                return Word[:index+2]+join(Word[index:index+2],Suffix);
    if(Word[len(Word)-1]==pulli):
        return join(Word,Suffix);
    return Word+Suffix;


def isLongVowelSound(letterz):
    if((letterz==Change[1]) |(letterz==Change[3]) |(letterz==Change[5]) |(letterz==Change[7]) |(letterz==Change[9]) |(letterz==Change[11]) ):
        return 1;
    return 0;

def isLongVowel(letterz):
    if((letterz==Vowels[1]) |(letterz==Vowels[3]) |(letterz==Vowels[5]) |(letterz==Vowels[7]) |(letterz==Vowels[9]) |(letterz==Vowels[11])|(letterz==Vowels[10])): ##10 was added for droppin ):
        return 1;
    return 0;


def Nounplural(Word):
    if(Word[len(Word)-2:len(Word)]==Consonant[9]):
        return Word[:len(Word)-2]+Consonant[1]+u'\u0B95'+Consonant[15];
    Syl=NoofSyllables(Word);
    if(Syl==1):
        if(isLongVowelSound(Word[len(Word)-1])):
            return Word+Consonant[0]+join(Consonant[0],Vowels[0])+Consonant[15];
        else:
            if(Word[len(Word)-2:len(Word)]==Consonant[12]):
                return Word[:len(Word)-2]+Consonant[16]+u'\u0B95'+Consonant[15];
            elif(Word[len(Word)-2:len(Word)]==Consonant[15]):
                return Word[:len(Word)-2]+Consonant[4]+u'\u0B95'+Consonant[15];
    return Word+u'\u0B95'+Consonant[15];

def SuffixNum(Word,Link):
    return Word[:len(Word)-1]+Change[1]+Link[1:];
            
"""               
#Simple Present        
print "Simple Present        ";
F1=open('D:\\cp\\WEAKVERBS.txt');
V=F1.readline();
print V[2:len(V)-3];
S=V[2:len(V)-3].decode('utf-16');
searchpresentW(S);
F1.close();

F2=open('D:\\cp\\STRONGVERBS.txt');
V=F2.readline();
S=V[2:len(V)-3].decode('utf-16');
searchpresentS(S);
F2.close();

#simple future
print "Simple Future";
F1=open('D:\\cp\\WEAKVERBS.txt');
V=F1.readline();
print V[2:len(V)-3];
S=V[2:len(V)-3].decode('utf-16');
searchfutureW(S);
F1.close();

F2=open('D:\\cp\\STRONGVERBS.txt');
V=F2.readline();
S=V[2:len(V)-3].decode('utf-16');
searchfutureS(S);
F2.close();

print "*******************"

#print plurals of nouns
f=open('D:\\x\\nouns.txt');
V=f.readline();
S=V[2:len(V)-3].decode('utf-16');
print Nounplural(S);
while 1:
    V=f.readline();
    if not V:
        break;
    S=V[1:len(V)-3].decode('utf-16');
    if(len(S)>0):
        print Nounplural(S);

f.close();


#print adjectives
f=open('D:\\x\\nouns.txt');
V=f.readline();
S=V[2:len(V)-3].decode('utf-16');
Link=Vowels[1]+u'\u0BA9';
print SuffixAdd(S,Link);
while 1:
    V=f.readline();
    if not V:
        break;
    S=V[1:len(V)-3].decode('utf-16');
    if len(S)>=1:
        print SuffixAdd(S,Link);
f.close();

#print adverbs
f=open('D:\\x\\nouns.txt');
V=f.readline();
S=V[2:len(V)-3].decode('utf-16');
Link=Vowels[1]+u'\u0B95';
print SuffixAdd(S,Link);
while 1:
    V=f.readline();
    if not V:
        break;
    S=V[1:len(V)-3].decode('utf-16');
    if len(S)>=1:
        print SuffixAdd(S,Link);
f.close();
"""

#print Commands 
f=open('D:\\cp\\WEAKVERBS.txt');
V=f.readline();
S=V[2:len(V)-3].decode('utf-16');
Link=Vowels[4]+u'\u0B99\u0BCD\u0B95\u0BB3\u0BCD';
print Link;
print SuffixAdd(S,Link);

while 1:
    V=f.readline();
    if not V:
        break;
    S=V[1:len(V)-3].decode('utf-16');
    if len(S)>=1:
        print SuffixAdd(S,Link);
        
f.close();

#print negative commands 
f=open('D:\\cp\\WEAKVERBS.txt');
V=f.readline();
S=V[2:len(V)-3].decode('utf-16');
Link=Vowels[1]+u'\u0BA4\u0BC7';
Link2=Vowels[1]+u'\u0BA4\u0BC0'+Consonant[11]+u'\u0B95'+Consonant[15];
print Link;
print Link2;
print SuffixAdd(S,Link);
print SuffixAdd(S,Link2);
while 1:
    V=f.readline();
    if not V:
        break;
    S=V[1:len(V)-3].decode('utf-16');
    if len(S)>=1:
        print SuffixAdd(S,Link);
        print SuffixAdd(S,Link2);
f.close();

Check=u'\u0B95\u0BC8';
print Check;
print NoofSyllables(Check);
print Nounplural(Check);

###adding Suffixes
f=open('D:\\cp\\Check.txt');
V=f.readline();
S=V[2:len(V)-3].decode('utf-16');
print SuffixAdd(S,VERBsuffixes[6]);
while 1:
    V=f.readline();
    if not V:
        break;
    S=V[1:len(V)-3].decode('utf-16');
    if len(S)>=1:
        print SuffixAdd(S,VERBsuffixes[6]);
f.close();

Check=u'\u0BA4\u0BAE\u0BCD\u0BAA\u0BBF';
print SuffixAdd(Check,VERBsuffixes[6]);
print Check;
#print isVowels(VERBsuffixes[6][0]);

print Check+join(Consonant[10],VERBsuffixes[6]);

Check=u'\u0BA4\u0B99\u0BCD\u0B95\u0BC8';
print Check;
print SuffixAdd(Check,VERBsuffixes[6]);

Check=u'\u0B85\u0BAE\u0BCD\u0BAE\u0BBE';
print Check;
print SuffixAdd(Check,VERBsuffixes[6]);

Check=u'\u0BA8\u0BC0';
print Check;
print SuffixAdd(Check,VERBsuffixes[6]);


Check=u'\u0BAA\u0BC6\u0BA3\u0BCD';
print Check;
print SuffixAdd(Check,VERBsuffixes[6]);


Check=u'\u0BAA\u0B9A\u0BC1';
print Check;
#print findleng(Check);
#print findlen(Check);
print SuffixAdd(Check,VERBsuffixes[6]);

Check=u'\u0BAE\u0BBE\u0B9F\u0BC1';
print Check;
print SuffixAdd(Check,VERBsuffixes[6]);
print "******************************";

### Ordinal Numbers
f=open('D:\\cp\\Numbers.txt');
V=f.readline();
S=V[2:len(V)-3].decode('utf-16');
Link=u'\u0B86\u0BB5\u0BA4\u0BC1';
print SuffixNum(S,Link);
while 1:
    V=f.readline();
    if not V:
        break;
    S=V[1:len(V)-3].decode('utf-16');
    if len(S)>=1:
        print SuffixNum(S,Link);
f.close();

### Ordinal Days
f=open('D:\\cp\\Numbers.txt');
V=f.readline();
S=V[2:len(V)-3].decode('utf-16');
Link=u'\u0B86\u0BAE\u0BCD';
print SuffixNum(S,Link);
while 1:
    V=f.readline();
    if not V:
        break;
    S=V[1:len(V)-3].decode('utf-16');
    if len(S)>=1:
        print SuffixNum(S,Link);
f.close();
