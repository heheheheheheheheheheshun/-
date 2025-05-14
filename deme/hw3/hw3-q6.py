#此题借助大模型
def trap_brute_force(height):
    if not height:
        return 0

    n = len(height)
    total_water = 0

    for i in range(1, n - 1):
        left_max = max(height[:i])
        right_max = max(height[i + 1:])
        water = min(left_max, right_max) - height[i]
        if water > 0:
            total_water += water

    return total_water


# e.g
height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
print(trap_brute_force(height))