#此题借助大模型
def max_profit(stocks, budget):
    n = len(stocks)
    dp = [[0] * (budget + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        w, v = stocks[i - 1]
        for j in range(1, budget + 1):
            if w <= j:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - w] + v)
            else:
                dp[i][j] = dp[i - 1][j]

    # 回溯选中的股票
    res = []
    j = budget
    for i in range(n, 0, -1):
        if dp[i][j] != dp[i - 1][j]:
            res.append(i - 1)
            j -= stocks[i - 1][0]

    return dp[n][budget], [stocks[i] for i in res]


# e.g 输入：股票列表（重量, 价值），预算
stocks = [(5000, 500), (3000, 240), (2000, 240)]
budget = 8000
max_val, selected = max_profit(stocks, budget)
print(f"最大收益: {max_val} 美元")
print("选中股票:", selected)