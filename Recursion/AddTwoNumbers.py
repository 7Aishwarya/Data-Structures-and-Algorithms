# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def __init__(self):
        self.l = ListNode()
        self.head = self.l
        self.carry = 0
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        '''
        if l1 == None and l2 == None:
            return
        if l1 and l2:
            temp = ListNode((l1.val + l2.val + self.carry)%10)
            self.l.next = temp
            self.l = self.l.next
            self.carry = (l1.val + l2.val + self.carry)/10
            self.addTwoNumbers(l1.next, l2.next)
        if l1 and not l2:
            temp = ListNode((l1.val + self.carry)%10)
            self.l.next = temp
            self.l = self.l.next
            self.carry = (l1.val + self.carry)/10
            self.addTwoNumbers(l1.next, l2)
        if l2 and not l1:
            temp = ListNode((l2.val + self.carry)%10)
            self.l.next = temp
            self.l = self.l.next
            self.carry = (l2.val + self.carry)/10
            self.addTwoNumbers(l1, l2.next)
        if self.carry >= 1:
            while self.carry > 0:
                print(self.carry)
                temp = ListNode(self.carry%10)
                self.l.next = temp
                self.l = self.l.next
                self.carry = self.carry/10
                
        return self.head.next
        '''
        result = ListNode(0)
        result_tail = result
        carry = 0
                
        while l1 or l2 or carry:            
            val1  = (l1.val if l1 else 0)
            val2  = (l2.val if l2 else 0)
            carry, out = divmod(val1+val2 + carry, 10)    
                      
            result_tail.next = ListNode(out)
            result_tail = result_tail.next                      
            
            l1 = (l1.next if l1 else None)
            l2 = (l2.next if l2 else None)
               
        return result.next
        