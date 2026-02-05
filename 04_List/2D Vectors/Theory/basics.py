def change2D(v):
    v[1][1] = 100

def main():
    # give some gap..
    v = []
    
    v1 = [1]
    
    v2 = [2, 3]
    
    v3 = [9, 8, 7]
    
    # pushing list to list..
    v.append(v1)
    v.append(v2)
    v.append(v3)
    # v becomes
    # v = [[1], [2, 3], [7, 8, 9]]
    
    print(v[1][1])
    change2D(v)
    print(v[1][1])

if __name__ == "__main__":
    main()
