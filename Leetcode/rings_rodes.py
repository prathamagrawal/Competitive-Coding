rings="B0B6G0R6R0R6G9"

data={}

for i in range(0, len(rings)-1,1):
    m=i+1
    data[rings[i]]=rings[m]

print(data)