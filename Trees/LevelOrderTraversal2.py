# https://leetcode.com/problems/binary-tree-level-order-traversal-ii/
#we don't need to necessarily find the height of the tree. we can do normal 
#pre order level order traversal and then just return the reverse of that list 

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:

        #we don't need to necessarily find the height of the tree. we can do normal 
#pre order level order traversal and then just return the reverse of that list 
        # self.leftLen =0
        # self.rightLen =0
        # def check(node):

        #     if node is None:
        #         return 
        #     if node.left:
        #         self.leftLen +=1
        #     if node.right:
        #         self.rightLen +=1

        #     self.leftLen = check(node.left)
        #     self.rightLen = check(node.right)
        #     return max(self.rightLen, self.leftLen) +1
        
        # height = check(root)
        # print(height)
        # return [[]]

        levels =[]

        def check(node, level):
            if node is None:
                return 
            
            if len(levels) == level:
                levels.append([])
            levels[level].append(node.val)
            if node.left:
                check(node.left, level+1)
            if node.right:
                check(node.right, level+1)

        
        check(root, 0)
        return levels[::-1]

  #time compl and space = O(n)
