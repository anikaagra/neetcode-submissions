class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dic = {}
        self.left, self.right = Node(0,0), Node(0,0)
        self.left.next, self.right.prev = self.right, self.left

    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev
    
    def insert(self, node):
        prev, nxt = self.right.prev, self.right
        prev.next = node
        nxt.prev = node
        node.next = nxt
        node.prev = prev

    def get(self, key: int) -> int:
        if key in self.dic:
            self.remove(self.dic[key])
            self.insert(self.dic[key])
            return self.dic[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.dic:
            self.remove(self.dic[key])
        self.dic[key] = Node(key, value)
        self.insert(self.dic[key])

        if len(self.dic) > self.capacity:
            lru = self.left.next
            self.remove(lru)
            del self.dic[lru.key]