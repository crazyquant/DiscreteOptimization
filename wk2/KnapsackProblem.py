import time
import numpy as np


class Knapsack:
    # A class to solve Knapsack problems presented in Coursera, Discrete Optimisation, week 2

    def __init__(self, values, weights):
        self.diagnose = False
        self.v = values
        self.w = weights
        self.method_names = {1: "DP",
                             2: "DP (Branch & Bound)",
                             3: "DP (Branch & Bound, fractional item)"
                             }

    def solve(self, capacity, method):
        self.count = 0
        self.currentBest = 0
        self.K = capacity
        self.method = method
        start_time = time.time()

        if method == 1:
            self.value = self.DP(self.K, self.v.size, self.v, self.w)
        elif method == 2:
            self.value = self.DP_BB1(self.K, self.v.size, self.v, self.w)

        self.time_taken = (time.time() * 1000 - start_time * 1000)

    def print(self):
        print("Capacity of this knapsack problem:", self.K)
        print("Optimal value:", self.value)
        print("Method used is:", self.method_names[method])
        print("Time taken: %s ms" % round(self.time_taken, 0))
        print("The function has been called: %i times." % self.count)

    def DP(self, k, j, v, w):
        self.count += 1
        if self.diagnose:
            print(f"count={self.count} | k={k} | j={j} | v={v} | w={w}")
        if j == 0:
            return 0
        elif w[j - 1] <= k:
            return max(self.DP(k, j - 1, v, w), v[j - 1] + self.DP(k - w[j - 1], j - 1, v, w))
        else:
            return self.DP(k, j - 1, v, w)

    def DP_BB1(self, k, j, v, w):
        self.count += 1
        if self.diagnose:
            print(f"count={self.count} | k={k} | j={j} | v={v} | w={w}")

        if j == 0 or v.dot(w) < self.currentBest:
            return 0
        elif w[j - 1] <= k:
            value = max(self.DP(k, j - 1, v, w), v[j - 1] + self.DP(k - w[j - 1], j - 1, v, w))
            if value > self.currentBest:
                self.currentBest = value
            return value
        else:
            return self.DP(k, j - 1, v, w)


v1 = np.array([16, 19, 23, 28, 18, 24, 5, 15, 17, 37, 21, 14, 9, 24, 11, 58, 28, 22, 18,
               13, 33, 16, 19, 23, 28, 18, 24, 5, 15, 17, 37, 21, 14, 9, 24, 11, 58, 28, 22, 18, 13, 33,
               16, 19, 23, 28, 18, 24, 5, 15, 17, 37, 21, 13, 33, 16, 19, 23, 28, 18, 24, 5, 15, 17])

w2 = np.array([2, 3, 4, 5, 3, 4, 1, 2, 2, 6, 4, 1, 1, 4, 1, 7, 5, 4, 3, 2, 6, 2, 3, 4, 5, 3, 4, 1, 2, 2, 6,
               4, 1, 1, 4, 1, 7, 5, 4, 3, 2, 6, 2, 3, 4, 5, 3, 4, 1, 2, 2, 6, 4,
               1, 1, 4, 1, 7, 5, 4, 3, 2, 6, 2, 3, 4, 5, 3, 4, 1, 2, 2])

v2 = np.array([45, 48, 35])
w2 = np.array([5, 8, 3])

knapsack1 = Knapsack(v2, w2)
knapsack1.diagnose = False

K = 10
method = 2
knapsack1.solve(K, method)
knapsack1.print()
