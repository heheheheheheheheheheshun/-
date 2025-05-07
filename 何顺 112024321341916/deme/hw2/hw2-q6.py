#本题借助大模型
def longestPalindrome(s: str) -> int:
    n = len(s)
    if n < 2:
        return n
    dp = [[False] * n for _ in range(n)]
    max_length = 1
    for i in range(n):
        dp[i][i] = True
    for length in range(2, n + 1):
        for start in range(n - length + 1):
            end = start + length - 1
            if s[start] == s[end] and (length == 2 or dp[start + 1][end - 1]):
                dp[start][end] = True
                max_length = max(max_length, length)

    return max_length

#e.g
s = "adccaccd"
print(longestPalindrome(s))