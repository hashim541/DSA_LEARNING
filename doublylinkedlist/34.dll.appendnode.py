class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class DLL:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def append_node(self, value):
        new_node = Node(value)
        if self.head is None and self.tail is None :
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length+=1
        
    def print_list_next(self):
        self.print_dll_headers('next')
        temp = self.head
        while temp is not None :
            self.print_format(temp)
            temp = temp.next
    
    def print_list_prev(self):
        self.print_dll_headers('prev')
        temp = self.tail
        while temp is not None :
            self.print_format(temp)
            temp = temp.prev

    def print_format(self, temp):
        if temp.prev is not None :
            print('previous : ',temp.prev.value, end='    ')
        else :
            print('previous : None', end='  ')
        print('current : ',temp.value,end='  ')
        if temp.next is not None:
            print('next : ',temp.next.value)
        else:
            print('next : None')

    def print_dll_headers(self, parse):
        print()
        if parse == 'next':
            print(' - - - - - - - - NEXT NODE - - - - - - - - ')
        else:
            print(' - - - - - - - - PREV NODE - - - - - - - - ')
        print('self.head : ',self.head.value)
        print('self.tail : ',self.tail.value)
        print('self.length : ',self.length)
        print()


doublyLL = DLL()
doublyLL.append_node(4)
doublyLL.append_node(6)
doublyLL.append_node(7)
doublyLL.print_list_next()
doublyLL.print_list_prev()