import math
def do_something(A, p, r):
    n = r - p + 1
    if n == 2 and A[p] > A[r]:
        A[p], A[r] = A[r], A[p]
    elif n >= 3:
        m = math.ceil(2 * n / 3)
        do_something(A, p, p + m - 1)
        do_something(A, r - m + 1, r)
        do_something(A, p, p + m - 1)
#e.g
A = [8, 3, 5, 7, 6, 2, 9, 1, 4]
do_something(A, 0, len(A) - 1)
print(A)