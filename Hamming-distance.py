class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        l1 = []
        while x >= 1:
            r = x%2
            l1.append(r)
            x = x // 2
        l2 = []
        while y >= 1:
            r = y%2
            l2.append(r)
            y = y // 2
        if len(l1) > len(l2):
            diff = len(l1) - len(l2)
            for i in range(diff):
                l2.append(0)
        elif len(l2) > len(l1):
            diff = len(l2) - len(l1)
            for i in range(diff):
                l1.append(0)
        
        count = 0
        for i in range(len(l1)-1, -1, -1):
            if l1[i] != l2[i]:
                count += 1
        return count
        
            
        