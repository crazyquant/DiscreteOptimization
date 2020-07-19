# Dynamic programming
# maximize 16a + 19b + 23c + 28d
# subject to 2a + 3b + 4c + 5d <= 7
# a,b,c,d in {0, 1}
import numpy as np


def O(k, j, v, w):
    if j == 0:
        return 0
    elif w[j-1] <= k:
        return max(O(k, j - 1, v, w), v[j-1] + O(k - w[j-1], j - 1, v, w))
    else:
        return O(k, j - 1, v, w)


K = 7
N = 5
v = np.array([16, 19, 23, 28, 55])
w = np.array([2, 3, 4, 5, 6])

x = O(K, N, v, w)
print(x)