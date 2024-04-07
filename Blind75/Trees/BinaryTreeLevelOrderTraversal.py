#https://leetcode.com/problems/binary-tree-level-order-traversal/editorial/

#time:O(n) 
#space: O(n) 
#iterative

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result =[]
        level = 0
        if root is None:
            return []
        
        # if len(root) ==1:
        #     return root

        queue= collections.deque([root])
        while queue:
            result.append([])
            l = len(queue)
            for i in range(l):
                node = queue.popleft()

                result[level].append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            level +=1

            
        return result     
