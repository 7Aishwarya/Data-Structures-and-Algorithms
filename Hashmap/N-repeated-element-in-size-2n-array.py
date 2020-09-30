class Solution(object):
    def repeatedNTimes(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        temp = []
        for i in range(len(A)):
            if A[i] in temp:
                return A[i]
            temp.append(A[i])