class Stack:
    def __init__(self):
        self.arr = []
    
    def push(self, val):
        self.arr.append(val)
    
    def pop(self):
        if len(self.arr) == 0:
            print("Stack is Empty")
            return
        self.arr.pop()
    
    def top(self):
        if len(self.arr) == 0:
            print("Stack is Empty")
            return -1
        return self.arr[-1]
    
    def size(self):
        return len(self.arr)
    
    def display(self):
        for i in range(len(self.arr)):
            print(self.arr[i], end=" ")
        print()

def main():
    st = Stack()
    st.push(10)
    st.push(20)
    st.push(30)
    print(st.size())
    print(st.top())
    st.pop()
    print(st.top())

if __name__ == "__main__":
    main()
