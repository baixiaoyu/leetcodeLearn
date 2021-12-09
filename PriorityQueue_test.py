# coding=utf-8
from max_heap_test import *

class PriorityQueue(object):
    def __init__(self, maxsize):
        self.maxsize = maxsize
        self._maxheap = MaxHeap()

    def push(self, priority, value):
        # 注意这里把这个 tuple push 进去，python 比较 tuple 从第一个开始比较
        # 这样就很巧妙地实现了按照优先级排序
        entry = (priority, value)    # 入队的时候会根据 priority 维持堆的特性
        self._maxheap.add(entry)

    def pop(self, with_priority=False):
        entry = self._maxheap.extract()
        if with_priority:
            return entry
        else:
            return entry[1]

    def is_empty(self):
        return len(self._maxheap.l) == 0

def test_priority_queue():
    size = 5
    pq = PriorityQueue(size)
    pq.push(5, 'purple')    # priority, value
    pq.push(0, 'white')
    pq.push(3, 'orange')
    pq.push(1, 'black')

    res = []
    while not pq.is_empty():
        res.append(pq.pop())
    print res
test_priority_queue()




