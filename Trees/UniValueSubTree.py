#Given the root of a binary tree, return the number of uni-value 
# subtrees
# A uni-value subtree means all nodes of the subtree have the same value.
#Input: root = [5,1,5,5,5,null,5]
#Output: 4
 


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countUnivalSubtrees(self, root: Optional[TreeNode]) -> int:
        self.vount =0
        def dfs(node):
            if node is None:
                return True
            
            isLeft = dfs(node.left)
            isRight = dfs(node.right)

            if isLeft and isRight:
                if node.left and node.val != node.left.val:
                    return False
                if node.right and node.val != node.right.val:
                    return False
                self.vount +=1
                return True
            return False
        
        dfs(root)
        return self.vount
        
