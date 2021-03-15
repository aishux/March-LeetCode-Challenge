# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: ListNode, k: int) -> ListNode:
        # record for first kth node, last kth node, and running cursor
        first_k, last_k, cur = None, None, head
        
        
        # Step #1: locate first_k to corresponding position
        for _ in range(k-1):
            cur = cur.next
        
        first_k = cur
        
        
        # Step #2: locate last_k to corresponding position
        last_k, cur = head, cur.next
        
        while cur:
            cur, last_k = cur.next, last_k.next
        
        # Step #3: swap value between first kth node and last kth node
        first_k.val, last_k.val = last_k.val, first_k.val
        
        return head
