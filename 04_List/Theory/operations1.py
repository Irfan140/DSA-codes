def main():
    v = []
    
    v.append(6)
    v.append(7)
    v.append(1)
    v.append(3)
    
    v.pop()  # last element gets removed
    # size is reduced
    
    for i in range(len(v)):
        print(v[i], end=" ")

if __name__ == "__main__":
    main()
