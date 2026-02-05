# In Python, lists are passed by reference by default (mutable objects)
# However, for immutables like numbers, strings, they are passed by value

def change(a):
    # Lists are mutable, so changes affect the original
    a[0] = 200

def main():
    v = []
    v.append(9)
    v.append(3)
    v.append(1)
    
    for i in range(len(v)):
        print(v[i], end=" ")
    print()
    change(v)
    for i in range(len(v)):
        print(v[i], end=" ")

if __name__ == "__main__":
    main()
