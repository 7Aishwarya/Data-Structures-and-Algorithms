class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        if len(stones) == 1:
            return stones[0]
        if len(stones) == 2:
            stones.sort()
            if stones[1] == stones[0]:
                return 0
            else:
                return stones[1] - stones[0]
        i = len(stones)-1
        while(i>0):
            stones.sort()
            if stones[i] == stones[i-1]:
                stones.pop(i)
                stones.pop(i-1)
                i -= 2
            else:
                stones[i-1] = stones[i] - stones[i-1]
                stones.pop(i)
                i -= 1
        if len(stones) > 0:
            return stones[len(stones)-1]
        else:
            return 0
        