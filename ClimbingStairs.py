"""
You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
"""

class Solution:
    # @param n, an integer
    # @return an integer
    def climbStairs(self, n):
        res = [0 ,1, 2]
        if n > 2:
            for i in range(3, n+1):
                res.append(res[i-1] + res[i-2])
        return res[n]