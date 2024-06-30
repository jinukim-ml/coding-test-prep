from collections import OrderedDict

class LRUCache: # using OrderedDict()
    def __init__(self, capacity: int):
        self.cache = OrderedDict()
        self.cap = capacity

    def get(self, key: int) -> int:
        if key in self.cache:
            self.cache.move_to_end(key) 
            return self.cache[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache.move_to_end(key) 
        elif len(self.cache) == self.cap:
            self.cache.popitem(last=False)
        self.cache[key] = value

# LL solution
class Node:
    def __init__(self, key, val) -> None:
        self.key, self.val = key, val
        self.prev, self.nxt = None, None

class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}
        self.head, self.tail = Node(0, 0), Node(0, 0)
        self.head.nxt, self.tail.prev = self.tail, self.head

    def remove(self, node: Node) -> None:
        prev, nxt = node.prev, node.nxt
        prev.nxt, nxt.prev = nxt, prev
        return

    def insert(self, node: Node) -> None:
        prev, nxt = self.tail.prev, self.tail
        prev.nxt = nxt.prev = node
        node.nxt, node.prev = nxt, prev
        return

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.cap:
            target = self.head.nxt
            self.remove(target)
            self.cache.pop(target.key)