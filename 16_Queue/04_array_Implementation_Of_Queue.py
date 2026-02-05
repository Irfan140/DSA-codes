# Converted from arrayImplementationOfStack.cpp


class ArrayQueue:
    def __init__(self, capacity: int):
        self.f = 0
        self.b = 0
        self.arr = [0] * capacity

    def push(self, val: int) -> None:
        if self.b == len(self.arr):
            print("Queue is full")
            return
        self.arr[self.b] = val
        self.b += 1

    def pop(self) -> None:
        if self.b - self.f == 0:
            print("Queue is empty")
            return
        self.f += 1

    def front(self) -> int:
        if self.b - self.f == 0:
            print("Queue is empty")
            return -1
        return self.arr[self.f]

    def back(self) -> int:
        if self.b - self.f == 0:
            print("Queue is empty")
            return -1
        return self.arr[self.b - 1]

    def size(self) -> int:
        return self.b - self.f

    def empty(self) -> bool:
        return self.size() == 0

    def display(self) -> None:
        for i in range(self.f, self.b):
            print(self.arr[i], end=" ")
        print()


def main():
    q = ArrayQueue(5)
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
