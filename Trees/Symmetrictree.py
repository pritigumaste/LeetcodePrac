
#https://leetcode.com/problems/symmetric-tree/solutions/3290155/day-72-with-diagram-iterative-and-recursive-easiest-beginner-friendly-sol/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    
    def check(self,  node1,  node2):
        #recursion
        if(node1 is None and node2 is not None or node2 is None and node1 is not None):
           # print("first IF")
            return False
        if(node1 is None and node2 is None):
            #print("secbd if")
            return True
        else:
            #print("third else")
            return node1.val == node2.val and self.check(node1.left, node2.right) and self.check(node1.right , node2.left)
        return False
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
     
        return self.check(root, root)
    
        
        
        
