# 散列函数一般都是取余，可以改变取余时候的计算方法，一种是折叠 2个一组，然后相加，或者隔一个反转下，一种是平方取中，平方数，然后取中间2个，字符串是用对应的数值相加，然后取余。
#hash冲突的处理，1 线性探测，开放定址 在冲突后，可以找后面是空的槽，放进去，或者跳过几个槽，在放进去，2 再散列 在散列函数，平方探测，如果散列值是h,以后就是h+4 h+9 h+16
#链接法，冲突的值用链表串联起来。

class HashTable:
    def __init__(self):
        self.size = 11
        self.slots = [None] * self.size
        self.data = [None] * self.size

    def put(self, key, data):
        hashvalue = self.hashfunction(key, len(self.slots))

        if self.slots[hashvalue] == None:
            self.slots[hashvalue] = key
            self.data[hashvalue] = data

        else: #没有判断data的冲突吗，不需要判断data，就是按key 来的， data就是key的复制品
            nextslot = self.rehash(hashvalue, len(self.slots))
            while self.slots[nextslot] != None and self.slots[nextslot] != key:
                nextslot = self.rehash(nextslot, len(self.slots))

            if self.slots[nextslot] == None:
                self.slots[nextslot] = key
                self.data[nextslot] = data
            else:
                self.data[nextslot] = data

    def hashfunction(self, key, size):
        return key%size

    def rehash(self, oldhash, size):
        return (oldhash +1)%size

    def get(self, key):
        startslot = self.hashfunction(key, len(self.slots))

        data = None
        stop = False
        found = False
        position = startslot

        while self.slots[position] != None and not found and not stop:
            if self.slots[position] == key:
                found = True
                data = self.data[position]
            else:
                position=self.rehash(position, len(self.slots))
                if position == startslot:
                    stop = True
        return data

    def __getitem__(self, item):
        return self.get(item)

    def __setitem__(self, key, value):
        self.put(key, value)

H = HashTable()
H[54] = "cat"
H[26] = "dog"
H[93] = "lion"
H[17] = "tiger"
H[77] = "bird"
H[31] = "cow"
H[44] = "goat"
H[55] = "pig"
H[20] = "chicken"
print(H.slots)
print(H.data)

