# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        if not lists or len(lists) == 0:
            return None

        while len(lists) > 1:

            mergedlist = []

            for i in range(0, len(lists), 2):
                list1 = lists[i]
                list2 = lists[i+1] if i+1 < len(lists) else None

                mergedlist.append(self.mergeList(list1, list2))

            lists = mergedlist
        
        return lists[0]


    

    def mergeList(self, l1 , l2):

        if not l1: return l2
        if not l2: return l1

        head = ListNode(0, None)

        answer = head

        currA = l1

        currB = l2

        while currA and currB:

            if currA.val < currB.val:
                answer.next = currA
                currA = currA.next
            
            else:
                answer.next = currB
                currB = currB.next

            answer = answer.next

        if currA:
            answer.next = currA
        if currB:
            answer.next = currB

        
        return head.next

  


