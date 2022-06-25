''''
Fitness Problem Code: FIT
Add problem to Todo list
Submit
Chef wants to become fit for which he decided to walk to the office and return home by walking. It is known that Chef's office is X km away from his home.

If his office is open on 5 days in a week, find the number of kilometers Chef travels through office trips in a week.

Input Format
First line will contain T, number of test cases. Then the test cases follow.
Each test case contains of a single line consisting of single integer X.
Output Format
For each test case, output the number of kilometers Chef travels through office trips in a week.

Constraints
1≤T≤10
1≤X≤10
Sample Input 1 
4
1
3
7
10
Sample Output 1 
10
30
70
100
'''

def calc(n):
    return 2*5*n

for i in range(int(input())):
    print(calc(int(input())))