# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if headA == None or headB == None:
            return None
        
        temp1 = headA
        temp2 = headB
        flag1 = flag2 = None
        
        while temp1 != temp2:
            if temp1.next == None:
                flag1 = temp1.val
                temp1 = headB
            else:
                temp1 = temp1.next
            if temp2.next == None:
                flag2 = temp2.val
                temp2 = headA
            else:
                temp2 = temp2.next
            if flag1 and flag2:
                if flag1 != flag2:
                    return None
        return temp1
            
                
        
    '''Approach : Two Pointers
 - Maintain two pointers temp1 and temp2 initialized at the head of A and B, respectively. 
 - Then let them both traverse through the lists, one node at a time.
 - When temp1 reaches the end of a list, then redirect it to the head of B; similarly when temp2 reaches the end of a list, redirect it the head of A.
 - If at any point temp1 meets temp2, then temp1/temp2 is the intersection node.

Consider the following two lists: A = {1,3,5,7,9,11} and B = {2,4,9,11}, which are intersected at node '9'. 
 - Since B.length (=4) < A.length (=6), temp2 would reach the end of the merged list first, 
   because temp2 traverses exactly 2 nodes less than temp1 does. 
 - By redirecting temp2 to head A, and temp1 to head B, we now ask temp2 to travel exactly 2 more nodes than temp1 would. 
 - So in the second iteration, they are guaranteed to reach the intersection node at the same time.
 - If two lists have intersection, then their last nodes must be the same one. So when temp1/temp2 reaches the end of a list, 
   record the last element of A/B respectively. If the two last elements are not the same one, then the two lists have no intersections.
'''