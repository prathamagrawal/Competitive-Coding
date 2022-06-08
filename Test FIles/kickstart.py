def speed_typing(originial,real):
    if(len(orginal)==len(real)):
        if(orginial==result):
            return 0
        else:
            return -1
    elif(len(orginal)<len(real)):
        if(orginial in result):
            return len(real)-len(orginal)
        else:
            return -1;
    else:
        return -1;


def charcheck(orginal,real):
    count=0
    if(len(orginal)<len(real)):
        for i in orginal:
            if(i not in real):
                count+=1
    print(count)


char

t=int(input())
l=[]
for i in range(t):
    original = input()
    real=input()
    l.append(speed_typing(originial,real))
print(l)
