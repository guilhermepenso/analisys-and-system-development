# sequencial = []
# sequencial.append(7)

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0
        
    def allocate(self, n):
        if self.head:
            # inserção quando a lista já possui elementos
            pointer = self.head
            while(pointer.next):
                pointer = pointer.next
            pointer.next = Node(n)
        else:
            # primeira inserção
            self.head = Node(n)
        self.size += 1

lista = LinkedList()
lista.size
lista.append(7)
