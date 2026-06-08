class ListNode:
    def __init__(self,key,val):
        self.key=key
        self.val=val
        self.next=None
        self.prev=None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity=capacity
        self.cache={}
        self.left=ListNode(0,0)
        self.right=ListNode(0,0)
        self.right.prev=self.left
        self.left.next=self.right

    def remove(self,node):
        p,n=node.prev,node.next
        p.next=n
        n.prev=p
    def insert(self,node):
        p=self.right.prev
        n=self.right
        node.prev=p
        node.next=n
        p.next=node
        n.prev=node
        


    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key]=ListNode(key,value)
        self.insert(self.cache[key])

        if len(self.cache)>self.capacity:
            lru=self.left.next
            self.remove(lru)
            del self.cache[lru.key]
