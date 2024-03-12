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

    def pop_node(self):
        if self.head is None and self.tail is None :
            print('List is empty')
        else:
            if self.tail.prev is None:
                self.head = None
                self.tail = None
            else:
                temp = self.tail
                self.tail = self.tail.prev
                self.tail.next = None
                temp.prev = None
            self.length-=1

    def prepend_node(self, value):
        new_node = Node(value)
        if self.head is None and self.tail is None :
            self.head = new_node
            self.tail = new_node
        else:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = self.head.prev
        self.length+=1

    def pop_first(self):
        if self.head is None and self.tail is None:
            print('List is empty')

        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            temp = self.head
            self.head = self.head.next
            self.head.prev = None
            temp.next = None
        self.length-=1

    def get_node(self, index):
        if index < 0 or index >= self.length:
            print('Index out of bound : ', index)
        else:
            if index < self.length/2:
                temp = self.head
                for i in range(0,index):
                    temp = temp.next
                print('from head ->',temp.value)
            else:
                temp = self.tail
                for i in range(0,self.length-1-index):
                    temp=temp.prev
                print('from tail ->',temp.value)

    def set_value(self, index, value):
        if index < 0 or index >= self.length:
            print('Index out of bound : ',index)
        else:
            temp = self.head
            for i in range(0,index):
                temp=temp.next
            temp.value=value

    def insert_node(self, index, value):
        new_node = Node(value)
        if index < 0 or index > self.length:
            print('Index out of bound : ',index)
            return
        elif index == 0:
            temp = self.head
            new_node.next = temp
            temp.prev = new_node
            self.head = self.head.prev
        elif index == self.length:
            temp = self.tail
            new_node.prev = temp
            temp.next = new_node
            self.tail=self.tail.next
        else:
            temp = self.head
            for i in range(0, index-1):
                temp=temp.next
            new_node.next = temp.next
            new_node.prev = temp
            temp.next.prev = new_node
            temp.next = new_node
        self.length+=1
        return

#-----------------------------------------------------#

    def remove_node(self, index):
        if index < 0 or index >= self.length:
            print('Index out of bound : ',index)
            return
        elif index == 0:
            self.head = self.head.next
            self.head.prev.next = None
            self.head.prev = None
        elif index == self.length-1:
            self.tail = self.tail.prev
            self.tail.next.prev = None
            self.tail.next = None
        else:
            temp = self.head
            for i in range(0, index):
                temp = temp.next
            temp.prev.next = temp.next
            temp.next.prev = temp.prev
            temp.prev = None
            temp.next = None
        self.length-=1 


#-----------------------------------------------------#

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
        print('self.head   : ',self.head.value)
        print('self.tail   : ',self.tail.value)
        print('self.length : ',self.length)
        print()


doublyLL = DLL()
doublyLL.append_node(4)
doublyLL.append_node(6)
doublyLL.append_node(8)
doublyLL.append_node(9)
doublyLL.append_node(10)

doublyLL.remove_node(0)

doublyLL.print_list_next()

doublyLL.print_list_prev()
# doublyLL.get_node(3)