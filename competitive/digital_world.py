# https://www.hackerearth.com/practice/basic-programming/implementation/basics-of-implementation/practice-problems/algorithm/monk-and-digital-world-code-monk/

N=int(input())
l=input()
l2=input()
l.split()
l2.split()
d={}
d2={}
for x in range(N):
    d[l[x]]=0
    d2[l2[x]]=0
for x in range(N):
    d[l[x]]+=1
    d2[l2[x]]+=1
flag=0
for x in d:
    if x in d2:
        if d[x]!=d2[x]:
            flag=1
    else:
        flag=1
if flag==0:
    print ("YES")
else:
    print ("NO")