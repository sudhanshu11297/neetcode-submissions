class Node:
    def __init__(self,key,value):
        self.key = key
        self.value = value
        self.next= None
        self.prev = None

class LRUCache:

    def __init__(self,capacity):
        self.capacity = capacity
        self.cache = {}
        self.head = Node(0,0)
        self.tail = Node(0,0)

        #creat a dummy node
        self.head.next = self.tail
        self.tail.prev = self.head

    def insert(self,node):
        next_node = self.head.next
        self.head.next = node
        node.prev = self.head

        node.next = next_node
        next_node.prev = node
    
    def remove(self,node):
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node
        
    def get(self,key):
        if key not in self.cache:
            return -1
        else:
            node = self.cache[key]
            self.remove(node)
            self.insert(node)

            return node.value
    def put(self,key,value):        
            if key in self.cache:
               self.remove(self.cache[key])
            node = Node(key,value)
            self.cache[key] = node
            self.insert(node)

            if len(self.cache) > self.capacity:
                lru = self.tail.prev
                self.remove(lru)
                del self.cache[lru.key]


