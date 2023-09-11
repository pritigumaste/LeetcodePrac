#Time: o(nlogn)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    #check if its height balanced, traverse to last node
    #if height balanced then check left node is balanced then check for right node 
    #compare sub trees then perform recursion 
    

    def height(self, root:TreeNode) -> int:
        if not root:
            return -1
        return 1 + max(self.height(root.left), self.height(root.right))

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True

        return abs(self.height(root.left) - self.height(root.right)) < 2 and self.isBalanced(root.left) and self.isBalanced(root.right)
            
