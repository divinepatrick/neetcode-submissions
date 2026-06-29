# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None         # tracks the new tail
        current = head      # starts at the original head

        while current:
            next_node = current.next    # save the rest of the list
            current.next = prev         # reverse the pointer
            prev = current              # move prev forward
            current = next_node         # move current forward
        return prev