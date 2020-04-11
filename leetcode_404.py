# 404. Sum of Left Leaves

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        total = 0

        if root == None:
            return total

        if root.left != None:
            if root.left.left == None and root.left.right == None:
                total += root.left.val
            else:
                total += self.sumOfLeftLeaves(root.left)

        if root.right != None:
            total += self.sumOfLeftLeaves(root.right)

        return total