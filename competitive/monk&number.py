"""
https://www.hackerearth.com/problem/algorithm/monk-and-number/

"""
def divSum(n) : 
    result = 0
    for i in range(2,int((n**(1/2))+1)) : 
        if (n % i == 0) : 
            if (i == (n/i)) : 
                result = result + i 
            else : 
                result = result + (i + n//i) 
    return (result + n + 1) 
def findDivisors(n) : 
    i = 1
    l2=[]
    while i <= int((n**(1/2))): 
        if (n % i == 0) : 
            if (n / i == i) : 
                l2.append(int(i)) 
            else : 
                l2.append(int(i))
                l2.append(int(n/i))
        i = i + 1
    return (l2)
t=int(input())
for x in range(0,t):
    N=int(input())
    l=input()
    l=l.split()
    s=1
    f=0
    for x in l:
        s=s*int(x)
    for x in findDivisors(s):
        f+=divSum(x)
    print (f-1)