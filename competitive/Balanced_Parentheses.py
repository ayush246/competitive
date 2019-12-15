# https://www.hackerearth.com/practice/data-structures/stacks/basics-of-stacks/practice-problems/algorithm/little-monk-and-balanced-parentheses/description/

N=int(input())
l=input()
l=l.split()
c=0
x=0
while x<len(l):
    flag=0
    if int(l[x])<0:
        if l[x]=="-"+l[x-1]:
            c+=2
            l.remove(l[x-1])
            l.remove(l[x-1])
            flag=1
    x+=1
    if flag==1:
        x=0
print (c)
                