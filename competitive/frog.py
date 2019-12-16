# https://www.hackerearth.com/practice/algorithms/searching/linear-search/practice-problems/algorithm/counting-frog-paths-1abd84d5/description/

l=[int(x) for x in input().split()]
x=l[0]
y=l[1]
s=l[2]
T=l[3]
o1=0
o2=0
p=0
for i in range(T+1):
    for j in range(T+1):
        if (x <= o1+i <= x+s) and (y <= o2+j <= y+s) and ((o1+i)+(o2+j)<=T):
            p+=1
print (p)