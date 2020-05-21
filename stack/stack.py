"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order. 

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Stack?
"""
# array
class Stack:
    def __init__(self):
        self.size = 0
        self.storage = []

    def __len__(self):
        return len(self.storage)

    def push(self, value):
        self.storage.append(value)

    def pop(self):
        if len(self.storage) > 0:
            return self.storage.pop()

# linked list

# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None
#     def __len__(self):
#         return len(self.data)

# class Stack:
#     def __init__(self):
#         self.head = None

#     def __len__(self):
#         return len(self.head)

#     def push(self, data):
#         if self.head is None:
#             self.head = Node(data)
#         else:
#             new_node = Node(data)
#             new_node.next = self.head
#             self.head = new_node

#     def pop(self):
#         if self.head is None:
#             return None
#         else:
#             popped = self.head.data
#             self.head = self.head.next
#             return popped