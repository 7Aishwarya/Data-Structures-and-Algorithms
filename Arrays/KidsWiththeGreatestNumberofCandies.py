class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        max1 = max(candies)
        for count, val in enumerate(candies):
            if val+extraCandies >= max1:
                candies[count] = True
            else:
                candies[count] = False
        return candies