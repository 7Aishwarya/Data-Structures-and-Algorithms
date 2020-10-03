class MyCircularQueue(object):

    def __init__(self, k):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        :type k: int
        """
        self.queue = []
        self.front = self.rear = 0
        self.k = k
        

    def enQueue(self, value):
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        :type value: int
        :rtype: bool
        """
        if self.rear == self.k:
            return False
        else:
            self.queue.append(value)
            self.rear = self.rear + 1
            return True
        

    def deQueue(self):
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        :rtype: bool
        """
        if self.front == self.rear:
            return False
        else:
            self.queue.pop(0)
            self.rear = self.rear - 1
            return True
        

    def Front(self):
        """
        Get the front item from the queue.
        :rtype: int
        """
        if self.front == self.rear:
            return -1
        else:
            return self.queue[self.front]
        

    def Rear(self):
        """
        Get the last item from the queue.
        :rtype: int
        """
        if self.front == self.rear:
            return -1
        else:
            return self.queue[self.rear-1]
        

    def isEmpty(self):
        """
        Checks whether the circular queue is empty or not.
        :rtype: bool
        """
        if self.front == self.rear:
            return True
        else:
            return False
        

    def isFull(self):
        """
        Checks whether the circular queue is full or not.
        :rtype: bool
        """
        if self.rear == self.k:
            return True
        else:
            return False
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()