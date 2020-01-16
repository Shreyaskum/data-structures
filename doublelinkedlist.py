class Node(object):
    def __init__(self,value):
        self.info = value
        self.prev = None
        self.next = None

class DoublLinkedList(object):

    def __init__(self):
        self.start = None

    def display_list(self):
        if self.start is None:
            print("Empty list")
            return

        p = self.start
        while p is not None:
            print(p.info, " ",end='')
            p = p.next
        print()

    def insert_in_beginning(self,data):
        temp = Node(data)
        temp.next = self.start
        self.start.prev = temp
        self.start = temp

    def insert_in_empty_list(self,data):
        temp = Node(data)
        self.start = temp

    def insert_at_the_end(self,data):
        temp = Node(data)
        p = self.start
        while p.next is not None:
            p = p.next
        p.next = temp
        temp.prev = p

    def create_list(self):
        n = int(input("Enter the number of nodes: "))
        if n == 0:
            return
        data = int(input("Enter the first element: "))
        self.insert_in_empty_list(data)
        for i in range(n-1):
            data = int(input("Enter the next element: "))
            self.insert_at_the_end(data)

    def insert_after(self,data,x):
        temp = Node(data)
        p = self.start
        while p is not None:
            if p.info == x:
                break
            p = p.next
        if p is None:
            print("The element is not present")
        else:
            temp.prev = p
            temp.next = p.next
            if p.next is not None:
                p.next.prev = temp
            p.next = temp

    def insert_before(self,data,x):
        if self.start is None:
            return
        if self.start.info == x:
            temp = Node(data)
            temp.next = self.start
            self.start.prev = self.start
            self.start = temp
            return

        p = self.start
        while p is not None:
            if p.next == x:
                break
            p = p.next

        if p is None:
            print("The element is not present")
        else:
            temp = Node(data)
            temp.next = p
            temp.prev = p.prev
            p.prev.next = temp
            p.prev = temp

    def delete_first_node(self):
        if self.start is None:
            return
        if self.start.next is None:
            self.start = None
            return
        self.start = self.start.next
        self.start.prev = None

    def delete_last_node(self):
        if self.start is None:
            return
        if self.start.next is None:
            self.start = None
            return

        p = self.start
        while p.next is not None:
            p = p.next
        p.prev.next = None

    def delete_node(self,x):
        if self.start is None:
            return
        if self.start.next is None:
            if self.start.info == x:
                self.start = None
            else:
                print("value not found")
            return

        # deletion of first node:

        if self.start.info == x:
            self.start = self.start.next
            self.start.prev = None
            return

        p = self.start
        while p.next is not None:
            if p.info == x:
                break
            p = p.next

        if p.next is not None: # Node to be deleted is in between
            p.prev.next = p.next
            p.next.prev = p.prev
        else:
            if p.info == x:# Node to be deleted is last node
                p.prev.next = None
            else:
                print("Element not found")

    def reverse_list(self):
        if self.start is None:
            return
        p1 = self.start
        p2 = self.start.next
        p1.next = None
        p1.prev = p2
        while p2 is not None:
            p2.prev = p2.next
            p2.next = p1
            p1 = p2
            p2 = p2.prev
        self.start = p1










list = DoublLinkedList()
list.create_list()

while True:
    print("1 Display list")
    print("2 Insert in empty list")
    print("3 Insert node in the begining")
    print("4 Insert node at the end")
    print("5 Insert node after a specified position")
    print("6 Insert node before a specified position")
    print("7 Delete first node")
    print("8 Delete last node")
    print("9 Delete any node")
    print("10 Reverse list")
    print("11 quit")

    option = int(input("Enter your choice"))

    if option == 1:
        list.display_list()
    elif option ==2:
        list.insert_in_empty_list(int(input("Enter an elemnet to be insertd")))
    elif option ==3:
        list.insert_in_beginning(int(input("Enter the element to be at the begining ")))
    elif option == 4:
        list.insert_at_the_end(int(input("Enter the element to be at the end ")))
    elif option == 5:
        list.insert_after((int(input("Enter the element to be inserted "))),(int(input("Enter the next node"))))
    elif option == 6:
        list.insert_after((int(input("Enter the element to be inserted "))), (int(input("Enter the previous node"))))
    elif option == 7:
        list.delete_first_node()
    elif option == 8:
        list.delete_last_node()
    elif option == 9:
        list.delete_node(int(input("Enter the element to be deleted")))
    elif option ==10:
        list.reverse_list()
    elif option == 11:
        quit()


