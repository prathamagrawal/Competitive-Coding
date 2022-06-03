nums=[2,2,1]

for i in range(len(nums)):
    if(nums.count(nums[i])==1):
        print(nums[i])