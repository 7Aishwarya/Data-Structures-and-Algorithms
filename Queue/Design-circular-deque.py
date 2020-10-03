class MyCircularDeque(object):

    def __init__(self, k):
        """
        Initialize your data structure here. Set the size of the deque to be k.
        :type k: int
        """
        self.queue = []
        self.front = self.rear = 0
        self.k = k
        

    def insertFront(self, value):
        """
        Adds an item at the front of Deque. Return true if the operation is successful.
        :type value: int
        :rtype: bool
        """
        if self.rear == self.k:
            return False
        else:
            self.queue = [value] + self.queue
            self.rear = self.rear + 1
            return True
        

    def insertLast(self, value):
        """
        Adds an item at the rear of Deque. Return true if the operation is successful.
        :type value: int
        :rtype: bool
        """
        if self.rear == self.k:
            return False
        else:
            self.queue.append(value)
            self.rear = self.rear + 1
            return True
        

    def deleteFront(self):
        """
        Deletes an item from the front of Deque. Return true if the operation is successful.
        :rtype: bool
        """
        if self.front == self.rear:
            return False
        else:
            self.queue.pop(0)
            self.rear = self.rear - 1
            return True
        
        

    def deleteLast(self):
        """
        Deletes an item from the rear of Deque. Return true if the operation is successful.
        :rtype: bool
        """
        if self.front == self.rear:
            return False
        else:
            self.queue.pop(len(self.queue)-1)
            self.rear = self.rear - 1
            return True
        

    def getFront(self):
        """
        Get the front item from the deque.
        :rtype: int
        """
        if self.front == self.rear:
            return -1
        else:
            return self.queue[self.front]
        

    def getRear(self):
        """
        Get the last item from the deque.
        :rtype: int
        """
        if self.front == self.rear:
            return -1
        else:
            return self.queue[self.rear-1]
        

    def isEmpty(self):
        """
        Checks whether the circular deque is empty or not.
        :rtype: bool
        """
        if self.front == self.rear:
            return True
        else:
            return False

    def isFull(self):
        """
        Checks whether the circular deque is full or not.
        :rtype: bool
        """
        if self.rear == self.k:
            return True
        else:
            False
        


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()