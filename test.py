class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            return

        current = self.head
        while current.next:
            current = current.next

        current.next = new_node

    def print_list(self):
        current = self.head
        while current:
            print(str(current.value), end=" -> ")
            current = current.next
        print("None")

list = LinkedList()
list.append(10)
list.append(20)
list.append(30)
list.print_list()