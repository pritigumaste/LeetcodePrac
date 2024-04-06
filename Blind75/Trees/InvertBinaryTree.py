#https://leetcode.com/problems/invert-binary-tree/editorial/

#time: O(n) - n number of nodes, you visit all nodes atleast once
#space: O(h) - stack trace of all the nodes, at max height is h 


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return None 
       #inverting meaning we are exchanging the nodes 
        temp = root.left
        root.left = root.right
        root.right = temp

        #recursive calls to do the same for all the nodes
        self.invertTree(root.left)
        self.invertTree(root.right)

        return root
