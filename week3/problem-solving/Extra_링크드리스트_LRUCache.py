# 링크드리스트 - LRU Cache
# 문제 링크: https://leetcode.com/problems/lru-cache/description/?envType=study-plan-v2&envId=top-interview-150

class Node:
    def __init__(self, key: int, val: int, bit: int):
        self.key = key
        self.val = val
        self.bit = bit
        self.next: Node = None
        self.prev: Node = None
    def __lt__(self, other):
        return self.bit < other.bit

class DoubleLinkedList:
    def __init__(self):
        head = Node(None, None, None) # push
        tail = Node(None, None, None) # pop
        self.head = head
        self.tail = tail
        self.head.prev = tail
        self.tail.next = head
    def push(self, node: Node):
        prev = self.head.prev
        node.prev = prev
        node.next = self.head
        prev.next = node
        self.head.prev = node
    def pop(self, node: Node) -> Node:
        prev = node.prev
        next = node.next
        if prev:
            prev.next = next
        if next:
            next.prev = prev
        node.next = node.prev = None # can be omission
        return node
    def removeCumbersome(self):
        return self.pop(self.tail.next)

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.limit = capacity
        self.bit = 0
        self.dll = DoubleLinkedList()

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            node.bit = self.bit
            self.bit += 1
            self.dll.pop(node)
            self.dll.push(node)
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            node.bit = self.bit
            self.dll.pop(node)
            self.dll.push(node)
            pass
        else:
            new_node = Node(key, value, self.bit)
            if len(self.cache) == self.limit: # new cache
                deleted_node = self.dll.removeCumbersome()
                if deleted_node and deleted_node.key in self.cache: self.cache.pop(deleted_node.key)
            self.dll.push(new_node)
            self.cache[key] = new_node
        self.bit += 1


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

# lRUCache = LRUCache(2)
# lRUCache.put(1, 1)
# lRUCache.put(2, 2)
# print(lRUCache.get(1))
# lRUCache.put(3, 3)

# print(lRUCache.get(2))
# # print(lRUCache.cache)
# lRUCache.put(4, 4)
# print(lRUCache.get(1))
# print(lRUCache.get(3))
# print(lRUCache.get(4))
