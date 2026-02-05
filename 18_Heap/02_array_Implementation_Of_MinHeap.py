class MinHeap:
    def __init__(self):
        self.arr = [0] * 50
        self.idx = 1
    
    def top(self):
        return self.arr[1]  # The root is at index 1
    
    def push(self, x):
        self.arr[self.idx] = x
        i = self.idx
        self.idx += 1
        # Swapping with parent till we reach the root
        while i != 1:
            parent = i // 2
            if self.arr[i] < self.arr[parent]:
                self.arr[i], self.arr[parent] = self.arr[parent], self.arr[i]
            else:
                break
            i = parent
    
    def pop(self):
        if self.idx == 1:
            return  # Empty heap check
        self.idx -= 1
        self.arr[1] = self.arr[self.idx]  # Replace root with last element
        i = 1
        while True:
            left = 2 * i
            right = 2 * i + 1
            if left >= self.idx:
                break  # No children, stop
            if right >= self.idx:  # Only left child exists
                if self.arr[i] > self.arr[left]:
                    self.arr[i], self.arr[left] = self.arr[left], self.arr[i]
                break
            # Both children exist
            if self.arr[left] < self.arr[right]:
                if self.arr[i] > self.arr[left]:
                    self.arr[i], self.arr[left] = self.arr[left], self.arr[i]
                    i = left
                else:
                    break
            else:
                if self.arr[i] > self.arr[right]:
                    self.arr[i], self.arr[right] = self.arr[right], self.arr[i]
                    i = right
                else:
                    break
    
    def display(self):
        for i in range(1, self.idx):
            print(self.arr[i], end=" ")
        print()
    
    def size(self):
        return self.idx - 1

def main():
    pq = MinHeap()
    pq.push(10)
    pq.push(20)
    pq.push(11)
    pq.push(30)
    pq.push(40)
    pq.push(12)
    pq.push(4)
    pq.display()  # Displays the current heap
    print(f"Top: {pq.top()}")  # Shows the minimum element (root)
    pq.pop()  # Removes the top (min) element
    pq.display()  # Displays the heap after pop

if __name__ == "__main__":
    main()
