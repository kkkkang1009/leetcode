# 104. Maximum Depth of Binary Tree

class Solution:
    maxDep = 0
    def maxDepth(self, root: TreeNode) -> int:
        nowDepth = 0
        if not root:
            return self.maxDep
        self.checkDepth(root, nowDepth)
        return self.maxDep

    def checkDepth(self, root: TreeNode, nowDepth: int):
        if root is not None:
            print(self.maxDep)
            nowDepth += 1
            if self.maxDep < nowDepth:
                self.maxDep = nowDepth
            self.checkDepth(root.left, nowDepth)
            self.checkDepth(root.right, nowDepth)