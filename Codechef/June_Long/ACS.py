''''
Count the ACs Problem Code: ACS
Add problem to Todo list
Submit
There are 10 problems in a contest. You know that the score of each problem is either 1 or 100 points.

Chef came to know the total score of a participant and he is wondering how many problems were actually solved by that participant.

Given the total score P of the participant, determine the number of problems solved by the participant. Print −1 in case the score is invalid.

Input Format
First line will contain T, number of test cases. Then the test cases follow.
Each test case contains of a single line containing a single integer P - denoting the number of points scored by the participant.
Output Format
For each testcase, output the number of problems solved by the participant or −1 if the score is invalid.

Constraints
1≤T≤1000
0≤P≤1000
Sample Input 1 
5
103
0
6
142
1000
Sample Output 1 
4
0
6
-1
10
'''

def calc(n):
    count=0
    if(n<0):
        return -1
    elif(n==0):
        return 0
    else:
        while(n!=0):
            if(n>=100):
                n-=100
                count+=1
            else:
                n-=1
                count+=1

        if(count>10):
            return -1
        else:
            return count
        
for i in range(int(input())):
    print(calc(int(input())))