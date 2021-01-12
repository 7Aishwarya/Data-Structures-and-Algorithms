'''Time limit may exceed using recursive approach, therefore space optimized solution using dp'''
class Solution(object):
    def tribonacci(self, n):
        """
        :type n: int
        :rtype: int
        """
        i = 0
        if n == 0:
            return 0
        if n == 1 or n == 2:
            return 1
        a, b, c = 0, 1, 1
        i = 3
        while i <= n:
            d = a + b + c
            a = b
            b = c
            c = d
            i += 1
        return d
