# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        if not head or not head.next or k == 0:
            return head 

        length = 1
        tail = head
        while tail and tail.next:
            tail = tail.next
            length += 1

        curr = head 
        for i in range(length - (k % length) - 1):
            curr = curr.next

        tail.next = head
        lastNode = curr.next
        curr.next = None
        return lastNode        