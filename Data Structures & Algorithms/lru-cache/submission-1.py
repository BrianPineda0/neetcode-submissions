class Node:
    def __init__(self, key, val):

        self.val = val
        self.key = key

        self.prev = self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}

        self.head = Node(0,0)
        self.tail = Node(0,0)

        self.head.next = self.tail
        self.tail.prev = self.head

    def insert(self, node):
        # [prev] <-> [node] <-> [tail]
        prev = self.tail.prev
        prev.next = node
        self.tail.prev = node
        node.prev = prev
        node.next = self.tail
        
    def delete(self, node):
        #[prev] <--> [next]

        prev = node.prev
        next = node.next

        prev.next = next
        next.prev = prev


    def get(self, key: int) -> int:

        if key in self.cache:
            self.delete(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val

        else: return -1

    def put(self, key: int, value: int) -> None:

        if key in self.cache:
            self.cache[key].val = value
            self.delete(self.cache[key])
            self.insert(self.cache[key])
        else:
            node = Node(key,value)
            self.insert(node)
            self.cache[key] = node

        if len(self.cache) > self.capacity:
            toDel = self.head.next 
            self.delete(toDel)
            del self.cache[toDel.key]



