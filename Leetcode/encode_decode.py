import random
import re
import string


data={}


def encode(longUrl):
    lower_upper_alphabet = string.ascii_letters
    longUrl=longUrl.split("/")
    code=""
    if("https:" in longUrl):
        longUrl.remove("https:")
        data["s"]="https:/"
        code=code+"s"
    else:
        longUrl.remove("http:")
        data["h"]="http:/"
        code=code+"h"
    longUrl.remove("")
    for i in longUrl:
        random_letter = random.choice(lower_upper_alphabet)
        if(random_letter in data.keys()):
            random_letter = random.choice(lower_upper_alphabet)
        data[random_letter] =i
        code=code+random_letter
    return "http://tinyurl.com/"+code



def decode(shortUrl):
    shortUrl=shortUrl.replace("http://tinyurl.com/","")
    code=""
    for i in range(0,len(shortUrl)):
        if(shortUrl[i] in data.keys()):
            code=code+str(data.get(shortUrl[i]))+"/"
            print(code)
    code=code[0:-1]
    return code


s="http://example.net/amusement/afterthought.aspx"
result=encode(s)
print(result)
print(decode(result))


