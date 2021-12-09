class MyCircularDeque(object):

    def __init__(self, k):
        """
        Initialize your data structure here. Set the size of the deque to be k.
        :type k: int
        """
       # self.q = k * [None]
        self.q = []
        self.size = k

    def insertFront(self, value):
        """
        Adds an item at the front of Deque. Return true if the operation is successful.
        :type value: int
        :rtype: bool
        """
        try:
            if self.isFull():
                return False
            self.q.insert(0, value)
            return True
        except Exception as e:
            return False

    def insertLast(self, value):
        """
        Adds an item at the rear of Deque. Return true if the operation is successful.
        :type value: int
        :rtype: bool
        """
        try:
            if self.isFull():
                return False
            self.q.append(value)
            return True
        except Exception as e:
            return False

    def deleteFront(self):
        """
        Deletes an item from the front of Deque. Return true if the operation is successful.
        :rtype: bool
        """
        try:
            if self.isEmpty():
                return False
            self.q.pop(0)
            return True
        except Exception as e:
            return False

    def deleteLast(self):
        """
        Deletes an item from the rear of Deque. Return true if the operation is successful.
        :rtype: bool
        """
        try:
            if self.isEmpty():
                return False
            self.q.pop()
            return True
        except Exception as e:
            return False

    def getFront(self):
        """
        Get the front item from the deque.
        :rtype: int
        """
        if len(self.q) == 0:
            return -1
        else:
            return self.q[0]

    def getRear(self):
        """
        Get the last item from the deque.
        :rtype: int
        """
        if len(self.q) == 0:
            return -1
        else:
            return self.q[-1]

    def isEmpty(self):
        """
        Checks whether the circular deque is empty or not.
        :rtype: bool
        """
        return len(self.q) == 0

    def isFull(self):
        """
        Checks whether the circular deque is full or not.
        :rtype: bool
        """
        print(self.q)
        print(self.size)
        return len(self.q) >= self.size

# Your MyCircularDeque object will be instantiated and called as such:
obj = MyCircularDeque(3)

param_2 = obj.insertLast(1)
param_3 = obj.insertLast(2)
param_4 = obj.insertFront(3)
param_5 = obj.insertFront(4)
param_6 = obj.getRear()
param_7 = obj.isFull()
param_8 = obj.deleteLast()
param_9 = obj.insertFront(4)
param_10 = obj.getFront()
print(param_2,param_3,param_4,param_5,param_6,param_7,param_8,param_9,param_10)
#[null,true,true,true,false,2,true,true,true,4]