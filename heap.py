class Heap:
    def __init__(self,maxSize = 10):
        self.a = [None]*maxSize
        self.a[0] = 10000
        self.n = 0

    def insert(self, value):
        self.n+=1
        self.a[self.n] = value
        self.restore_up(self.n)

    def restore_up(self,i):
        k = self.a[i]
        iparent = i//2

        while self.a[iparent] < k:
            self.a[i] = self.a[iparent]
            i = iparent
            iparent = i//2
        self.a[i] = k

    def delete_root(self):
        maxvalue = self.a[1]
        self.a[1] = self.a[self.n]
        self.n-=1
        self.restore_down(1)
        return maxvalue

    def restore_down(self, i):
        k = self.a[i]
        lchild = 2*i
        rchild = lchild+1

        while self.n >= rchild:
            if k >= self.a[lchild] and k >= self.a[rchild]:
                self.a[i] = k
                return
            else:
                if self.a[lchild] > self.a[rchild]:
                    self.a[i] = self.a[lchild]
                    i = lchild
                else:
                    self.a[i] = self.a[rchild]
                    i = rchild
                lchild = i*2
                rchild = lchild+1

        # If the number of nodes is even
        if lchild == self.n and k < self.a[lchild]:
            self.a[i] = self.a[lchild]
            i = lchild
        self.a[i] = k

    def display(self):
        for i in range(1,self.n+1):
            print(self.a[i],end = " ")
        print()
h = Heap()
while True:
    print("1 Insert")
    print("2 Delete root")
    print("3 Display")
    print("4 Exit")
    choice = int(input("Enter the value to be inserted"))

    if choice == 1:
        value = int(input("Enter value to be inserted: "))
        h.insert(value)
    elif choice == 2:
        print("Max value is", h.delete_root())
    elif choice == 3:
        h.display()
    elif choice == 4:
        break
    else:
        print("Wrong option")


