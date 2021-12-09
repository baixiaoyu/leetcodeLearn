
class MaxHeap:
    def __init__(self):
        self.l = []
        self._count = 0
    def __len(self):
        return self._count

    def add(self,value):
        self.l.append(value)
        self._count = self._count+1
        self._shiftup()

    def extract(self):

        if self._count<=0:
            raise Exception('empty')
        value = self.l[0]
        self._count = self._count - 1
        self._shiftdown(0)

        return value

    def _shiftup(self):
        pos = self._count-1

        parent = int((pos-1) / 2)
        while self.l[pos] > self.l[parent] and parent>=0:
            self.l[pos],self.l[parent] = self.l[parent],self.l[pos]
            pos = parent
            parent = int((pos - 1) / 2)

    def _shiftdown(self,idx):
        self.l[0] ,self.l[self._count]=self.l[self._count], self.l[0]
        self.l.pop()
        pos = 0
        left = 2 * pos + 1
        right = 2*pos +2


        while left <=self._count-1 and right <= self._count-1:

            if self.l[pos] < self.l[left] :
                self.l[pos],self.l[left] = self.l[left],self.l[pos]
                pos=left
                left = 2 * pos + 1
                right = 2 * pos + 2


            elif self.l[pos] < self.l[right] :
                self.l[pos], self.l[right] = self.l[right], self.l[pos]
                pos = right
                left = 2 * pos + 1
                right = 2 * pos + 2


def test_maxheap():
    import random
    n = 5
    h = MaxHeap()

    for i in range(5):
        h.add(i)
    print ("maxheap",h.l)
    for i in reversed(range(n)):
        # print(i)
        print(h.extract())
test_maxheap()


