from itertools import combinations
class Solution(object):
    def numIdenticalPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        hashmap = {}
        for i in range(len(nums)):
            if nums[i] not in hashmap:
                hashmap[nums[i]] = [1]
            else:
                hashmap[nums[i]].append(1)
        count = 0
        for i in hashmap:
            if len(hashmap[i])>1:
                count = count + len(list(combinations(hashmap[i], 2))) 
        return count