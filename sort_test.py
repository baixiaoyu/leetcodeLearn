def bubbleSort1(alist):
    for sortnum in range(len(alist)-1,0,-1):
        for i in range(sortnum):
            print(i)
            if alist[i] > alist[i+1]:
                temp=alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp

alist = [14,24,5,34,25,54,2,56,98,53]
bubbleSort1(alist)
print(alist)

def  bubbleSort2(alist):
    sortnum = len(alist)-1
    while sortnum > 0:
        for i in range(sortnum):
            if   alist[i] > alist[i+1]:
                temp=alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp
        sortnum = sortnum -1


alist = [14,24,5,34,25,54,2,56,98,53]
bubbleSort2(alist)
print(alist)

def  shortbubbleSort(alist):
    exchanges = True
    sortnum = len(alist)-1
    while sortnum > 0 and exchanges:
        exchanges = False
        for i in range(sortnum):
            if   alist[i] > alist[i+1]:
                exchanges = True
                temp=alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp
        sortnum = sortnum -1


alist = [14,24,5,34,25,54,2,56,98,53]

shortbubbleSort(alist)
print("short bubble sort")
print(alist)


def  selectionSort(alist):
    sortnum = len(alist)-1
    while sortnum > 0:
        max_index = 0
        for i in range(1,sortnum+1):
            if alist[i] > alist[max_index]:
                max_index = i
        temp = alist[sortnum]
        alist[sortnum] = alist[max_index]
        alist[max_index] = temp
        sortnum = sortnum -1

alist = [14,24,5,34,25,54,2,56,98,53]
selectionSort(alist)
print("selection sort")
print(alist)

print([x for x  in range(1,10)])
print([x for x  in range(10,0,-1)])

def insertionSort(alist):
    for i in range(1,len(alist)):
        currentvalue = alist[i]
        position =i
        while position > 0 and  currentvalue < alist[position-1]:
                alist[position] = alist[position-1]
                position = position -1
        alist[position]  = currentvalue

alist = [14,24,5,34,25,54,2,56,98,53]
insertionSort(alist)
print("insert sort")
print(alist)


def shellSort(alist):
    sublistcount = len(alist)//2
    while sublistcount > 0:
        for startposition in range(sublistcount):
            gapInsertionSort(alist,startposition, sublistcount)

        print("after incremetns of size", sublistcount, "the list is", alist)

        sublistcount = sublistcount //2

def gapInsertionSort(alist, start,gap):
    for i in range(start+gap, len(alist), gap):
        currentvalue = alist[i]
        position = i
        while position>=gap and alist[position-gap] > currentvalue:
            alist[position] = alist[position-gap]
            position = position - gap
        alist[position] = currentvalue

alist = [54,26,93,17,77,31,44,55,20]
print("shell sort")
#shell sort是把列表分段，然后进行的插入排序
shellSort(alist)

def mergeSort(alist):
    if len(alist) > 1:
        mid = len(alist)//2
        left = alist[:mid]
        right = alist[mid:]

        mergeSort(left)
        mergeSort(right)

        i = 0
        j = 0
        k = 0
        while i< len(left) and j < len(right):
            if left[i] < right[j]:
                alist[k] = left[i]
                i = i+1
            else:
                alist[k] = right[j]
                j = j +1
            k = k +1

        while i < len(left):
            alist[k] = left[i]
            i = i +1
            k = k +1
        while j< len(right):
            alist[k] = right[j]
            j = j +1
            k = k+1
alist = [54,26,93,17,77,31,44,55,20]
print("mergesort")
mergeSort(alist)
print(alist)


def quickSort(alist):
    quickSortHelper(alist,0,len(alist) -1)

def quickSortHelper(alist, first,last):
    if first<last:
        splitpoint = partition(alist,first,last)

        quickSortHelper(alist,first, splitpoint-1)
        quickSortHelper(alist,splitpoint+1,last)

def partition(alist,first,last):
    pivotvalue = alist[first]

    leftmark = first +1
    rightmark = last

    while rightmark>=leftmark:
        while leftmark<=rightmark and alist[leftmark] <=pivotvalue:
            leftmark = leftmark +1
        while leftmark<=rightmark and alist[rightmark] >=pivotvalue:
            rightmark = rightmark -1

        if rightmark >= leftmark:

            temp = alist[leftmark]
            alist[leftmark] = alist[rightmark]
            alist[rightmark] = temp

    temp = alist[first]
    alist[first] = alist[rightmark]
    alist[rightmark] = temp

    return rightmark
alist = [54,26,93,17,77,31,44,55,20]
print("quicksort")
quickSort(alist)
print(alist)