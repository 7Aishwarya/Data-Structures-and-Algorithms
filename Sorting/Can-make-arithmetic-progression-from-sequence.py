class Solution(object):
    def partition(self, arr, low, high):
        i = low - 1
        pivot = arr[high]
        for j in range(low,high):
            if arr[j] < pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i+1], arr[high] = arr[high], arr[i+1]
        return i+1
    def quicksort(self, arr, low, high):
        if low < high:
            p = self.partition(arr, low, high)
            self.quicksort(arr, low, p-1)
            self.quicksort(arr, p+1, high)
            
        
    def canMakeArithmeticProgression(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        n = len(arr) - 1
        self.quicksort(arr, 0, n)
        diff = arr[1]-arr[0]
        for i in range(len(arr)-1):
            if ( arr[i+1] - arr[i] ) != diff:
                return False
        return True