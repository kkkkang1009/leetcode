# 203. Remove Linked List Elements
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        while True:
            if head is None:
                return None
            else:
                if head.val == val:
                    head = head.next
                else:
                    break
        now = head
        while True:
            if now is None:
                break
            temp = now.next
            if temp is None:
                break
            if temp.val == val:
                now.next = temp.next
            else:
                now = temp
        return head