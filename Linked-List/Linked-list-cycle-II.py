# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        temp = head
        hashmap = []
        while temp != None:
            if temp not in hashmap:
                hashmap.append(temp)
            else:
                return temp
            temp = temp.next
        return None
            