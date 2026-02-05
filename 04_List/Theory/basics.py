def main():
    v = []  # we don't need to mention size
    
    v.append(6)  # 6 is inserted from back to list (size=1)
    v.append(1)  # 1 is inserted from back to list (size=2)
    v.append(9)
    v.append(0)
    
    print(v[0], end=" ")
    print(v[1], end=" ")
    print(v[2], end=" ")
    print(v[3], end=" ")

if __name__ == "__main__":
    main()
