# 111. Minimum Depth of Binary Tree

class Solution:
    minDep = 10000

    def minDepth(self, root: TreeNode) -> int:
        nowDepth = 0
        if not root:
            return nowDepth
        self.checkDepth(root, nowDepth)
        return self.minDep

    def checkDepth(self, root: TreeNode, nowDepth: int):
        if root is not None:
            left = root.left is None
            right = root.right is None
            nowDepth += 1
            if left and right:
                if self.minDep > nowDepth:
                    self.minDep = nowDepth
            self.checkDepth(root.left, nowDepth)
            self.checkDepth(root.right, nowDepth)