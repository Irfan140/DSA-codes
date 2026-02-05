# Find the length of longest subarray which has maximum possible bitwise AND value

def main():
    arr = [12, 3, 1, 6, 1, 6, 6, 6, 6, 4, 3, 8, 13, 13, 13, 13, 8]
    n = len(arr)
    ans = 0
    max_el = float('-inf')
    count = 0
    for i in range(n):
        if arr[i] > max_el:
            max_el = arr[i]
            count = 1
        elif arr[i] == max_el:
            count += 1
        else:
            count = 0
        ans = max(ans, count)
    print(ans)

if __name__ == "__main__":
    main()
