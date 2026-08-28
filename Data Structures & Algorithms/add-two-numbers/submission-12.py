# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        first = l1
        second = l2

        start1 = first
        start2 = second

        prev1 = None
        prev2 = None

        while first or second:

            if first:
                temp1 = first.next
                first.next = prev1
                prev1 = first
                first = temp1

            if second:
                temp2 = second.next
                second.next = prev2
                prev2 = second
                second = temp2


        first = prev1
        second = prev2

        list1 = []
        list2 = []

        while first or second:

            if first:
                list1.append(first.val)
                first = first.next 

            if second:
                list2.append(second.val)
                second = second.next

        num1 = 0
        num2 = 0

        length = None

        if len(list1) < len(list2):
            length = list2
        else:
            length = list1

        for i in range(len(length)):
            
            if i < len(list1):
                num1 = num1 * 10 + list1[i]
            if i < len(list2):
                num2 = num2 * 10 + list2[i]

        answerNum = num1+num2

        head = ListNode(None,None)

        answer = head

        print(num1)
        print(num2)

        print(answerNum)

        if answerNum == 0 : return ListNode(0,None)

        while answerNum > 0:

            answer.val = answerNum % 10

            if answerNum // 10 > 0:
                answer.next = ListNode(None,None)

            answer = answer.next

            answerNum = answerNum // 10

        return head



