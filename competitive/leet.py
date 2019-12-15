# https://leetcode.com/problems/jewels-and-stones/

class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        c=0
        for x in range(len(J)):
            for y in range(len(S)):
                if J[x]==S[y]:
                    c+=1
        return c

# https://leetcode.com/problems/sort-array-by-parity-ii/

class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        even, odd = 0, 1
        while even < len(A) and odd < len(A):
            if A[even] % 2 == 0: even += 2
            elif A[odd] % 2 == 1: odd += 2
            else: A[even], A[odd] = A[odd], A[even]
        return A
    
# https://leetcode.com/problems/sort-array-by-parity/

class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        l=[]
        l2=[]
        for x in A:
            if x%2==0:
                l.append(x)
            else:
                l2.append(x)
        return (l+l2)

# https://leetcode.com/problems/robot-return-to-origin/

class Solution:
    def judgeCircle(self, moves: str) -> bool:
        c=0
        d=0
        for x in moves:
            if x=='U':
                c+=1
            elif x=='D':
                c-=1
            elif x=='L':
                d+=1
            else:
                d-=1
        if c==0 and d==0:
            return True
        else:
            return False

# https://leetcode.com/problems/self-dividing-numbers/

class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        l=[]
        for x in range(left,right+1):
            a=str(x)
            c=0
            for y in a:
                if y!='0':
                    if x%int(y)==0:
                        c+=1
            if c==len(a):
                l.append(x)
        return l
                  