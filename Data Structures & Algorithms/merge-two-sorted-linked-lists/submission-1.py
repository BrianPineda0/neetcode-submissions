# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        if not list1: return list2
        if not list2: return list1

        Acurr = list1
        Bcurr = list2

        head = None

        answer = None

        while Acurr and Bcurr:

            if Acurr.val <= Bcurr.val:
                if not head:
                    head = Acurr
                    answer = head
                else:
                    answer.next = Acurr
                    answer = answer.next
                Acurr = Acurr.next
            else:
                if not head:
                    head = Bcurr
                    answer = head
                else:
                    answer.next = Bcurr
                    answer = answer.next
                Bcurr = Bcurr.next

        if Acurr:
            answer.next = Acurr
        elif Bcurr:
            answer.next = Bcurr
            
        return head
            
