class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class Stack:
    def __init__(self):
        self.head = None
        self.size = 0

    def push(self, val):
        temp = Node(val)
        temp.next = self.head
        self.head = temp
        self.size += 1

    def pop(self):
        if self.head is None:
            print("Stack is Empty")
            return
        self.head = self.head.next
        self.size -= 1

    def top(self):
        if self.head is None:
            print("Stack is Empty")
            return -1
        return self.head.val

    def print(self, temp):
        if temp is None:
            return
        self.print(temp.next)
        print(temp.val, end=" ")

    def display(self):
        temp = self.head
        self.print(temp)
        print()


def main():
    st = Stack()
    st.push(1)
    st.push(2)
    st.push(3)
    st.push(4)
    st.display()


if __name__ == "__main__":
    main()
