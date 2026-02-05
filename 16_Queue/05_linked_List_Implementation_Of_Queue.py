class Node:  # This is a user defined data type
    def __init__(self, val):
        self.val = val
        self.next = None

class Queue:  # user defined data structure
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    
    # For inserting element at Tail
    def push(self, val):
        temp = Node(val)
        if self.size == 0:
            self.head = self.tail = temp
        else:
            self.tail.next = temp
            self.tail = temp
        self.size += 1
    
    # for deleting element at Head
    def pop(self):
        if self.size == 0:
            print("Queue is empty")
            return
        temp = self.head
        self.head = self.head.next
        self.size -= 1
        del temp  # no wastage of space
    
    def front(self):
        if self.size == 0:
            print("Queue is empty")
            return -1
        return self.head.val
    
    def back(self):
        if self.size == 0:
            print("Queue is empty")
            return -1
        return self.tail.val
    
    # To display
    def display(self):
        temp = self.head
        while temp is not None:
            print(temp.val, end=" ")
            temp = temp.next
        print()
    
    def Size(self):
        return self.size
    
    def empty(self):
        return self.size == 0

def main():
    q = Queue()
    q.push(1)
    q.push(2)
    q.push(3)
    q.push(4)
    q.display()
    q.push(5)
    q.push(6)
    q.display()
    q.pop()
    q.display()

if __name__ == "__main__":
    main()
