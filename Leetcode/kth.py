arr=["d","b","c","b","c","a"]
k=2

data={}
for i in arr:
    data[i]=arr.count(i)
l=[]
for key,value in data.items():
    if(value==1):
        l.append(key)

print(l[k-1])