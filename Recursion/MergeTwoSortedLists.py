# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    '''# Alternative way
    def __init__(self):
        self.temp = ListNode()
        self.head = self.temp
        '''
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        '''
        while l1 and l2:
            if l1.val < l2.val:
                self.temp.next = l1
                l1 = l1.next
            else:
                self.temp.next = l2
                l2 = l2.next
            self.temp = self.temp.next
        if l1:
            self.temp.next = l1
        if l2:
            self.temp.next = l2
            
        return self.head.next
        '''
        temp = None
        if l1 == None:
            return l2
        if l2 == None:
            return l1
        if l1.val <= l2.val:
            temp = l1
            temp.next = self.mergeTwoLists(l1.next,l2)
        else:
            temp = l2
            temp.next = self.mergeTwoLists(l1,l2.next)
        
        return temp
        