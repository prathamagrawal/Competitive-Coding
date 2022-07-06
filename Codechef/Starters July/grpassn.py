def assignment(arr,size):
    d={}
    for i in arr:
        d[i]=arr.count(i)
    
    keys=list(d.keys())
    values=list(d.values())

    for i in range(len(keys)):
        if(values[i]%keys[i]!=0):
            return False
    return True


test=int(input())

for i in range(test):
    size=int(input())
    arr=[int(x) for x in input().split(' ')]
    if(assignment(arr,size)):
        print("YES")
    else:
        print("NO")