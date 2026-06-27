class Node:
    def __init__(self ,key = 0, val = 0):
        self.key = key
        self.val = val 
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.head = Node()
        self.tail = Node()

        self.head.next = self.tail
        self.tail.prev = self.head


    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        

        node = self.cache[key]
        self.remove(node)
        self._insert_at_head(node)
        return node.val


    def remove(self ,node):
        p, n = node.prev, node.next
        p.next = n
        n.prev = p

    def _insert_at_head(self , node):
        first_node = self.head.next
        self.head.next = node
        node.prev = self.head
        node.next = first_node
        first_node.prev = node
        

    def put(self, key: int, value: int) -> None:
        
        if key in self.cache:
            node = self.cache[key]
            node.val = value

            self.remove(node)
            self._insert_at_head(node)
        else:
            new_node = Node(key , value)
            self.cache[key] = new_node
            self._insert_at_head(new_node)

        if len(self.cache) > self.capacity:

            lru_node = self.tail.prev
            del self.cache[lru_node.key]
            self.remove(lru_node)


        
