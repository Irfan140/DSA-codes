dp = []

# TOP DOWN
def f(i, j, arr):
    if i == j or i + 1 == j:
        return 0
    
    if dp[i][j] != -1:
        return dp[i][j]
    
    ans = float('inf')
    for k in range(i + 1, j):
        ans = min(ans, f(i, k, arr) + f(k, j, arr) + arr[i] * arr[k] * arr[j])
    
    dp[i][j] = ans
    return dp[i][j]

def main():
    global dp
    n = int(input())
    arr = list(map(int, input().split()))
    
    dp = [[-1] * 1000 for _ in range(1005)]
    # For bottom up
    dp = [[0] * 1000 for _ in range(1005)]
    
    for length in range(3, n + 1):
        for i in range(n):
            if i + length - 1 >= n:
                break
            j = i + length - 1
            dp[i][j] = float('inf')
            for k in range(i + 1, j):
                dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j] + arr[i] * arr[k] * arr[j])
    
    print(f(0, n - 1, arr))

if __name__ == "__main__":
    main()
