# coding=utf-8
# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import copy
import math

from link_learn import *
def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print("Hi, {0}".format(name))  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.

def FindGreatestSumOfSubArray(array):
    # write code here
    k = {}
    i = 1
    alen = len(array)
    dp = [0] * alen
    dp[0] = array[0]
    j = 1
    k[dp[0]] = [array[0]]
    q = 1
    while i < alen:
        # dp[i] = max(dp[i-1] + array[i],array[i])
        if (dp[i - 1] + array[i]) > array[i]:
            dp[i] = dp[i - 1] + array[i]
            tp = copy.deepcopy(k[dp[i-1]])
            tp.append(array[i])
            k[dp[i]]=tp
        else:
            dp[i] = array[i]
            k[dp[i]] = [array[i]]
        i = i + 1
    print("dp",dp)
    print("k",k)
    res = []
    m = float('-inf')
    for i in dp:
        if i> m:
            m=i
            res = k[i]

    return res

if __name__ == '__main__':
    [1, 2, -3, 4, -1, 1]
    array = [1,2,-3,4,-1,1,-3,2]
    res =FindGreatestSumOfSubArray(array)
    print(res)
    # dict = {1: 'Zara', 'Age': 7, 'Class': 'First'}
    # s = 1
    # print(dict[s])
    # l = [1,3,4]
    # res =[]
    # res.append(l)
    # print(res)
    #
    #
    # print_hi('PyCharm' for _ in range(10))
    # j = 2
    # i=7
    # print(2**2)
    # print(7.0/4)
    # print(7/2**2)
    # print(math.ceil((i // 2 ** j)))
    # min = math.ceil((i / 2 ** j)) + j
    # print("min",min)
    # k=2
    # n=1
    # dp = [[0] * (n + 1) for _ in range(k + 1)]
    # print(dp)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
#
#     node1 = ListNode(1)
#     node2 = ListNode(2)
#     node3 = ListNode(3)
#     node4 = ListNode(4)
#     node5 = ListNode(5)
#
#     node1.next = node2
#     node2.next = node3
#     node3.next = node4
#     node4.next = node5
#
#     test = Solution()
    # test.printList(node1)
    # print('===')
    # rev = test.reverseList(node1)
   # test.printList(node1)
    #test.printList(node1)
    # test.printList(test.rotateRight(node1,2))