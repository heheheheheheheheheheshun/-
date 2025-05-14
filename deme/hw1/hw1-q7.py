def find_local_minimum(arr):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        left_neighbor = arr[mid - 1] if mid > 0 else float('inf')
        right_neighbor = arr[mid + 1] if mid < len(arr) - 1 else float('inf')

        if arr[mid] < left_neighbor and arr[mid] < right_neighbor:
            return arr[mid]
        if mid > 0 and arr[mid] > left_neighbor:
            right = mid - 1
        else:
            left = mid + 1

    return None
A = [9, 3, 7, 2, 1, 4, 5]
result = find_local_minimum(A)
print("局部最小值为:", result)