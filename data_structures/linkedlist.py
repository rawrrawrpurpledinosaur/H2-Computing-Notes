class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None
        self.size = self.get_size()

    def get_size(self):
        probe = self.head
        count = 0
        while probe:
            count += 1
            probe = probe.next
        return count

    def append(self, data):
        if self.head == None:
            self.head = Node(data)
        else:
            probe = self.head
            while probe.next:
                probe = probe.next
            probe.next = Node(data)

    def insert(self, data: Node):
        if self.head is None:
            self.head = data
        else:
            probe = self.head
            while probe.next is not None:  # Traverse until the last node
                probe = probe.next
            probe.next = data  # Set the next of the last node to the new node

    def delete(self, index):
        probe = self.head
        for i in range(index - 1):
            probe = probe.next
        probe.next = probe.next.next

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
ll.delete(1)
print(ll)
