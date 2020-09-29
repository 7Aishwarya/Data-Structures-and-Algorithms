class Solution(object):
    def partition(self, piles, low, high):
        i = low - 1
        pivot = piles[high]
        for j in range(low,high):
            if piles[j] < pivot:
                i += 1
                piles[i], piles[j] = piles[j], piles[i]
        piles[i+1], piles[high] = piles[high], piles[i+1]
        return i+1
    def quicksort(self, piles, low, high):
        if low < high:
            p = self.partition(piles, low, high)
            self.quicksort(piles, low, p-1)
            self.quicksort(piles, p+1, high)
    def maxCoins(self, piles):
        """
        :type piles: List[int]
        :rtype: int
        """
        n = len(piles)-1
        self.quicksort(piles, 0, n)
        m = len(piles)//3
        n = n - 1
        coins = 0
        while(n>=m):
            coins = coins + piles[n]
            n -= 2
        return coins