class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class Stack:
    def __init__(self): 
        self.top = None
    
    def push(self, data):
        self.top = Node(data, self.top)

    def pop(self): 
        data = self.top
        self.top= self.top.next
        return data.data

    def __str__(self): 
        ret = "TOP -> "
        current = self.top
        while current:
            ret += str(current.data) + " -> "
            current = current.next
        return ret

s = Stack()
s.push(1) 
s.push(2)
print(s.pop())
s.push(3)
print(s)
