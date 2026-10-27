# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        best = float("-inf")

        def dfs(node):
            nonlocal best

            if not node:
                return 0

            left = max(dfs(node.left), 0)
            right = max(dfs(node.right), 0)

            path_sum = node.val + left + right

            best = max(best, path_sum)

            return node.val + max(left, right)

        dfs(root)

        return best