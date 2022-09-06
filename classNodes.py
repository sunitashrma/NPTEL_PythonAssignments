# A single node of a signly linked list:

class Node:

     # constructor

     def __init__(self,data, next= None):

         self.data = data
         self.next = next

# creating a single node
first = Node(3)

print(first.data)

# A Linked list class with a single head node

class LinkedList:
    def __init__(self):
    
     self.head = None

# Linked list with a single node

LL = LinkedList()
LL.head = Node (3)

print(LL.head.data)


