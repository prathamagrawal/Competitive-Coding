arr=[1,2,3,4]

runningsums=[]
temp=0
for i in range(len(arr)):
    temp=temp + arr[i]
    runningsums.append(temp)

print(runningsums)