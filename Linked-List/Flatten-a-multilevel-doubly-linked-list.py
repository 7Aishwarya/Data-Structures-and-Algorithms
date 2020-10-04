"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution(object):
    def flatten(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        temp = head
        stack = []
        while temp != None:
            if temp.child:
                if temp.next:
                    stack.append(temp.next)
                temp.next = temp.child
                temp.child.prev = temp
                temp.child = None
            if not temp.next and stack:
                t = stack.pop(len(stack)-1)
                t.prev = temp
                temp.next = t
            temp = temp.next
        return head
                    
''' Example:
1---2---3---4---5---6--NULL
         |
         7---8---9---10--NULL
             |
             11--12--NULL
'''