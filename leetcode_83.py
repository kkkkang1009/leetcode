# 83. Remove Duplicates from Sorted List

class Solution:
   def deleteDuplicates(self, head: 'ListNode') -> 'ListNode':
       if head == None or head.next == None:
           return head
       else:
           nowNode = head
           nextNode = head.next
       while True:
           if nowNode.val == nextNode.val:
               if nextNode.next != None:
                   nextNode = nextNode.next
                   nowNode.next = nextNode
               else:
                   nowNode.next = None
                   break
           else:
               if nextNode.next != None:
                   nowNode = nextNode
                   nextNode = nextNode.next
               else:
                   break
       return head