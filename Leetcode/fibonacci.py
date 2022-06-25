def fin(n):
    x,y,z=0,1,1
    l=[]
    result=x+y+z
    l.append(x)
    l.append(y)
    l.append(z)

    for i in range(n):
        result=x+y+z
        x=y
        y=z
        z=result
        l.append(result)
        
    return l[n]
print(fin(25))