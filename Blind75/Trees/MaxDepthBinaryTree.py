#time: O(n)
#space: O(n)

#https://leetcode.com/problems/maximum-depth-of-binary-tree/editorial/


#ITERATIVE BFS ----------------------
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0 
        levels = 0
        queue = collections.deque([root])
        while queue:
           # print(queue)
            for i in range(len(queue)):
                curr = queue.popleft()
        
                if curr.left:
                    queue.append(curr.left)

                if curr.right:
                    queue.append(curr.right)
            levels+=1
        return levels


#time: O(n)
#space: O(h)

#RECURSION

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0 

        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)

        return max(left,right) +1 
