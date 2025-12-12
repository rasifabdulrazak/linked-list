
class Node:
    def __init__(self, value,next=None):
        self.val = value
        self.next = next
        
        
A = Node(1)
B = Node(2)
C = Node(2)
D = Node(1)

A.next = B
B.next = C
C.next = D
print(A)


class LinkedList:
    def __init__(self,head=None):
        self.head = head
        
    def getbyindex(self,index):
        curr = self.head
        count = 0 
        while curr:
            if index == count: return curr.val
            count+=1
        return -1
    
    def addathead(self,value):
        head = self.head
        new_node = Node(value,head)
        
    def addtail(self,value):
        curr = self.head
        while curr:
            curr = curr.next
        new_node = Node(value,None)
        curr.next = new_node
        
    def addindex(self,index,value):
        curr = self.head
        count = 0
        new_node = Node(value)
        while curr:
            if count == index:
                curr.prev.next = new_node
                new_node.next = curr.next
        
    def deleteindex(self,index):
        curr = self.head
        count = 0
        while curr:
            if index == count:
                curr.prev.next,curr.next = curr.next,


def check_palindrome(node:Node):
    number = ""
    curr = node
    while curr:
        nm = str(curr.val)
        number += nm
        curr = curr.next
    return number == number[::-1]

# print(check_palindrome(A))

def check_palindrome_approch2(node:Node):
    curr = node
    answer = []
    while curr:
        answer.append(curr.val)
        curr = curr.next
    while node:
        ele = answer.pop()
        if ele != node.val: return False
        node = node.next
    return True
# print(check_palindrome_approch2(A),"============")

def check_palindrome_approach3(node:Node):
    slow = node
    fast = node
    while(fast and fast.next):
        slow = slow.next
        fast = fast.next.next

    prev = None
    curr = slow
    while curr:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp

    first = node
    second = prev
    while second:
        if first.val != second.val: return False
        first = first.next
        second = second.next
    return True

# print(check_palindrome_approach3(A),"AProch3")

def delete_nth_node_from_last_two_step(node:Node,val):
    sentinel = Node(0)
    sentinel.next = node
    length = 0
    while node:
        node = node.next
        length+=1
    prev_node = length - val
    prev = sentinel
    for i in range(prev_node):
        prev = prev.next
    prev.next = prev.next.next
    return sentinel.next

# print(delete_nth_node_from_last_two_step(A,2))

def delete_nth_node_from_last_one_step(node:Node,val):
    sentinel = Node(0)
    sentinel.next = node
    fast = sentinel
    for _ in range(val):
        fast = fast.next
    slow = sentinel
    while(slow.next):
        slow = slow.next
        fast = fast.next
    slow.next = slow.next.next
    return sentinel.next

# print(delete_nth_node_from_last_two_step(A,2))

def remove_duplicate_sorted_vals(node:Node):
    curr = node
    while curr and curr.next:
        if curr.val == curr.next.val:
            curr.next = curr.next.next
        else:
            curr = curr.next
    return node

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
    
    def middle(self):
        if not self.head: return
        slow = self.head
        fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
    
    def reverse(self):
        curr = self.head
        prev = None
        temp = None
        while curr:
            temp = curr
            curr.next = prev
            prev = curr
            curr = temp
            
        
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

from functools import lru_cache
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
        
# LRU cache
class Node:
    def __init__(self,key,value):
        self.key = key
        self.val = value
        self.next = self.prev = None
        
class Linkdlist:
    def __init__(self,capacity):
        self.cap = capacity
        self.cache = {}
        self.left = self.right = Node(0,0)
        self.left.next,self.right.prev = self.right,self.left
        # 0<->1<->2<->3<->0
        
    def _remove(self,node:Node):
        prev,next = node.prev,node.next
        prev.next,next.prev = next,prev
    
    def _insert(self,node:Node):
        prev,next = self.right.prev,self.right
        prev.next = next.prev = node
        node.prev,node.next = prev,next
        
    def get(self,key):
        if key in self.cache:
            self._remove(self.cache[key])
            self._insert(self.cache[key])
            return self.cache[key]
        return -1
    
    def put(self,key,value):
        if key in self.cache:
            self._remove(self.cache[key])
        self.cache[key] = Node(key,value)
        self._insert(self.cache[key])
        if len(self.cache) > self.cap:
            lru = self.left.next
            self._remove(lru)
            del self.cache[lru.key]
    
    def print_list(self):
        node = self.left
        result = []
        while node:
            result.append(str(node.val))
            node = node.next
            if node == self.left:  
                break
        print(" <-> ".join(result))
        
lru = Linkdlist(3)
lru.put(1,10)
lru.put(2,20)
lru.put(3,30)

print("srats here")
print(lru.get(2))
lru.print_list()     
 

class TreeNode:
    def __init__(self,value):
        self.val = value
        self.next = None
        
class SingleLinkedlist:
    def __init__(self,head):
        self.head = head
        
    def reverse(self,node):
        curr = node
        prev = None
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        self.head = prev
        return prev
    
    def printlist(self):
        curr = self.head
        while curr:
            print(curr.val,end="->")
            curr = curr.next
        print("None")
    
a = TreeNode(1)
b = TreeNode(2)
c = TreeNode(3)
d = TreeNode(4)
a.next = b
b.next = c
c.next = d

link = SingleLinkedlist(a)
print(link.reverse(a))
print(link.printlist()) 