from os import remove


class Node:
    def __init__(self,data=None,next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    #Length of LinkedList
    def get_length(self):
        counter = 0
        itr = self.head
        while itr:
            counter+=1
            itr = itr.next
        return counter

    #Insert a Node at beginning
    def insert_at_beginning(self,data):
        node = Node(data,self.head)
        self.head = node

    #Add a Node at the end
    def insert_at_end(self,data):
        if self.head == None:
            self.head = Node(data,None)
            return
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data,None)
    #Insert a node at given index

    def insert_at(self,index, data):
        if index<0 or index>=self.get_length():
            raise Exception("Invalid Index")
            return
        if index==0:
            self.insert_at_beginning(data)
            return
        counter = 0
        itr = self.head
        while itr:
            if counter==index-1:
                node = Node(data,itr.next)
                itr.next = node
                break
            itr = itr.next
            counter+=1

    #Insert collection of Values
    def insert_values(self,data_list):
        self.head = None # Make the LinkedList empty
        for data in data_list:
            self.insert_at_end(data)

    #Remove node by index
    def remove_at(self,index):
        if index<0 or index>=self.get_length():
            raise Exception("Invalid Index")
            return
        if index==0:
            self.head = self.head.next
        counter = 0
        itr = self.head
        while itr:
            if counter==index-1:
                itr.next = itr.next.next
                break
            itr = itr.next
            counter+=1

    #Remove node by value
    def remove(self,val):
        if self.head.data == val:
            self.remove_at(0)
        itr = self.head
        counter = 0
        while itr:
            if itr.data == val:
                self.remove_at(counter)
                break
            itr = itr.next
            counter+=1

    #Print the LinkedList
    def print(self):
        if self.head is None:
            print("LinkedList is empty")
            return
        itr = self.head
        llstr = ''
        while itr:
            llstr += str(itr.data)+'-->'
            itr = itr.next
        print(llstr)

    #Insert a node after a data value
    def insert_after_data(self,data_after,data_to_insert):
        itr = self.head
        found = False
        while itr:
            if itr.data == data_after:
                node = Node(data_to_insert,itr.next)
                itr.next = node
                found = True
                break

            itr = itr.next
        if not found:
            raise Exception(data_after,"doesn't exist")




#LinkedList object
ll1 = LinkedList()
ll1.insert_values([1,2,4,5])
ll1.print()
ll1.insert_after_data(2,3)
ll1.print()
ll1.remove(4)
ll1.print()