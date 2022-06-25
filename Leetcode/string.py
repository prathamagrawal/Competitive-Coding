import numpy
s="abacbc"
data={}
s=list(s)

for i in s:
    data[i]=s.count(i)

values=numpy.array(list(data.values()))

if(len(numpy.unique(values))):
    print(False)
else:
    print(True)
