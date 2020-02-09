# 112. Path Sum

class Solution:
    exist = False
    totalSum = 0

    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        self.totalSum = sum
        if root is None:
            return False
        else:
            nowSum = 0
            self.checkSum(root, nowSum)
            return self.exist

    def checkSum(self, root: TreeNode, nowSum: int):
        if root is not None:
            left = root.left is None
            right = root.right is None
            nowSum += root.val
            if left and right:
                if nowSum == self.totalSum:
                    self.exist = True
            self.checkSum(root.left, nowSum)
            self.checkSum(root.right, nowSum)