class Node:
    def __init__(self, data):
        self.value = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def insert_at_begninning(self, data):
        new_node = Node(data)
        if self.head:
            new_node.next = self.head
            self.head = new_node
        else:
            self.head = new_node
            self.tail = new_node
        
    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head:
            self.tail.next = new_node
        else:
            self.insert_at_begninning(data)

    def remove_at_beginning(self):
        self.head = self.head.next

    def indexOf(self, data):
        count = 0
        current_node = self.head
        while current_node:
            if current_node.value == data:
                return count
            current_node = current_node.next
            count += 1
        print("Data not found.")
        return
    
    def find(self, val: int):
        count = 0
        current_node = self.head
        while count <= val:
            if not current_node:
                print("Index exceeds LinkedList bounds.")
                return
            current_node = current_node.next
        return current_node.value

    def set(self, data, val: int):
        if not self.head:
            self.insert_at_begninning(data)
        count = 0
        current_node = self.head
        new_node = Node(data)
        while count < val:
            if not current_node:
                self.insert_at_end(data)
                print("Index exceeds LinkedList bounds. Data added at end.")
            current_node = current_node.next
        new_node.next = current_node.next
        current_node.next = new_node
    
    def clear(self):
        self.head = None
        self.tail = None
    
    
