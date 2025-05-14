#此题解答借助大模型
def knapsack_max_value(items, max_weight):
    n = len(items)
    # 初始化动态规划表，dp[i][j]表示前i个物品、容量j时的最大价值
    dp = [[0] * (max_weight + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        w, v = items[i - 1]
        for j in range(1, max_weight + 1):
            if j < w:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - w] + v)

    return dp[n][max_weight]


#e.g
items = [(5, 10), (4, 40), (6, 30), (3, 50)]
max_weight = 9

# 计算并输出结果
max_value = knapsack_max_value(items, max_weight)
print(f"最大价值为: {max_value}")

