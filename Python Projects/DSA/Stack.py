from LinkedList import Node

class Stack:
    def __init__(self):
        self.top = None
        self.size = 0
    
    def push(self, data):
        new_node = Node(data)
        if self.top:
            new_node.next = self.top
        self.top = new_node
        self.size += 1

    def pop(self, data):
        if not self.top:
            return None
        else:
            popped_node = self.top
            self.top = self.top.next
            self.size -= 1
            popped_node.next = None
            return popped_node
    
    def clear(self):
        self.top = None
        self.size = 0
