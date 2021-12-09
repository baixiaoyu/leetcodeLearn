def binarySearch(alist,item):
    if len(alist) ==0:
        return False
    else:
        mid = len(alist)//2
        if alist[mid] == item:
            return True
        else:

            if alist[mid] > item:
                return binarySearch(alist[:mid],item)
            else:
                return binarySearch(alist[mid:],item)
        
