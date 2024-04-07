#https://leetcode.com/problems/subtree-of-another-tree/editorial/

#time: O(mn) - n num of nodes in initial tree, m in the subtree
# space: O(m+n) - n recrusive calls to the node and m for the subtree- recursion stack

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # if root is None or subRoot == None:
        #     return False 

        def checkRoot(node):
            if node == None:
                return False
            
            elif check(node, subRoot):
                return True
            
            return checkRoot(node.left) or checkRoot(node.right)

        def check( p, q):
            if p is None or q is None:
                return p is None and q is None
            # if p is None and q is None:
            #     return None
            return p.val == q.val and check(p.left, q.left) and check(p.right, q.right)
        
        # if root.left.val == subRoot.val:
        #     check(root.left, subRoot)
        # elif root.right.val == subRoot.val:
        #     check(root.right, subRoot)
        
        return checkRoot(root)
