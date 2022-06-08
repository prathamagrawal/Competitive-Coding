l=[4,3,2,1]
n=len(l)
temp=0
for i in range(n):
    temp=temp + l[i]*pow(10,n-i-1)
temp=temp+1


l=list(map(int, str(temp)))
print (l)