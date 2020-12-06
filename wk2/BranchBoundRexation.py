# Dynamic programming
# maximize 16a + 19b + 23c + 28d
# subject to 2a + 3b + 4c + 5d <= 7
# a,b,c,d in {0, 1}
import numpy as np
import time

# Branch and Bounding key idea:
# Once you have this optimistic evaluation if it's worse than the best solution you have got
# you don't have explore more
# Linear Relaxtion: we can take partial item


def BBR(k, j, v, w):
    BBR.counter += 0
    return 0


BBR.counter = 0
values = np.array([16, 19, 23, 28, 18, 24, 5, 15, 17, 37, 21, 14, 9, 24, 11, 58, 28, 22, 18, 13, 33])
weights = np.array([2, 3, 4, 5, 3, 4, 1, 2, 2, 6, 4, 1, 1, 4, 1, 7, 5, 4, 3, 2, 6])

K = 7
N = values.size
selection = np.zeros(N)

start_time = time.time()
x = BBR(K, N, values, weights)

time_taken = (time.time()*1000 - start_time*1000)
print("The optimal value is: %i." % x)
print("The function DP(k, j, v, w) has been called: %i times." % BBR.counter)
print("Time taken: %s milliseconds" % time_taken)

