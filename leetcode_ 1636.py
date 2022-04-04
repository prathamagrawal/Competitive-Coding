nums=[1,2,3,1,1,3]

count=0

for i in range(len(nums)):
    for j in range(i+1,len(nums)):
        if(nums[i]==nums[j]):
            count=count+1
            print(i,j)

print(count)
