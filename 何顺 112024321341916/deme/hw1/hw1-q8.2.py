class MinHeap:
    def __init__(self):
        self.heap = []

    def push(self, val):
        self.heap.append(val)
        self._sift_up(len(self.heap) - 1)

    def pop(self):
        if not self.heap:
            return None
        self._swap(0, len(self.heap) - 1)
        val = self.heap.pop()
        self._sift_down(0)
        return val

    def _sift_up(self, idx):
        while idx > 0:
            parent = (idx - 1) // 2
            if self.heap[idx] < self.heap[parent]:
                self._swap(idx, parent)
                idx = parent
            else:
                break

    def _sift_down(self, idx):
        while 2 * idx + 1 < len(self.heap):
            left = 2 * idx + 1
            right = 2 * idx + 2
            min_child = left
            if right < len(self.heap) and self.heap[right] < self.heap[left]:
                min_child = right
            if self.heap[min_child] < self.heap[idx]:
                self._swap(idx, min_child)
                idx = min_child
            else:
                break

    def _swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]


def find_k_smallest_heap(arr, k):
    heap = MinHeap()
    # 建堆 O(n log n)
    for num in arr:
        heap.push(num)
    # 取前k小 O(k log n)
    return [heap.pop() for _ in range(k)]


# 测试
arr = [4, 1, 7, 3, 9, 2]
k = 3
print(find_k_smallest_heap(arr, k))
#此问借助了大模型参考