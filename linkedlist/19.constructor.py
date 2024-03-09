class Node:
    def __init__(self, value):
        self.value=value
        self.next=None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length=0
    
    def print_list(self):
        temp = self.head
        while temp is not None :
            print(temp.value)
            temp=temp.next
    
    def append_node(self,value):
        new_node = Node(value)
        if self.head is None and self.tail is None :
            self.head = new_node
            self.tail = new_node
            self.length = 1
        else :
            temp=self.head
            self.tail.next = new_node
            self.tail=new_node
            self.length+=1
    
    def pop(self):
        if self.head is None :
            print('nothing to pop')
        elif self.length == 1:
            self.head = None
            self.tail = None
            self.length = 0
        else : 
            temp = self.head
            while temp.next.next is not None :
                temp=temp.next
            self.tail = temp
            temp.next = None
            self.length -= 1
    
    def prepend(self,value):
        new_node = Node(value)
        if self.head is None :
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length+=1
    
    def pop_first(self):
        if self.head is None:
            print('nothing to pop')
        elif self.length == 1:
            self.head = None
            self.tail = None
            self.length -= 1
        else:
            temp = self.head
            self.head = self.head.next
            temp.next = None
            self.length -= 1
    
    def get(self, index):
        i=0;
        temp=self.head
        if index >= self.length or index < 0:
            print('no such index')
            return None
        while(i < self.length):
            if(i == index):
                return temp
            temp=temp.next
            i+=1

    def set_value(self,index,value):
        i=0
        temp=self.head
        if index >= self.length or index < 0:
            print('no such index')
            return None
        while(i < self.length):
            if(i == index):
                temp.value = value
                return temp
            temp=temp.next
            i+=1
    
    def insert(self,index,value):
        if index >= self.length or index < 0:
            print('no such index')
            return None
        if index == 0:
            self.prepend(value)
            return True
        if index == self.length:
            self.append_node(value)
            return True
        new_node = Node(value)
        temp = self.get(index-1)
        new_node.next=temp.next
        temp.next=new_node
        return new_node

    def remove(self,index):
        if index >= self.length or index < 0:
            print('no such index')
            return None
        if index == 0:
            self.pop_first()
            return True
        if index == self.length:
            self.pop()
            return True
        temp1=self.get(index-1)
        remove_node = temp1.next
        temp1.next=temp1.next.next
        remove_node.next = None
        return remove_node

    def reverse(self):
        temp=self.head
        self.head=self.tail
        self.tail=temp
        after = temp.next
        before = None
        for _ in range(self.length):
            after=temp.next
            temp.next=before
            before = temp
            temp=after
    


linked_list = LinkedList()
print('Head : ',linked_list.head)
print('Tail : ',linked_list.tail)
print('Length : ',linked_list.length)
linked_list.append_node(5)
linked_list.append_node(6)
linked_list.append_node(7)
linked_list.print_list()
print('Head : ',linked_list.head.value)
print('Tail : ',linked_list.tail.value)
print('Length : ',linked_list.length)
# linked_list.prepend(4)
# linked_list.print_list()
# print('Head : ',linked_list.head.value)
# print('Tail : ',linked_list.tail.value)
# print('Length : ',linked_list.length)
# linked_list.pop_first()
# linked_list.print_list()
# print('Head : ',linked_list.head.value)
# print('Tail : ',linked_list.tail.value)
# print('Length : ',linked_list.length)
# print(linked_list.get(3))
print(linked_list.reverse())
linked_list.print_list()
print('Head : ',linked_list.head.value)
print('Tail : ',linked_list.tail.value)
print('Length : ',linked_list.length)