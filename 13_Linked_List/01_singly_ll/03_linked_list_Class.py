class Node:
    def __init__(self, val):
        self.val = val
        self.next = None




class LinkedList:  

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    # For inserting element at  Tail
    def insertAtEnd(self, val):
        temp = Node(val)
        if self.size == 0:
            self.head = self.tail = temp
        else:
            self.tail.next = temp
            self.tail = temp
        self.size += 1

    # for inserting element at Head
    def insertAtHead(self, val):
        temp = Node(val)
        if self.size == 0:
            self.head = self.tail = temp
        else:
            temp.next = self.head
            self.head = temp
        self.size += 1

    # for inserting Element at any index
    def insert(self, idx, val):
        if idx < 0 or idx > self.size:
            print("Invalid index")
        elif idx == 0:
            self.insertAtHead(val)
        elif idx == self.size:
            self.insertAtEnd(val)
        else:
            t = Node(val)
            temp = self.head
            for i in range(1, idx):
                temp = temp.next
            t.next = temp.next
            temp.next = t
            self.size += 1

    # for deleting element at Head
    def deleteAtHead(self):
        if self.size == 0:
            print("List is empty")
            return
        self.head = self.head.next
        self.size -= 1
        if self.size == 0:
            self.tail = None

    # deleting element at Tail
    def deleteAtTail(self):
        if self.size == 0:
            print("list is empty")
            return
        if self.size == 1:
            self.head = self.tail = None
            self.size = 0
            return
        temp = self.head
        while temp.next != self.tail:
            temp = temp.next
        temp.next = None
        self.tail = temp
        self.size -= 1

    # deleting element at any index
    def deleteAtIndex(self, idx):
        if idx < 0 or idx >= self.size:
            print("Invalid index")
        elif idx == 0:
            self.deleteAtHead()
        elif idx == self.size - 1:
            self.deleteAtTail()
        else:
            temp = self.head
            for i in range(1, idx):
                temp = temp.next
            temp.next = temp.next.next
            self.size -= 1

    # To get element at any index
    def getAtIdx(self, idx):
        if idx < 0 or idx >= self.size:
            print("Invalid Index")
            return -1
        elif idx == 0:
            return self.head.val
        elif idx == self.size - 1:
            return self.tail.val
        else:
            temp = self.head
            for i in range(idx):
                temp = temp.next
            return temp.val

    # To display 
    def display(self):
        temp = self.head
        while temp is not None:
            print(temp.val, end=" ")
            temp = temp.next
        print()


def main():
    ll = LinkedList()
    ll.insertAtEnd(1)
    ll.display()
    ll.insertAtEnd(2)
    ll.display()

    # cout<<ll.size; //  printing of size of Linked List..

    ll.insertAtHead(9)
    ll.display()
    ll.insertAtHead(100)
    ll.display()

    ll.insert(1, 70)
    ll.display()

    ll.deleteAtHead()
    ll.display()

    ll.deleteAtTail()
    ll.display()

    ll.deleteAtIndex(0)
    ll.display()


if __name__ == "__main__":
    main()
