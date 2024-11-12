class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class Queue:
    def __init__(self):
        self.head = None

    def enqueue(self, data):
        if self.head is None:
            self.head = Node(data)
            return
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = Node(data)

    def dequeue(self):
        if self.head is None:
            return None
        data = self.head.data
        self.head = self.head.next
        return data

    def peek(self):
        if self.head is None:
            return None
        return self.head.data

    def __str__(self):
        current = self.head
        out = ""
        while current:
            out += str(current.data) + " -> "
            current = current.next
        return out


# test the code
q = Queue()
q.enqueue(1)
q.enqueue(2)
q.dequeue()
print(q)  #
q.enqueue(3)
q.peek()  # 2
print(q)
