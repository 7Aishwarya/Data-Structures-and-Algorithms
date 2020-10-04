class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        while n >= 1:
            r = n%2
            if r == 1:
                count += 1
            n = n//2
        return count
        