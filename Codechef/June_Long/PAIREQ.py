'''
Make all equal using Pairs Problem Code: PAIREQ
Add problem to Todo list
Submit
Chef has an array A of length N.

In one operation, Chef can choose any two distinct indices i,j (1≤i,j≤N,i≠j) and either change Ai to Aj or change Aj to Ai.

Find the minimum number of operations required to make all the elements of the array equal.

Input Format
First line will contain T, number of test cases. Then the test cases follow.
First line of each test case consists of an integer N - denoting the size of array A.
Second line of each test case consists of N space-separated integers A1,A2,…,AN - denoting the array A.
Output Format
For each test case, output the minimum number of operations required to make all the elements equal.

Constraints
1≤T≤100
2≤N≤1000
1≤Ai≤1000
Sample Input 1 
4
3
1 2 3
4
5 5 5 5
4
2 2 1 1
3
1 1 2
Sample Output 1 
2
0
2
1
'''

def calc(l):
    m=0
    for i in l:
        if(l.count(i)>m):
            m=l.count(i)
    return len(l)-m


for i in range(int(input())):
    n=int(input())
    x=list(map(int, input().split()))
    print(calc(x))