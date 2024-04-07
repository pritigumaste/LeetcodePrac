#https://leetcode.com/problems/same-tree/
#time: O(n) 
#space: o(n) - stack recursion

#recursive
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        if p == None and q == None:
            return True

        if p == None or q == None:
            return False 
        
        if p.val != q.val:
            return False


        return self.isSameTree(p.right, q.right)and self.isSameTree(p.left, q.left)
        
#Iterative
#time: O(n) 
#space: o(n) - queue

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        def isSame(p,q):
            if p == None and q == None:
                return True

            if p == None or q == None:
                return False 
        
            if p.val != q.val:
                return False
            return True
        
        queue = collections.deque([(p,q)])
        while queue:
            p,q = queue.popleft()

            if not isSame(p,q):
                return False
            
            if p:
                queue.append((p.left, q.left))
                queue.append((p.right, q.right))


        return True
