class Node:
    def __init__(self,value):
        self.info = value
        self.link = None


class SingleLinkedList:
    def __init__(self):
        self.start = None

    def display_list(self):
        if self.start is None:
            print("List is empty")
            return
        else:
            print("List is: ")
            p = self.start
            while p is not None:
                print(p.info, " ", end="")
                p = p.link
            print()

    def count_nodes(self):
        p = self.start
        n = 0
        while p is not None:
            n += 1
            p = p.link
        print("Number of nodes in the list is", n)

    def search(self,x):
        position = 1
        p = self.start
        while p is not None:
            if p.info == x:
                print(x, "is at ", position)
                return True
            position += 1
            p = p.link
        else:
            print(x," is not in the list")
            return False

    def insert_in_begining(self, data):
        temp = Node(data)
        temp.link = self.start
        self.start = temp

    def insert_at_the_end(self,data):
        temp = Node(data)
        if self.start is None:
            self.start = temp
            return

        p = self.start
        while p.link is not None:
            p = p.link
        p.link = temp


    def create_list(self):
        n = int(input("Enter the number of nodes:  "))
        if n == 0:
            return
        else:
            for i in range(n):
                data = int(input("Enter the elements to be inserted"))
                self.insert_at_the_end(data)

    def insert_after(self,data,x):
        p = self.start
        while p is not None:
            if p.info == x:
                break
            p = p.link

        if p is None:
            print(x,"is not in list")
        else:
            temp = Node(data)
            temp.link = p.link
            p.link = temp

    def insert_before(self,data,x):
        # if list is empty

        if self.start is None:
            print("List is empty")
            return

        # x is the first node, new node to be inserted before first node
        if x == self.start.info:
            temp = Node(data)
            temp.link = self.start
            self.start = temp
            return

        #Find references to predecessor of node containing X

        p = self.start
        while p.link is not None:
            if p.link.info == x:
                break
            p = p.link

        if p.link is None:
            print(x ,"not present in the lsit")
        else:
            temp = Node(data)
            temp.link = p.link
            p.link = temp


    def insert_at_position(self,data,k):
        if k == 1:
            temp = Node(data)
            temp.link = self.start
            self.start = temp
            return

        p = self.start
        i = 0
        while i<k and p is not None:
            p = p.link
            i+=1

        if p is None:
            print("you can insert only upto ",i)
        else:
            temp = Node(data)
            temp.link = p.link
            p.link = temp

    def delete_node(self,x):

        if self.start == None:
            print("List is empty")
            return

        #Deletion of first node:

        if self.start.info == x:
            self.start = self.start.link
            return

        # Deletion in between or at the end:
        p = self.start
        while p.link is not None:
            if p.link.info == x:
                break
            p = p.link
        if p is None:
            print("The element is not in the list")
        else:
            p.link = p.link.link


    def delete_first_node(self):
        if self.start == None:
            return
        self.start = self.start.link

    def _delete_last_node(self):
        if self.start is None:
            return
        if self.start.link is None:
            self.start = None

        p = self.start
        while p.link.link is not None:
            p = p.link
        p.link = None


    def reverse_list(self):
        prev = None
        p = self.start
        while p is not None:
            next = p.link
            p.link = prev
            prev = p
            p = next
        self.start = prev

    def bubble_sort_data(self):
        end = None
        while end != self.start.link:
            p = self.start
            while p.link != end:
                q = p.link
                if p.info > q.info:
                    p.info, q.info = q.info, p.info
                p = p.link
            end = p

    def bubble_sort_links(self):
        end = None
        while end != self.start.link:
            p = r = self.start
            while p.link != end:
                q = p.link
                if p.info > q.info:
                    p.link = q.link
                    q.link = p
                if p != self.start:
                    r.link = q
                else:
                    self.start = q
                p,q = q,p
            r = p
            p = p.link
        end = p

    def merge_sort(self):
        self.start = self._merge_sort(self.start)

    def _merge_sort(self,list_start):
        # If list has only one value
        if list_start is None or list_start.link is None:
            return list_start

        start1 = list_start
        start2 = self.divide_list(start1)
        start1 = self._merge_sort(start1)
        start2 = self._merge_sort(start2)
        startM = self._merge2(start1,start2)
        return startM

    def divide_list(self,p):
        q = p.link.link
        while q is not None and q.link is not None:
            p = p.link
            q = q.link.link
        start2 = p.link
        p.link = None
        return start2



    def _merge2(self,p1,p2):

        if p1.info <= p2.info:
            startM = p1
            p1 = p1.link
        else:
            startM = p2
            p2 = p2.link
        pM = startM

        while p1 is not None and p2 is not None:
            if p1.info <= p2.info:
                pM.link = p1
                p1 =p1.link
                pM = pM.link
            else:
                pM.link = p2
                p2 = p2.link
                pM = pM.link

        while p2 is not None:
            pM.link = p2
            p2 = p2.link
            pM = pM.link
        while p1 is not None:
            pM.link = p1
            p1 = p1.link
            pM = pM.link
        return startM

    def has_cycle(self):
        if self.find_cycle is None:
            return False
        else:
            return True

    def find_cycle(self):
        if self.start is None or self.start.link is None:
            return None
        slowR = self.start
        fastR = self.start

        while fastR is not None and fastR.link is not None:
            slowR = slowR.link
            fastR = fastR.link.link
            if slowR == fastR:
                return slowR
        return None

    def remove_cycle(self):
        c = self.find_cycle()
        if c is None:
            return

        print("the node at which the cycle is detected at", c.info)

        cycle_len = 0
        p = c
        q = c
        while True:
            cycle_len+=1
            q = q.link
            if p == q:
                break

        print("cycle len is",cycle_len)

        rem_len = 0
        p = self.start
        while p!= q:
            p = p.link
            q = q.link
            rem_len+=1

        list_length = cycle_len + rem_len
        print("list length is:", list_length)

        p = self.start
        for i in range(list_length-1):
            p = p.link
        p.link = None

    def insert_cycle(self,x):
        if self.start is None:
            return
        p = self.start
        px = None
        prev = None

        while p is not None:
            if p.info == x:
                px = p
            prev = p
            p = p.link

        if px is not None:
            prev.link = px
        else:
            print(x,"is not in the lsit")




list = SingleLinkedList()
list.create_list()

while True:
    print("1 Display list")
    print("2 count nodes")
    print("3 Search an element")
    print("4 Insert at the begining of the lsit")
    print("5 Insert at the end of the lsit")
    print("6 Insert after a node")
    print("7 insert before a node")
    print("8 Insert element at a postion")
    print("9 Delete first node")
    print("10 Delete last node")
    print("11 Delete a Node")
    print("12 Reverse a lsit")
    print("13 Bubble sort using data")
    print("14 Bubble sort using links")
    print("15 Merge sort")
    print("16 Insert cycle")
    print("17 Detect cycle")
    print("18 Remove cycle")
    print("19 Exit")


    option = int(input("Enter option: "))
    if option == 1:
        list.display_list()
    elif option == 2:
        list.count_nodes()
    elif option == 3:
        data = int(input("Enter the element to be searched: "))
        list.search(data)
    elif option == 4:
        data = int(input("Enter the elem to be inserted at the begining"))
        list.insert_in_begining(data)
    elif option == 5:
        list.insert_at_the_end(int(input("Enter the elem to be inserted at the end")))
    elif option == 6:
        data = int(input("Enter the elem to be inserted "))
        z = int(input("Enter the element after which it has to be inserted"))
        list.insert_after(data,z)
    elif option == 7:
        data = int(input("Enter the elem to be inserted "))
        z = int(input("Enter the element before which it has to be inserted"))
        list.insert_before(data, z)
    elif option == 8:
        data = int(input("Enter the elem to be inserted "))
        z = int(input("Enter the position to be inserted"))
        list.insert_at_position(data,z)
    elif option == 9:
        list.delete_first_node()
    elif option == 10:
        list._delete_last_node()
    elif option ==11:
        list.delete_node(int(input("Enter the element to be deleted")))
    elif option == 12:
        list.reverse_list()
    elif option == 13:
        list.bubble_sort_data()
    elif option ==14:
        list.bubble_sort_links()
    elif option ==15:
        list.merge_sort()
    elif option == 16:
        list.insert_cycle(5)
    elif option == 17:
        list.has_cycle()
    elif option == 18:
        list.remove_cycle()
    elif option == 19:
        quit()