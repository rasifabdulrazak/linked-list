class Node:
    def __init__(self, value,next=None):
        self.val = value
        self.next = next
        
        
A = Node(1)
B = Node(2)
C = Node(3)
D = Node(4)

A.next = B
B.next = C
C.next = D

class LinkdeList:
    def __init__(self,head=None):
        self.head = head
        
    def insert_at_begining(self,val):
        # create a new node
        new_node = Node(val)
        # new node point to head
        new_node.next = self.head
        # make new node as head
        self.head = new_node
        pass
    
    def insert_at_end(self,val):
        # create a new node
        new_node = Node(val)
        # if no head or val in linklist make new node as head
        if not self.head: 
            self.head = new_node 
            return
        # get the last node
        curr = self.head
        while curr.next:
            curr = curr.next 
        # point last node next to newnode
        curr.next = new_node
        pass
    
    def insert_at_position(self,index,val):
        # if index not exist return out of box
        if index < 0: raise IndexError("Not found")
        if index == 0: return self.insert_at_begining(val)
        curr = self.head
        for _ in range(index-1):
            if not curr:
                raise IndexError("Not found")
            curr = curr.next
        new_node = Node(val,curr.next)
        curr.next = new_node
        
    def delete_at_end(self):
        if not self.head: return
        if not self.head.next:
            self.head = None
        curr = self.head
        previous = None
        while curr.next:
            previous = curr
            curr = curr.next
        previous.next = None
        
    def delete_by_value(self,value):
        pass
        
    def print_list(self):
        curr = self.head
        while curr:
            print(curr.val, end=" -> ")
            curr = curr.next
        print("None")
        
# 1->2->3->4->None
linklist = LinkdeList(A)

# 5->1->2->3->4->None
linklist.insert_at_begining(5)

# 5->1->2->3->4->9->None
linklist.insert_at_end(9)

# 5->1->90->2->3->4->9->None
linklist.insert_at_position(2,90)

# 5->1->90->2->3->4->None
linklist.delete_at_end()

linklist.print_list()


from collections import OrderedDict
        
class LRUCache:
    
    def __init__(self,capacity):
        self.cache = OrderedDict()
        self.capacity = capacity
        
    def get(self,index):
        if index in self.cache:
            self.cache.move_to_end(index)
            return self.cache[index]
        return -1
    
    def put(self,index,value):
        if index in self.cache:
            self.cache.move_to_end(index)
        self.cache[index] = value
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)
        
        
class Node:
    def __init__(self,key,value):
        self.key = key
        self.val = value
        self.next = self.prev = None
        

class LRUCache:
    
    def __init__(self,capacity):
        self.capacity = capacity
        self.cache = {}
        self.left = self.right = Node(0,0)
        self.left.next ,self.right.prev = self.right, self.left
        
    def _remove(self,node:Node):
        prev,next = node.prev,node.next
        prev.next, next.prev = next,prev
    
    def _insert(self,node):
        prev,next = self.right.prev, self.right
        prev.next = next.prev = node
        node.next ,node.prev = next,prev
        
    def get(self,index):
        if index in self.cache:
            self._remove(self.cache[index])
            self._insert(self.cache[index])
            return self.cache[index].val
        return -1
            
    def put(self,index,value):
        if index in self.cache:
            self._remove(self.cache[index])
        self.cache[index] = Node(index,value)
        self._insert(self.cache[index])
        
        if len(self.cache) > self.capacity:
            lru = self.left.next
            self._remove(lru)
            del self.cache[lru.index]
        