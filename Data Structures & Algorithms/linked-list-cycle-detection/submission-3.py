# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        curr1 = head
        curr2 = head
        
        while curr1 and curr2:
            curr1 = curr1.next
            curr2 = curr2.next

            if curr2 is None:
                break
            else:
                curr2 = curr2.next

            if curr1 == curr2:
                return True

        return False