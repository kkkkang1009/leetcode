# 141. Linked List Cycle
class Solution(object):
    def hasCycle(self, head):
        stack = []
        temp = head
        if temp is None:
            return False
        while True:
            if temp in stack:
                return True
            else:
                stack.append(temp)
                if temp.next is None:
                    return False
                temp = temp.next