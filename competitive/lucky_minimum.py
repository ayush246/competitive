"""
Monk just purchased an array A having N integers. Monk is very superstitious. He calls the array A Lucky if the frequency of
the minimum element is odd, otherwise he considers it Unlucky. Help Monk in finding out if the array is Lucky or not.

Input:
First line consists of a single integer T denoting the number of test cases.
First line of each test case consists of a single integer N denoting the size of array A.
Second line of each test case consists of N space separated integers denoting the array A.

Output:
For each test case, print "Lucky" (without quotes) if frequency of minimum element is odd, otherwise print "Unlucky"
(without quotes). Print a new line after each test case.

SAMPLE INPUT 
2
5
8 8 9 5 9
5
3 3 3 5 3
SAMPLE OUTPUT 
Lucky
Unlucky
Explanation
In first case, value of minimum element is 5 and it's frequency is 1 which is odd, so the array is Lucky.
In second case, value of minimum element is 3 and it's frequency is 4 which is even, so the array is Unlucky.
"""

t=int(input())
for x in range (0,t):
    N=int(input())
    l=input()
    l=l.split()
    d={}
    for x in range(0,N):
        d[int(l[x])]=0
    for x in range(0,N):
        d[int(l[x])]+=1
    if d[min(d)] % 2 != 0:
        print ("Lucky")
    else:
        print ("Unlucky")
        
