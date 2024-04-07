
#time: O(n) - n nodes
#space o(n) - height n nodes in recursive stack

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        #RECURSIVE APPROACH
        parent = root.val
        pVal = p.val
        qVal = q.val

        if pVal > parent and qVal > parent:
            return self.lowestCommonAncestor(root.right, p, q)
        elif pVal < parent and qVal < parent:
            return self.lowestCommonAncestor(root.left, p,q)
        
        else:
            return root
        
