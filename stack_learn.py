class MyQueue(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.l = []


    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: None
        """
        self.l.append(x)


    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        x = self.l[0]
        del self.l[0]
        return x

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        if len(self.l) == 0:
            return -1
        return self.l[0]

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return 0 == len(self.l)


# Your MyQueue object will be instantiated and called as such:
obj = MyQueue()
x=11
obj.push(x)
param_2 = obj.pop()
param_3 = obj.peek()
param_4 = obj.empty()


nums1 = [4,1,2]
nums2 =  [1,3,4,2]

for p1,v1 in enumerate(nums2[3:]):
    print(p1,v1)
    res = []
    flag = False
    for pos,val in enumerate(nums1):
        p  = nums2.index(val)
        print(p)

        for n2p,n2v in enumerate(nums2[p:]):
            if n2v > val:
                flag = True
                res.append(n2v)
                break
        if flag:
            pass
        else:
            res.append(-1)
        flag = False
    print(res)

from collections import *
# s = "3[a]2[bc]"
# "aaabcbc"
def decodeString(s):
    stack = []
    num = 0
    res = ""
    for c in s:
        if c.isdigit():
            num = num * 10 + int(c)
        elif c == "[":
            stack.append((res, num))
            print(stack)
            res, num = "", 0
        elif c == "]":
            top = stack.pop()
            res = top[0] + res * top[1]
        else:
            res += c
    print(res)
    return res
s = "3[a2[c]]"
#s="2[abc]3[cd]ef"

decodeString(s)

str = "babx"
print(str*2)


def calPoints( ops):
    """
    :type ops: List[str]
    :rtype: int
    """
    stack = []
    for i in ops:
        flag = False
        if i.startswith('-'):
            i  = i[1:]
            flag = True

        if i.isdigit():
            print(i)
            if flag:
                i='-'+i
            stack.append(i)
        if i == 'C':
            stack.pop()
        if i == 'D':
            var = int(stack[-1])
            stack.append(2*var)
        if i == "+":
            var = int(stack[-1]) + int(stack[-2])
            stack.append(var)
    sum = 0
    for j in stack:
        sum = sum+int(j)

    print(sum)
ops = ["5","2","C","D","+"]
ops = ["5","-2","4","C","D","9","+","+"]
ops = ["1"]
calPoints(ops)


l1=  [1,2,3]
l2 = [4,5,6]
print(sum(l1+l2))

a=2
b=3
print(a^b)
