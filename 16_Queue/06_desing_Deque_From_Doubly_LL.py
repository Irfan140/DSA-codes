# Converted from desingDequeFromDoublyLL.cpp


class Node:
    def __init__(self, val: int):
        self.val = val
        self.next = None
        self.prev = None


class Deque:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def pushBack(self, val: int) -> None:
        temp = Node(val)
        if self.size == 0:
            self.head = self.tail = temp
        else:
            self.tail.next = temp
            temp.prev = self.tail
            self.tail = temp
        self.size += 1

    def pushFront(self, val: int) -> None:
        temp = Node(val)
        if self.size == 0:
            self.head = self.tail = temp
        else:
            temp.next = self.head
            self.head.prev = temp
            self.head = temp
        self.size += 1

    def popFront(self) -> None:
        if self.size == 0:
            print("List is empty")
            return
        self.head = self.head.next
        if self.head is not None:
            self.head.prev = None
        if self.head is None:
            self.tail = None
        self.size -= 1

    def popBack(self) -> None:
        if self.size == 0:
            print("list is empty")
            return
        elif self.size == 1:
            self.popFront()
            return
        self.tail = self.tail.prev
        self.tail.next = None
        self.size -= 1

    def front(self) -> int:
        if self.size == 0:
            print("Deque is empty")
            return -1
        return self.head.val

    def back(self) -> int:
        if self.size == 0:
            print("Deque is empty")
            return -1
        return self.tail.val

    def Size(self) -> int:
        return self.size

    def empty(self) -> bool:
        return self.size == 0

    def display(self) -> None:
        temp = self.head
        while temp:
            print(temp.val, end=" ")
            temp = temp.next
        print()


def main():
    dq = Deque()
    dq.pushBack(10)
    dq.pushBack(20)
    dq.pushBack(30)
    dq.pushBack(40)
    dq.display()
    dq.popBack()
    dq.display()


if __name__ == "__main__":
    main()
