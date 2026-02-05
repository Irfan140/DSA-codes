def main():
    v = []
    
    v.append(6)
    print(len(v))
    # Python lists don't have a separate capacity concept like C++ vectors
    
    v.append(7)
    print(len(v))
    
    v.append(1)
    print(len(v))
    
    v.append(3)
    print(len(v))
    
    # capacity and size are two different things in C++
    # Python lists automatically manage capacity

if __name__ == "__main__":
    main()
