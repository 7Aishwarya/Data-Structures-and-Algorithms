import math
class Solution(object):
    def kClosest(self, points, K):
        """
        :type points: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """
        dict1 = {}
        for i in range(len(points)):
            dict1[i] = math.sqrt( points[i][0]**2 + points[i][1]**2 )
        sortDict = sorted(dict1.items(), key=lambda x: x[1])
        
        l = []
        for i in sortDict:
            l.append(points[i[0]])
            K -= 1
            if K == 0:
                break
        return l
            
                
        