class Queue:
    def __init__(self, val):
        self.f = 0
        self.b = 0
        self.s = 0  # maintaining a size variable
        self.arr = [0] * val
    
    def push(self, val):
        if self.b == len(self.arr):
            print("Queue is full")
            return
        self.arr[self.b] = val
        self.b += 1
        self.s += 1
    
    def pop(self):
        if self.s == 0:
            print("Queue is empty")
            return
        self.f += 1
        self.s -= 1
    
    def front(self):
        if self.s == 0:
            print("Queue is empty")
            return -1
        return self.arr[self.f]
    
    def back(self):
        if self.s == 0:
            print("Queue is empty")
            return -1
        return self.arr[self.b - 1]
    
    def size(self):
        return self.s
    
    def empty(self):
        return self.f - self.b == 0
    
    def display(self):
        for i in range(self.f, self.b):
            print(self.arr[i], end=" ")
        print()

def main():
    q = Queue(5)
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
