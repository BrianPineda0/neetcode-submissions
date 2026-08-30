# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        newList = head
        curr = head
        count = 0

        while curr:
            count +=1
            curr = curr.next

        byKs = count // k
        dummy = ListNode(0, None)
        answer = dummy

        while byKs > 0: 
        
            reversedList, tail, newList = self.reverseList(newList,k)
            dummy.next = reversedList
            dummy = tail
            byKs -= 1

        dummy.next = newList

        return answer.next
    

    def reverseList(self, head, k):

        count = k
        curr = head
        prev = None

        while count > 0 :

            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
            count -= 1

        return prev, head, curr



            



