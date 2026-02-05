class Node: 
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

class DLL:  
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    
    # For inserting element at Tail
    def insert_at_tail(self, val):
        temp = Node(val)
        if self.size == 0:
            self.head = self.tail = temp
        else:
            self.tail.next = temp
            temp.prev = self.tail
            self.tail = temp
        self.size += 1
    
    # for inserting element at Head
    def insert_at_head(self, val):
        temp = Node(val)
        if self.size == 0:
            self.head = self.tail = temp
        else:
            temp.next = self.head
            self.head.prev = temp
            self.head = temp
        self.size += 1
    
    # for inserting Element at any index
    def insert_at_index(self, idx, val):
        if idx < 0 or idx > self.size:
            print("Invalid index")
        elif idx == 0:
            self.insert_at_head(val)
        elif idx == self.size:
            self.insert_at_tail(val)
        else:
            t = Node(val)
            temp = self.head
            for i in range(1, idx):
                temp = temp.next
            t.next = temp.next
            temp.next = t
            t.prev = temp
            t.next.prev = t
            self.size += 1
    
    # for deleting element at Head
    def delete_at_head(self):
        if self.size == 0:
            print("List is empty")
            return
        self.head = self.head.next
        if self.head is not None:
            self.head.prev = None
        if self.head is None:
            self.tail = None
        self.size -= 1
    
    # deleting element at Tail
    def delete_at_tail(self):
        if self.size == 0:
            print("list is empty")
            return
        elif self.size == 1:
            self.delete_at_head()
            return
        self.tail.prev.next = None
        self.tail = self.tail.prev
        self.size -= 1
    
    # deleting element at any index
    def delete_at_index(self, idx):
        if idx < 0 or idx >= self.size:
            print("Invalid index")
        elif idx == 0:
            self.delete_at_head()
        elif idx == self.size - 1:
            self.delete_at_tail()
        else:
            temp = self.head
            for i in range(1, idx):
                temp = temp.next
            temp.next = temp.next.next
            temp.next.prev = temp
            self.size -= 1
    
    # to get element at any index
    def get_at_idx(self, idx):
        if idx < 0 or idx >= self.size:
            print("Invalid Size")
            return -1
        elif idx == 0:
            return self.head.val
        elif idx == self.size - 1:
            return self.tail.val
        else:
            if idx < self.size // 2:
                temp = self.head
                for i in range(1, idx + 1):
                    temp = temp.next
                return temp.val
            else:
                temp = self.tail
                for i in range(self.size - 1, idx, -1):
                    temp = temp.prev
                return temp.val
    
    # To display we have to create our own function
    def display(self):
        temp = self.head
        while temp:
            print(temp.val, end=" ")
            temp = temp.next
        print()

def main():
    dll_list = DLL()
    dll_list.insert_at_head(1)
    dll_list.display()
    dll_list.insert_at_tail(2)
    dll_list.display()
    dll_list.insert_at_head(40)
    dll_list.display()
    dll_list.insert_at_index(1, 49)
    dll_list.display()
    dll_list.delete_at_tail()
    dll_list.display()

if __name__ == "__main__":
    main()
