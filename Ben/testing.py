# Dynamic programming
# maximize 16a + 19b + 23c + 28d
# subject to 2a + 3b + 4c + 5d <= 7
# a,b,c,d in {0, 1}
import numpy as np

w = np.array([2, 3, 4,])
x = np.array([1, 2, 3])

print(w.dot(x))

