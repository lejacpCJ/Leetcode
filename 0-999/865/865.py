# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional

class Solution:
    def subtreeWithAllDeepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(node):
            if not node:
                return None, 0
            l_node, l_dist = dfs(node.left)
            r_node, r_dist = dfs(node.right)

            if l_dist > r_dist:
                return l_node, l_dist + 1
            if r_dist > l_dist:
                return r_node, r_dist + 1
            return node, l_dist + 1

        result_node, _ = dfs(root)
        return result_node