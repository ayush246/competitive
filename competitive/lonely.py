# https://www.hackerearth.com/practice/basic-programming/implementation/basics-of-implementation/practice-problems/algorithm/lonely-monk-code-monk/

N=int(input())
a=[int(x) for x in input().split()]
temp = [1,0]
result = 0
s= 0
for i in range(N):
    s = ((s+a[i])%2 + 2)%2
    temp[s]+= 1
result+= int(temp[0]*(temp[0]-1)/2) + int(temp[1]*(temp[1]-1)/2)
print(result)