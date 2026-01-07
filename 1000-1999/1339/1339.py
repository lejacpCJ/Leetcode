# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional

class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        MOD = 10 ** 9 + 7
        self.max_subtree = 0

        # First pass: compute total sum of the tree
        def get_total(node):
            if not node:
                return 0
            return node.val + get_total(node.left) + get_total(node.right)

        total = get_total(root)

        # Second pass: try all possible splits
        def dfs(node):
            if not node:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            curr_sum = node.val + left + right
            # Update max product
            self.max_subtree = max(self.max_subtree, curr_sum * (total - curr_sum))
            return curr_sum

        dfs(root)
        return self.max_subtree % MOD