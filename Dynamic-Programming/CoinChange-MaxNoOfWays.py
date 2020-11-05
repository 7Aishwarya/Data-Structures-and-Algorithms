class Solution:
    def count(self, S, m, n): 
        # code here
        t = [ [None] * (n+1) ] * (m+1)
        for i in range(m+1):
            for j in range(n+1):
                if j == 0:
                    t[i][j] = 1
                if i == 0:
                    t[i][j] = 0
                if S[i-1] <= j:
                    t[i][j] = t[i-1][j] + t[i][j-S[i-1]]
                else:
                    t[i][j] = t[i-1][j]
        return t[i][j]