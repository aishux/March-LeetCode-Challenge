# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        
        if not headA or not headB:
            return None
        
        dct = {}
        
        while headA:
            dct[headA] = 1
            headA = headA.next
        
        while headB:
            if headB in dct:
                return headB
            headB = headB.next
