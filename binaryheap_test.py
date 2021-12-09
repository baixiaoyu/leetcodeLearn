import heapq


def smallest_queue(arr):
    """
    默认为最小优先队列
    """
    print("原数组：{0}".format(arr))
    # 将给定的列表转化为最小堆，线性时间
    heapq.heapify(arr)
    print("最小堆数组：{0}".format(arr))

    # 插入元素
    heapq.heappush(arr, 5)
    print("插入新元素后：{0}".format(arr))

    # 弹出最小元素
    item0 = heapq.heappop(arr)
    print("弹出的元素后：{0}".format(arr))

    # 返回最小元素
    item1 = arr[0]
    print("获取最小元素的值：{0}".format(item1))

    # 弹出最小元素，并插入一个新的元素，相当于先 heappop, 再 heappush
    item2 = heapq.heapreplace(arr, -2)
    print("弹出的元素为：{0}".format(item2))
    print("现在的堆结构为：{0}".format(arr))


class BinaryHeap:
    def __init__(self):
        self.heaplist = [0]
        self.currentSize = 0

    def insert(self, k):
        self.heaplist.append(k)
        self.currentSize = self.currentSize +1
        self.percUp(self.currentSize)

    def percUp(self, size):
        while size //2 > 0:
            if self.heaplist[size] < self.heaplist[size//2]:
                temp = self.heaplist[size//2]
                self.heaplist[size//2] = self.heaplist[size]
                self.heaplist[size] = temp
            size = size //2

    def delMin(self):
        retVal = self.heaplist[1]
        self.heaplist[1] = self.heaplist[self.currentSize]
        self.currentSize = self.currentSize -1
        self.heaplist.pop()
        self.percDown(1)
        return retVal

    def percDown(self,i):
        while (i*2) <= self.currentSize:
            mc = self.minChild(i)
            if self.heaplist[i] > self.heaplist[mc]:
                temp = self.heaplist[i]
                self.heaplist[i] = self.heaplist[mc]
                self.heaplist[mc] = temp
            i = mc

    def minChild(self,i):
        if i*2 +1 > self.currentSize:
            return i*2
        else:
            if self.heaplist[i*2] < self.heaplist[i*2+1]:
                return i*2
            else:
                return i*2+1

    def buildHeap(self,alist):
        i= len(alist)//2
        self.currentSize = len(alist)
        self.heaplist = [0] + alist

        while(i>0):
            self.percDown(i)
            i = i -1


