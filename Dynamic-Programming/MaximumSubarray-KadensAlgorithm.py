class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cur_best = nums[0]
        overall_best = nums[0]
        for i in range(1, len(nums)):
            cur_best = max(nums[i], cur_best + nums[i])
            overall_best = max(overall_best, cur_best)
        return overall_best
        