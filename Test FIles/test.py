def speedcheck(og,real):
    oglist=list(og)
    reallist=list(real)
    flag=True
    if(og in real):
        flag==True 
        return len(real)-len(og)   
    elif(len(oglist)<=len(reallist)):
        for i in range(len(oglist)):
            if(oglist[i] in reallist):
                reallist.remove(oglist[i])
                flag=True
            else:
                flag=False
                break
    if(flag==True):
        return len(reallist)
    else:
        return -1
                


t = int(input())
l=[]
for i in range(t):
    og=raw_input()
    real=raw_input()
    l.append(speedcheck(og,real))

for i in range(len(l)):
    if(l[i]==-1):
        print("Case #"+str(i+1)+": IMPOSSIBLE")
    else:
        print("Case #"+str(i+1)+": "+str(l[i]))
