# Create a Node class to create a node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
    def __str__(self):
        return f'Node of {self.data}'
 
# Create a LinkedList class
class LinkedList:
    def __init__(self):
        self.head = None
        
    # Method to add a node at the end of LL
    def insertAtEnd(self, data):
        new_node = Node(data)
        
        if self.head is None:
            self.head = new_node
            print('\n')
            return
 
        current_node = self.head
        while(current_node.next):
            current_node = current_node.next
 
        current_node.next = new_node
 
    # Method to add a node at begin of LL
    def insertAtBegin(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        else:
            new_node.next = self.head
            self.head = new_node
            
    # print method for the linked list
    def printLL(self):
        current_node = self.head
        while(current_node):
            print(current_node.data)
            current_node = current_node.next
            
    # Print the size of linked list            
    def getCount(self):
        count = 0
        if self.head is None:
            return count
        
        current_node = self.head
        while(current_node):
            count += 1
            current_node = current_node.next
        return count
            

llist = LinkedList()
llist.insertAtEnd('a')
llist.insertAtEnd('b')
llist.insertAtEnd('c')
llist.insertAtEnd('d')
# print the linked list
print("Node Data")
llist.printLL()

print('count', llist.getCount())

