'''
Reversal Sorting Problem Code: REVSORT
Add problem to Todo list
Submit
Chef is deriving weird ways to sort his array. Currently he is trying to sort his arrays in increasing order by reversing some of his subarrays.

To make it more challenging for himself, Chef decides that he can reverse only those subarrays that have sum of its elements at most X. Soon he notices that it might not be always possible to sort the array with this condition.

Can you help the Chef by telling him if the given array can be sorted by reversing subarrays with sum at most X.

More formally, for a given array A and an integer X, check whether the array can be sorted in increasing order by reversing some (possibly none) of the subarrays such that the sum of all elements of the subarray is at most X.

Input Format
First line will contain T, number of test cases. Then the test cases follow.
The first line of each test case contains of two space-separated integers N and X denoting the length of the array and the maximum sum of subarrays that you can reverse.
The second line contains N space-separated integers A1,A2,...,AN representing the initial array.
Output Format
For each test case, output ðð´ð if Chef can sort the array using a finite number of operations, else output ð½ð¾.

You may print each character of the string in uppercase or lowercase (for example, the strings ððð, ð¢ð´ð, ð¢ðð and ðð´ð will all be treated as identical).

Constraints
1â¤Tâ¤5â104
1â¤Nâ¤105
1â¤Aiâ¤2â109
1â¤Xâ¤2â109
Sum of N over all test cases does not exceeds 3â105.
Sample Input 1 
3
4 1
1 2 3 4
4 1
2 1 3 4
5 7
3 2 2 3 3
Sample Output 1 
YES
NO
YES
'''
def calc(array,x):
    result=True
    for i in range(len(array)-1):
        if(array[i]>array[i+1]):
            if(array[i]+array[i+1]<=x):
                temp=array[i]
                array[i]=array[i+1]
                array[i+1]=temp
            else:
                result=False
                break
    
    return result

for i in range(int(input())):
    length,s=input().split(' ')
    array=[int(x) for x in input().split()]
    if(calc(array,int(s))==True):
        print("YES")
    else:
        print("NO")
    