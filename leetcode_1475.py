from sre_parse import FLAGS


prices=[8,4,6,2,3]

index=[]
for i in range(len(prices)):
    flag=True
    for j in range(i+1,len(prices)):
        if(prices[i]>=prices[j]):
            prices[i]=prices[i]-prices[j]
            flag=False
            break
    if(flag==True):
        prices[i]=prices[i]

print(prices)