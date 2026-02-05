class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def display(head):
    if head is None:
        return
    print(head.val, end=" ")
    display(head.next)


def main():
    a = Node(1)
    b = Node(2)
    c = Node(3)
    d = Node(4)

    a.next = b
    b.next = c
    c.next = d

    display(a)


if __name__ == "__main__":
    main()
