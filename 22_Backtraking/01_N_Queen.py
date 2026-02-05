grid = []
result = []

def canPlaceQueen(row, col, n):
    # column check
    for i in range(row - 1, -1, -1):
        if grid[i][col] == 'Q':
            return False  # we are attacked
    
    # left diagonal check
    i, j = row - 1, col - 1
    while i >= 0 and j >= 0:
        if grid[i][j] == 'Q':
            return False  # we are attacked
        i -= 1
        j -= 1
    
    # right diagonal check
    i, j = row - 1, col + 1
    while i >= 0 and j < n:
        if grid[i][j] == 'Q':
            return False  # we are attacked
        i -= 1
        j += 1
    
    return True  # no attack found

def f(row, n):
    if row == n:
        # we got one possible answer
        temp = []
        for i in range(n):
            res = ""
            for j in range(n):
                res += grid[i][j]
            temp.append(res)
        result.append(temp)
        return
    
    for col in range(n):
        if canPlaceQueen(row, col, n):
            grid[row][col] = 'Q'  # change of state
            f(row + 1, n)  # move to next column
            grid[row][col] = '.'  # revert the state

def nqueen(n):
    global grid, result
    grid = [['.' for _ in range(n)] for _ in range(n)]
    result = []
    f(0, n)
    return result

def main():
    nqueen(4)

if __name__ == "__main__":
    main()
