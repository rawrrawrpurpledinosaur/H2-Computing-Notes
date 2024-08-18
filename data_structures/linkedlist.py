class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class LinkedList: 
    def __init__(self): 
        self.head = None


    def append(self, data):
        if self.head == None:
            self.head = Node(data) 
        else: 
            probe = self.head
            while probe.next: 
                probe = probe.next
            probe.next = Node(data)

    def insert(self, data, index): 
        probe = self.head
        for i in range(index-1): 
            probe = probe.next
        probe.next = Node(data, probe.next)

    def __str__(self): 
        probe = self.head
        result = ""
        while probe: 
            result += str(probe.data) + " "
            probe = probe.next
        return result

ll = LinkedList()
ll.append(1)
ll.append(2)
ll.insert(3, 1)
print(ll)

