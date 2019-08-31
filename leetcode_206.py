# 206. Reverse Linked List

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        temp = head
        stack = []
        while True:
            if temp is None:
                break
            else:
                stack.append(temp.val)
            temp = temp.next
        stack.reverse()
        if len(stack) == 0:
            return
        head = ListNode(stack[0])
        stack.pop(0)
        temp = head
        while True:
            if temp is None:
                break
            else:
                if len(stack) == 0:
                    break
                sample = ListNode(stack[0])
                temp.next = sample
                stack.pop(0)
                temp = sample
        return head
