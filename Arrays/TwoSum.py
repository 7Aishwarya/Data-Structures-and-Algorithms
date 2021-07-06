class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        d = {}
        for i, j in enumerate(nums):
            if target-j in d.keys():
                return [i, d[target-j]]
            else:
                d[j] = i