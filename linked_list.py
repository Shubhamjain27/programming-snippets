#creation

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head=None

    
#traversal 
    def traversal(self):
        current_node = self.head
        while start is not None:
            print(current_node.value)
            current_node = current_node.next


#Insert in beginning

    def insert_beginning(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node


#Insert at end

    def insert_end(self, value):
        new_node = Node(value)
        last_node = self.head
        while last_node.next is not None:
            last_node = last_node.next

        last_node.next = new_node


    def inse
list1 = LinkedList()
list1.head = Node("Mon")
e2 = Node("Tue")
e3 = Node("Wed")

list1.head.next = e2

e2.next = e3



