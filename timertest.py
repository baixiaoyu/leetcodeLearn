from timeit import Timer


def test1():
    l = []
    for i in range(1000):
        l = l+ [i]

t1 = Timer("test1", "from __main__ import test1")
print("concat",t1.timeit(number=1000), "milliseconds")

list = [2,3,4,67,2]
print(list[:-1])


def merge(nums1, m, nums2, n):
    """
    Do not return anything, modify nums1 in-place instead.
    """

    n1 = nums1[:m]
    n2 = nums2[:n]
    print(n1)
    print(n2)
    sorted = []

    p ,q = 0, 0

    while p <m or q<n:
        if p >=m:
            sorted.append(n2[q])
            q = q+1

        elif q >=n:
            sorted.append(n1[p])
            p = p+1

        else:
            if n1[p] < n2[q]:
                sorted.append(n1[p])
                p = p+1
            else:
                sorted.append(n2[q])
                q =q+1

    print("sorted",sorted)


nums1=[1,2,3,0,0,0]
m=3
nums2=[2,5,6]
n=3
merge(nums1,m,nums2,n)