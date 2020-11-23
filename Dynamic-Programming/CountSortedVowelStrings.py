class Solution(object):
    def countVowelStrings(self, n):
        """
        :type n: int
        :rtype: int
        """
        t = [[-1] * 5] * (n+1)
        m = 4
        
        for i in range(5):
            t[0][i] = 1
            
        for i in range(1, n+1):
            for j in range(5):
                if m == 4:
                    t[i][m] = t[i-1][m]
                else:
                    t[i][m] = t[i-1][m] + t[i][m+1]
                m -= 1
                if m == -1:
                    m = 4
        
        return t[n][0]
    