#3.python代码实现
def sort_strings(A):
    max_len = max(len(s) for s in A)
    for i in range(max_len - 1, -1, -1):
        # 创建26个桶加一个特殊桶用于长度小于当前处理长度的字符串
        buckets = {chr(k): [] for k in range(ord('a'), ord('z') + 1)}
        special_bucket = []

        for s in A:
            if len(s) <= i:
                special_bucket.append(s)
            else:
                buckets[s[i]].append(s)

        # 重新组合回列表
        A = special_bucket
        for k in range(ord('a'), ord('z') + 1):
            A.extend(buckets[chr(k)])

    return A


# 测试
arrays = [["a", "da", "bde", "ab", "bc", "abdc", "cdba"],
          ['ab', 'a', 'b', 'abc', 'ba', 'c'],
          ['aef', 'yzr', 'wr', 'ab', 'bhjc', 'lkabdc', 'pwcdba']]

for A in arrays:
    print(f"原来的字符串: {A}")
    sorted_array = sort_strings(A)
    print(f"排序后的字符串: {sorted_array}\n")
