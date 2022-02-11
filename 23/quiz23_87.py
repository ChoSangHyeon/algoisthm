import collections


def climbsrairs(n: int) -> int:
    refo = collections.defaultdict(int)
    if n == 1:
        return 1
    if n == 2:
        return 2
    if refo[n]:
        return refo[n]
    refo[n] = climbsrairs(n - 1) + climbsrairs(n - 2)
    return refo[n]


print(climbsrairs(7))
from collections import defaultdict


class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n

        dp = [0] * (n + 1)

        dp[1] = 1
        dp[2] = 2

        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]

        return dp[n]