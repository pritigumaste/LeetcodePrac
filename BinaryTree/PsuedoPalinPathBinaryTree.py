#Time: O(n) 
#space: O(h)

#https://leetcode.com/problems/pseudo-palindromic-paths-in-a-binary-tree/description/?envType=daily-question&envId=2024-01-24

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pseudoPalindromicPaths(self, root: TreeNode) -> int:
        def dfs(node, path_set):
            if node is None:
                return 0

            # Toggle the presence of node.val in the set
            if node.val in path_set:
                path_set.remove(node.val)
            else:
                path_set.add(node.val)

            # Leaf node: check if the path can form a pseudo-palindrome
            if node.left is None and node.right is None:
                return 1 if len(path_set) <= 1 else 0

            # Continue DFS traversal
            left_count = dfs(node.left, set(path_set))
            right_count = dfs(node.right, set(path_set))

            return left_count + right_count

        return dfs(root, set())
