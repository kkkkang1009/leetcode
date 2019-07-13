# 107. Binary Tree Level Order Traversal II

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        result = []
        if root is None:
            return result
        stack = [root]
        while stack:
            nowDepth = []
            nowStack = []
            length = len(stack)
            for index in range(0, length):
                if stack[index].left is not None:
                    nowStack.append(stack[index].left)
                if stack[index].right is not None:
                    nowStack.append(stack[index].right)
                nowDepth.append(stack[index].val)
            result.insert(0, nowDepth)
            stack = nowStack
        return result