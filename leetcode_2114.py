sentences = ["alice and bob love leetcode","i think so too", "this is great thanks very much"]

result = []
for i in range(len(sentences)):
    count = 1
    for j in sentences[i]:
        if(j == " "):
            count = count+1
    result.append(count)
print(max(result))
#return (max(result))


