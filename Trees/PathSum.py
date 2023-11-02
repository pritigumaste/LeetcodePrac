#https://leetcode.com/problems/path-sum/description/
class Solution:

 # DFS using Recussive
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        if not root:
            return 0
        def check(root,subpathsum,target):
            if not root:
                return 0
            if root.left == None and root.right == None:
                if subpathsum == target:
                    self.flag = True
            if root.left:
                check(root.left,subpathsum+root.left.val,target)
            if root.right:
                check(root.right,subpathsum+root.right.val,target)
        self.flag =False
        check(root,root.val,targetSum)
        return self.flag
