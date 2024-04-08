
#https://leetcode.com/problems/validate-binary-search-tree/editorial/
#time: O(n)
#space: O(n)
#RECURSIVE inorder traversal
def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def inorder(node):
            if node is None:
                return True
            if not inorder(node.left):
                return False
            
            if node.val <= self.prev:
                return False 
            self.prev = node.val
            return inorder(node.right)        
        
        self.prev = -math.inf
        return inorder
