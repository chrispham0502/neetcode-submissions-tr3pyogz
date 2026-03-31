# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        curr = head
        prev = None

        # end when reach next = None
        while curr:

            # save the next node info
            tmp = curr.next

            # rewire current next to previous node
            curr.next = prev

            # update previous node to current node
            prev = curr

            # update current node to next node
            curr = tmp

        return prev
            