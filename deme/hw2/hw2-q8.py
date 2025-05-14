#本题借助大模型
def subset_sum(S, W):
    n = len(S)
    dp = [False] * (W + 1)
    dp[0] = True

    for num in S:
        for j in range(W, num - 1, -1):
            if dp[j - num]:
                dp[j] = True
    return dp[W]
#e.g
S = {1, 4, 7, 3, 5}
W = 11
print(subset_sum(S, W))