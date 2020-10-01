class Solution(object):
    def generate(self, l, openb, closeb, n, s=[]):
        if closeb == n:
            l.append(''.join(s))
            return
        else:
            if openb > closeb:
                s.append(')')
                self.generate(l, openb, closeb+1, n, s)
                s.pop()
            if openb < n:
                s.append('(')
                self.generate(l, openb+1, closeb, n, s)
                s.pop()
        return
            
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        l = []
        self.generate(l, 0,0,n)
        return l