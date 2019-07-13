# 110. Balanced Binary Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    balanced = True

    def isBalanced(self, root: TreeNode) -> bool:
        self.checkDepth(root, 0)
        return self.balanced

    def checkDepth(self, root: TreeNode, depth: int):
        if root is None:
            return None
        left = self.checkDepth(root.left, depth + 1) if root.left else depth
        right = self.checkDepth(root.right, depth + 1) if root.right else depth
        if abs(left - right) > 1:
            self.balanced = False
        return max(left, right)

