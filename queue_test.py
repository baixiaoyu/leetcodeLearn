from functools import cmp_to_key


class Queue:
    def __init__(self):
        self.size = 0
        self.list = []

    def enqueue(self,e):
        self.list.insert(0,e)

    def dequeue(self):
        e = self.list.pop()
        return e
    def length(self):
        return len(self.list)

    def isEmpty(self):
        return self.list == []


alist = [1,2,3,4,5,6,7]
print(alist[3:7])

for i in range(2):
    print(i)


def largestNumber( nums):
    n = len(nums)
    nums = list(map(str, nums))
    print(nums)
    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] + nums[j] < nums[j] + nums[i]:
                nums[i], nums[j] = nums[j], nums[i]
    print(nums)
    return str(int("".join(nums)))


nums = [3,30,34,5,9]

print(largestNumber(nums))


def largestNumber3(nums):
    def cmp(x, y):
        return 1 if x + y < y + x else -1

    nums = list(map(str, nums))
    nums.sort(key=cmp_to_key(cmp))
    res = str(int("".join(nums)))
    return res


def largestNumber2( nums) :
    def mycmp(x, y):

        return 1 if x + y < y + x else -1

    nums = list(map(str, nums))
    nums.sort(cmp=mycmp)
    #sorted(nums,key=cmp_to_key(mycmp))
    print("2")
    print(nums)
    res = str(int("".join(nums)))
    return res


print(largestNumber2(nums))