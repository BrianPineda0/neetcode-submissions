"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        if not head:
            return None

        hashtable = {}

        curr = head

        new = Node(0, None, None)

        answer = new

        hashtable = {}

        while curr:

            new.val = curr.val

            if curr.next:
                new.next = Node(0, None, None)

            hashtable[curr] = new

            new = new.next

            curr = curr.next

        curr2 = answer

        curr = head

        while curr2 and curr:

            if curr.random:
                curr2.random = hashtable[curr.random]
            else: curr2.random = None

            curr2 = curr2.next
            curr = curr.next

        return answer
        