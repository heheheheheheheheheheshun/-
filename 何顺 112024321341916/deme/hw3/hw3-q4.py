def climbStairs(n):
    if n <= 2:
        return n

    # 初始化dp数组
    dp = [0] * (n + 1)
    dp[0], dp[1] = 1, 1

    # 动态规划计算dp[i]
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]


#e.g
n = 10
print(f"爬{n}阶楼梯的方法数为：{climbStairs(n)}")