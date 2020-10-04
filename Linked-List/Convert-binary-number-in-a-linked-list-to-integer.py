# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def getDecimalValue(self, head):
        """
        :type head: ListNode
        :rtype: int
        """
        temp = head
        l = []
        while temp != None:
            l.append(temp.val)
            temp = temp.next
            
        n = 0
        sum1 = 0
        for i in range(len(l)-1, -1, -1):
            sum1 += l[i] * (2**n)
            n += 1
        return sum1
        