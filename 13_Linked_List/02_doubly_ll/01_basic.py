class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

def display(head):
    while head:
        print(head.val, end=" ")
        head = head.next
    print()

def reverse(tail):
    while tail:
        print(tail.val, end=" ")
        tail = tail.prev
    print()

def main():
    a = Node(1)
    b = Node(2)
    c = Node(3)
    d = Node(4)
    
    a.next = b
    b.next = c
    c.next = d
    d.prev = c
    c.prev = b
    b.prev = a
    
    display(a)
    reverse(d)

if __name__ == "__main__":
    main()
