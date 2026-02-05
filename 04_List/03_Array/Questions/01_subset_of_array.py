def printSubsets(arr, idx, ans):
    n = len(arr)
    if idx == n:
        print(ans)
        return
    
    # Don't take current element
    printSubsets(arr, idx + 1, ans)

    # Take current element
    ans.append(arr[idx])
    printSubsets(arr, idx + 1, ans)

    # Backtrack
    ans.pop()

def main():
    arr = [1, 2, 3]
    v = []
    printSubsets(arr, 0, v)

if __name__ == "__main__":
    main()
