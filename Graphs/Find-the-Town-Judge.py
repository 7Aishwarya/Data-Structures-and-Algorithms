class Solution(object):
    def findJudge(self, N, trust):
        """
        :type N: int
        :type trust: List[List[int]]
        :rtype: int
        """
        if N == 1:
            return 1
        d = {}
        for i in range(len(trust)):
            if trust[i][1] in d:
                d[trust[i][1]].append(1)
            else:
                d[trust[i][1]] = [1]
        max1 = 0
        for i in d:
            if max1 < len(d[i]):
                max1 = len(d[i])
                judge = i
        for i in range(len(trust)):
            if trust[i][0] == judge:
                return -1
    
        if max1 == N-1:
            return judge
        else:
            return -1
