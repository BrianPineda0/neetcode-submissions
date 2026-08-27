# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        if not head.next:
            return

        count = 0
        curr = head

        while curr:
            curr = curr.next
            count +=1

        half = count // 2

        n = 0

        prev = None

        list1 = head
        list2 = None

        curr = head

        while curr and n < half:

            prev = curr
            list2 = curr.next
            curr = curr.next
            n +=1

        prev.next = None

        curr = list2
        prev = None

        while curr:
            temp = curr.next
            curr.next = None

            if prev: curr.next = prev

            prev = curr 
            curr = temp

        list2 = prev

        ccount = 0

        head = list1

        answer = None

        first, second = list1, list2

        while second:

            if not first.next:
                first.next = second.next

            tmp1 = first.next
            tmp2 = second.next
            first.next = second
            second.next = tmp1
            first = tmp1
            second = tmp2


