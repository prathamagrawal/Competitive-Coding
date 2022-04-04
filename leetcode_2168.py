def test1(num1,num2):
    count = 0
    if(num1 == 0):
        return 0
    elif(num2 == 0):
        return 0
    elif(num1 == num2):
        return 1
    else:
        while num1 != 0 or num2 != 0 :
            if(num1 >= num2):
                num1 = num1-num2
                count += 1
            elif(num2>=num1):
                num2 = num2-num1
                count += 1
            
            if(num1 == 0) or (num2 == 0):
                break
        return count



num1 = 10
num2 = 10
print(test1(num1, num2))



