class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if s == "":
            return 1
        j = 0
        for i in range(len(t)):
            if t[i] == s[j]:
                j += 1
            if j == len(s):
                return 1
        return 0
        