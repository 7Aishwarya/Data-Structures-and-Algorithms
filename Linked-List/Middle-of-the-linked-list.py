# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        temp = head
        count = 0
        while temp != None:
            count += 1
            temp = temp.next
            
        n = count//2 + 1
        temp = head
        t = 1
        while t < n:
            temp = temp.next
            t += 1
        return temp
            
            
        
        