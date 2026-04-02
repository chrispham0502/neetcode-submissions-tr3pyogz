# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        first = second = head

        while first and first.next and second.next and second.next.next:
            first = first.next
            second = second.next.next
            if first.val == second.val:
                return True

        return False