class Node:
    def __init__(self, state, size):
        self.state = state
        self.size = 0
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0
        
    def allocate(self, processSize):
        if self.head is None:
            # primeira inserção
            self.head = Node(processSize)
        else:
            # inserção quando a lista já possui elementos
            pointer = self.head
            while(pointer.next):
                pointer = pointer.next
            pointer.next = Node(processSize)
            self.size = processSize

