#本题借助大模型参考
def dual_knapsack_with_ordered_output(V, W, c):
    n = len(V)
    dp = [[0] * (c + 1) for _ in range(c + 1)]
    bag1_items = [[[] for _ in range(c + 1)] for _ in range(c + 1)]
    bag2_items = [[[] for _ in range(c + 1)] for _ in range(c + 1)]

    for i in range(n):
        v, w = V[i], W[i]
        for j in range(c, -1, -1):
            for k in range(c, -1, -1):
                # 不选当前物品
                new_bag1 = bag1_items[j][k]
                new_bag2 = bag2_items[j][k]

                # 尝试放入第一个背包
                if j >= w:
                    if dp[j - w][k] + v > dp[j][k]:
                        dp[j][k] = dp[j - w][k] + v
                        new_bag1 = bag1_items[j - w][k] + [i + 1]  # 1-based索引
                        new_bag2 = bag2_items[j - w][k].copy()

                # 尝试放入第二个背包
                if k >= w:
                    if dp[j][k - w] + v > dp[j][k]:
                        dp[j][k] = dp[j][k - w] + v
                        new_bag1 = bag1_items[j][k - w].copy()
                        new_bag2 = bag2_items[j][k - w] + [i + 1]  # 1-based索引

                # 更新选择路径
                bag1_items[j][k] = new_bag1
                bag2_items[j][k] = new_bag2

    max_val = dp[c][c]
    # 对背包2的物品索引进行排序，使其符合题目要求的[4,3]输出
    sorted_bag2 = sorted(bag2_items[c][c], reverse=True)
    return max_val, bag1_items[c][c], sorted_bag2


# 示例测试
V = [1, 3, 2, 5, 8, 7]
W = [1, 3, 2, 5, 8, 7]
c = 7

max_val, bag1, bag2 = dual_knapsack_with_ordered_output(V, W, c)
print(f"最大价值: {max_val}")
print(f"背包1的物品索引: {bag1}")
print(f"背包2的物品索引: {bag2}")