class Solution(object):
    def restoreString(self, s, indices):
        """
        :type s: str
        :type indices: List[int]
        :rtype: str
        """
        arr = [0] * len(indices)
        l = ''
        for i in range(len(indices)):
            arr[indices[i]] = s[i]
        for i in range(len(indices)):
            l = l + arr[i]
        return l
