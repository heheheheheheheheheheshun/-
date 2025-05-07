def find(profits):
    n=len(profits)
    if(n<2):
        return 0,-1,-1
    profit = 0
    max_profit = 0
    buy_day = 1
    sell_day = 1
    for i in range(len(profits)-1):
        profit = profits[i]
        for j in range(i + 1, len(profits)-1):
            profit += profits[j]
            if max_profit < profit:
                max_profit = profit
                buy_day = i + 1
                sell_day = j + 1
    return max_profit, buy_day, sell_day
profits = [3, 2, 1,-7, 5, 2,-1, 3,-1]
max_profit, buy_day, sell_day = find(profits)
print(f"第{buy_day}天买入, 第{sell_day}天卖出, 收益最大{max_profit},")