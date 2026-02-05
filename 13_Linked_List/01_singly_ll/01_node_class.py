class Node:  # Linked list node
    def __init__(self, val):
        self.val = val
        self.next = None 


def main():
    a = Node(1)
    b = Node(2)
    c = Node(3)
    d = Node(4)
    
    a.next = b
    b.next = c
    c.next = d
    
    temp = a
    while temp:
        print(temp.val)
        temp = temp.next

if __name__ == "__main__":
    main()
