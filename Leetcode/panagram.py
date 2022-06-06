
def checkIfPangram(s):
    alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
         'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    count=[0]*26

    sentence = list(s)

    if(len(sentence) < 26):
            return False
    else:
        for i in range(len(sentence)):
            if(sentence[i] in alphabets):
                index=ord(sentence[i])-ord('a')
                count[index]+=1

            
    if(0 in count):
        return False
    else:
        return True


print(checkIfPangram("thequickbrownfoxjumpsoverthelazydog"))
print(checkIfPangram("leetcode"))