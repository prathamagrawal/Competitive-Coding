import random
import re
import string


data={}


def encode(longUrl):
    lower_upper_alphabet = string.ascii_letters
    random_letter = random.choice(lower_upper_alphabet)
    data[random_letter] = longUrl
    return longUrl+random_letter
    


def decode(shortUrl):
    return data.get(shortUrl[-1])


s="http://example.net/amusement/afterthought.aspx"
result=encode(s)
print(result)
print(decode(result))


