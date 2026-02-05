class Stack:  # user defined Data Structure
    def __init__(self):
        self.arr = [0] * 5
        self.idx = -1
    
    def push(self, val):
        if self.idx == len(self.arr) - 1:
            print("Stack is Full")
            return
        self.idx += 1
        self.arr[self.idx] = val
    
    def pop(self):
        if self.idx == -1:
            print("Stack is Empty")
            return
        self.idx -= 1
    
    def top(self):
        if self.idx == -1:
            print("Stack is Empty")
            return -1
        return self.arr[self.idx]
    
    def size(self):
        return self.idx + 1
    
    def display(self):
        for i in range(self.idx + 1):
            print(self.arr[i], end=" ")
        print()

def main():
    st = Stack()
    st.push(10)
    st.push(20)
    st.push(30)
    st.display()

if __name__ == "__main__":
    main()
