def main():
    n = int(input())
    dp = [[0] * 3 for _ in range(n)]
    
    # base case
    # a -> 0, b -> 1, c -> 2
    a, b, c = map(int, input().split())
    dp[0][0] = a
    dp[0][1] = b
    dp[0][2] = c
    
    for i in range(1, n):
        # input of happiness for ith day
        a, b, c = map(int, input().split())
        # ith day -> a
        dp[i][0] = a + max(dp[i-1][1], dp[i-1][2])
        # ith day -> b
        dp[i][1] = b + max(dp[i-1][0], dp[i-1][2])
        # ith day -> c
        dp[i][2] = c + max(dp[i-1][0], dp[i-1][1])
    
    print(max(dp[n-1][0], dp[n-1][1], dp[n-1][2]))

if __name__ == "__main__":
    main()
