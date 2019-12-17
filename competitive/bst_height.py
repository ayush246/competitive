# https://www.hackerearth.com/practice/data-structures/trees/binary-search-tree/practice-problems/algorithm/monk-watching-fight/

class Node: 
    def __init__(self,key): 
        self.left = None
        self.right = None
        self.val = key 
def insert(root,node): 
    if root is None: 
        root = node 
    else: 
        if root.val < node.val: 
            if root.right is None: 
                root.right = node 
            else: 
                insert(root.right, node) 
        else: 
            if root.left is None: 
                root.left = node 
            else: 
                insert(root.left, node) 
n=int(input())
l=[int(x) for x in input().split()]
r = Node(l[0])
for x in range(1,n): 
    insert(r,Node(l[x])) 
def maxDepth(node): 
    if node is None: 
        return 0  
    else : 
        lDepth = maxDepth(node.left) 
        rDepth = maxDepth(node.right) 
        if (lDepth > rDepth): 
            return lDepth+1
        else: 
            return rDepth+1
print (maxDepth(r))