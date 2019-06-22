# 101. Symmetric Tree
class Solution:
   left, right = [], []
   def isSymmetric(self, root: TreeNode) -> bool:
       self.left = []
       self.right = []
       if not root:
           return True
       self.in_order(root)
       self.post_order(root)
       print(self.left)
       print(self.right)
       if self.left == self.right:
           return True
       else:
           return False
   def in_order(self, root: TreeNode):
       if root is None:
           self.left.append("null")
       else:
           self.in_order(root.left)
           self.in_order(root.right)
           self.left.append(root.val)
   def post_order(self, root: TreeNode):
       if root is None:
           self.right.append("null")
       else:
           self.post_order(root.right)
           self.post_order(root.left)
           self.right.append(root.val)