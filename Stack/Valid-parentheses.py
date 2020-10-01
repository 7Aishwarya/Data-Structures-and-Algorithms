class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        opening = ['(', '{', '[']
        closing = [')', '}', ']']
        stack = []
        for i in s:
            if i in opening:
                stack.append(i)
            else:
                if not stack:
                    return False
                if i == ')' and stack[len(stack)-1]=='(':
                    stack.pop(len(stack)-1)
                elif i == '}' and stack[len(stack)-1]=='{':
                    stack.pop(len(stack)-1)
                elif i == ']' and stack[len(stack)-1]=='[':
                    stack.pop(len(stack)-1)
                else:
                    return False
        if not stack:
            return True