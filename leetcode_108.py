# 108. Convert Sorted Array to Binary Search Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if not nums:
            return None
        elif len(nums) == 1:
            root = TreeNode(nums[0])
            return root
        elif len(nums) == 2:
            root = TreeNode(nums[1])
            root.left = TreeNode(nums[0])
            return root
        elif len(nums) == 3:
            root = TreeNode(nums[1])
            root.left = TreeNode(nums[0])
            root.right = TreeNode(nums[2])
            return root
        else:
            mid = int(len(nums)/2)
            root = TreeNode(nums[mid])
            root.left = self.sortedArrayToBST(nums[0:mid])
            root.right = self.sortedArrayToBST(nums[mid+1:len(nums)])
        return root