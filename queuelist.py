class EmptyError(Exception):
    pass


class Queue:
    def __init__(self):
        self.items = []
        self.count = 0

    def enqueue(self,x):
        self.items.append(x)

    def dequeue(self):
        try:
            self.items[self.count] = None
            self.count+=1
        except Exception as e:
            print(str(e))
    def peek(self):
        if self.count == len(self.items):
            raise EmptyError("Queue is empty")
        print(self.items[self.count])

    def size(self):
        print(len(self.items) - self.count)

    def display(self):
        print(self.items)

obj = Queue()

while True:
    print("1 Enqueue")
    print("2 Dequeue")
    print("3 Peek")
    print("4 Size")
    print("5 Display")
    print("6 quit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        x = input("Enter elem")
        obj.enqueue(x)
    elif choice == 2:
        obj.dequeue()
    elif choice == 3:
        obj.peek()
    elif choice == 4:
        obj.size()
    elif choice == 5:
        obj.display()
    elif choice == 6:
        quit()




