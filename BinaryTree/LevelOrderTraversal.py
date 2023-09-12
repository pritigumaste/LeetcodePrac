#BFS
#Time comp: o(n) - as each node is visited only once
#space: o(n) as we are using list 
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:\

        levels =[]
        if not root:
            return []
        
        def helper(node, level):
            #if new level add a empty list of lists
            if len(levels) ==level:
                levels.append([])
            #add curr value to that level index in lists of lists
            levels[level].append(node.val)        
            #traverse left and roght nodes
            if node.left:
                helper(node.left, level+1)
            if node.right:
                helper(node.right, level+1)
        
        helper(root, 0)
        return levels
