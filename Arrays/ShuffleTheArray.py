class Solution(object):
    def shuffle(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """
        arr = []
        j = n
        for i in range(n):
            arr.append(nums[i])
            arr.append(nums[j])
            j += 1
        return arr
        