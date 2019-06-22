# 100. Same Tree
class Solution:
   def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
       if p != None and q != None:
           if p.val != q.val:
               return False
           else:
               if (self.isSameTree(p.left, q.left)) != True:
                   return False
               elif self.isSameTree(p.right, q.right) != True:
                   return False
               return True
       else:
           if p == None and q == None:
               return True
           else:
               return False
       return True