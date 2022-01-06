class LRUCache:
    
    class DoubleLinkNode:
        def __init__(self, key:int, val:int, ans=None, des=None):
            self.key = key
            self.val = val
            self.ans = ans
            self.des = des
    
    class DoubleLinkList:
        def __init__(self, cap:int):
            self.cap = cap
            self.size = 0
            self.head = None
            self.tail = None
        
        def append(self, node):
            self.size += 1
            if self.head is None:
                self.head = self.tail = node
            else:
                self.tail.des = node
                node.ans = self.tail
                self.tail = node
            
        def remove(self, node):
            self.size -= 1
            if node == self.head:
                if node.des:
                    node.des.ans = None
                self.head = node.des
            elif node == self.tail:
                if node.ans:
                    node.ans.des = None
                self.tail = node.ans
            else:
                node.ans.des = node.des
                node.des.ans = node.ans
        
    def __init__(self, capacity: int):
        self.cap = capacity
        self.where = {}
        self.cache = self.DoubleLinkList(self.cap)

    def get(self, key: int) -> int:
        if key not in self.where:
            return -1
        node = self.where[key]
        self.cache.remove(node)
        self.cache.append(node)
        
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.where:
            node = self.where[key]
            node.val = value
            self.cache.remove(node)
            self.cache.append(node)
        else:
            if self.cap == self.cache.size:
                self.where.pop(self.cache.head.key)
                self.cache.remove(self.cache.head)
            new_node = self.DoubleLinkNode(key, value)
            self.where[key] = new_node
            self.cache.append(new_node)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)