# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head

        if not head.next and n == 1:
            return None


        prev = None

        flag = 0

        while curr:

            count = 0

            sec = curr

            while sec and count < n:

                print (curr.val)

                if not sec.next:

                    if not prev:
                        head = curr.next
                        flag = 1
                        break

                    prev.next = curr.next
                    flag = 1
                    break

                    

                    

                sec = sec.next
                count +=1

            prev = curr
            curr = curr.next

            if flag: break

        return head