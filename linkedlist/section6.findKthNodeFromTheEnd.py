class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node

        
    def append(self, value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        return True
  
  
        
def find_kth_from_end(list,k):
    slow=list.head
    fast=list.head
    flag=True
    for i in range(k):
        if fast is None:
            print('yoyo')
            return None
        fast=fast.next
    # print(slow.value,fast.value)
    while fast is not None: 
        slow=slow.next
        fast=fast.next
    return slow




my_linked_list = LinkedList(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(4)
my_linked_list.append(5)


k = 2
result = find_kth_from_end(my_linked_list, k)

print('Output 1 : ',result.value)  # Output: 4

my_linked_list = LinkedList(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(4)
my_linked_list.append(5)


k = 5
result = find_kth_from_end(my_linked_list, k)

print('Output 2 : ',result.value)  # Output: 4

my_linked_list = LinkedList(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(4)
my_linked_list.append(5)


k = 8
result = find_kth_from_end(my_linked_list, k)

print('Output 3 : ',result.value)  # Output: 4
"""
    EXPECTED OUTPUT:
    ----------------
    4
    
"""

