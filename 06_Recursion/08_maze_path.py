def maze(row, col):
    if row < 1 or col < 1:
        return 0
    if row == 1 and col == 1:
        return 1

    rightWays = maze(row, col - 1)   # right
    downWays = maze(row - 1, col)    # down

    totalWays = rightWays + downWays
    return totalWays


def printPath(sr, sc, er, ec, s):
    if sr > er or sc > ec:
        return
    if sr == er and sc == ec:   # destination reached
        print(s)
        return

    printPath(sr, sc + 1, er, ec, s + 'R')   # right
    printPath(sr + 1, sc, er, ec, s + 'D')   # down


def main():
    print(maze(3, 3))
    printPath(1, 1, 4, 4, "")


if __name__ == "__main__":
    main()
