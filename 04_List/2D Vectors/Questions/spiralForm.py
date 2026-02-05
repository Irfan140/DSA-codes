def main():
    arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    m, n = 3, 3
    minr = 0
    maxr = m - 1
    minc = 0
    maxc = n - 1
    
    while minr <= maxr and minc <= maxc:
        # right
        for j in range(minc, maxc + 1):
            print(arr[minr][j], end=" ")
        minr += 1
        
        # Down
        if minr > maxr or minc > maxc:
            break
        for i in range(minr, maxr + 1):
            print(arr[i][maxc], end=" ")
        maxc -= 1
        
        # Left
        if minr > maxr or minc > maxc:
            break
        for j in range(maxc, minc - 1, -1):
            print(arr[maxr][j], end=" ")
        maxr -= 1
        
        # Up
        if minr > maxr or minc > maxc:
            break
        for i in range(maxr, minr - 1, -1):
            print(arr[i][minc], end=" ")
        minc += 1

if __name__ == "__main__":
    main()
