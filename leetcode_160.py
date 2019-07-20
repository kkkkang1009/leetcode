# 160. Intersection of Two Linked Lists
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        if not headA or not headB:
            return None
        lenA, lenB = 0, 0
        nodeA, nodeB = headA, headB
        while nodeA:
            lenA += 1
            nodeA = nodeA.next
        while nodeB:
            lenB += 1
            nodeB = nodeB.next
        nodeA = headA if lenA >= lenB else headB
        nodeB = headB if lenA >= lenB else headA
        length = lenA - lenB if lenA >= lenB else lenB - lenA
        for i in range(length):
            nodeA = nodeA.next
        while True:
            if nodeA == nodeB:
                return nodeA
            nodeA = nodeA.next
            nodeB = nodeB.next
        return None

# 1st - Time Limit Exceeded
# def getIntersectionNode(self, headA, headB):
#     if headA is None or headB is None:
#         return None
#     tempA = headA
#     tempB = headB
#     while True:
#         if tempA is None:
#             return None
#         tempB = headB
#         while True:
#             if tempB is None:
#                 break
#             if tempA is tempB:
#                 return tempA
#             else:
#                 tempB = tempB.next
#         tempA = tempA.next
#     return None

# 2st - Time Limit Exceeded
# def getIntersectionNode(self, headA, headB):
#     """
#     :type head1, head1: ListNode
#     :rtype: ListNode
#     """
#     if not headA or not headB:
#         return None
#
#     lenA = 0
#     lenB = 0
#     nodeA = headA
#     nodeB = headB
#
#     while nodeA:
#         lenA += 1
#         nodeA = nodeA.next
#     while nodeB:
#         lenB += 1
#         nodeB = nodeB.next
#
#     listNode = []
#     nodeL = headA if lenA >= lenB else headB
#     nodeS = headB if lenA >= lenB else headA
#
#     while nodeL:
#         listNode.append(nodeL)
#         nodeL = nodeL.next
#
#     for i in range(len(listNode)):
#         if not nodeS:
#             return None
#         if listNode.count(nodeS):
#             return nodeS
#         nodeS = nodeS.next
#
#     return None