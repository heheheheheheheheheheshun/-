#本题借助大模型参考
def min_edit_distance(x, y):
    m, n = len(x), len(y)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # 初始化边界条件
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j

    # 动态规划填表
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if x[i - 1] == y[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(dp[i][j - 1],  # 插入
                                   dp[i - 1][j],  # 删除
                                   dp[i - 1][j - 1])  # 替换

    return dp[m][n]


# e.g
x, y = "abcd", "bcfe"
print(f"最小编辑距离: {min_edit_distance(x, y)}")  # 输出: 3