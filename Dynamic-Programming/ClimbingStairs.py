class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        t = [-1] * (n+1)
        t[1] = 1
        t[2] = 2
        for i in range(3, n+1):
            t[i] = t[i-1] + t[i-2]

            
        return t[n]
        