def main():
    # 3 rows and 4 columns..
    v = [[20 for _ in range(4)] for _ in range(3)]
    
    for i in range(3):
        for j in range(4):
            print(v[i][j], end=" ")
        print()
    
    print()
    print(len(v))  # list size
    print(len(v[0]))  # means 0th position main jo list hai uska size...

if __name__ == "__main__":
    main()
