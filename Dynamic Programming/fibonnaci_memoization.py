def solve(n, dp):
    if n <= 1:
        return n

    if dp[n] != -1:
        return dp[n]

    dp[n] = solve(n - 1, dp) + solve(n - 2, dp)

    return dp[n]


def fibonnaci(n):
    dp = [-1] * (n + 1)

    solve(n, dp)

    return dp[n]


n = 6
print(fibonnaci(n))
