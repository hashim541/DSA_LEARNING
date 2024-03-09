class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class DLL:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1
    
    def printList(self):
        print('self.head : ',self.head.value)
        print('self.tail : ',self.tail.value)
        print('self.length : ',self.length)
        print()
        temp = self.head
        while temp is not None :
            print('previous : ',temp.prev,'  current : ',temp.value,'  next : ',temp.next)
            temp = temp.next


doublyLL = DLL(5)
doublyLL.printList()
