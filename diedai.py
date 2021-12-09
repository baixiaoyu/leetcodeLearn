def subsetXORSum( nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    candidates = [0]
    for x in nums:
        candidates += [x ^ y for y in candidates]
    return sum(candidates)

nums = [5,1,6]
print(sum(nums))
a=subsetXORSum(nums)
print(a)

#recMC([1,5,10,25], 63)
def recMC(coinValueList, charge):
    minCoins = 999999
    if charge in coinValueList:
        return 1
    for i in [c for c in coinValueList if c <= charge]:
        numCoins = 1+recMC(coinValueList,charge-i)
        if numCoins < minCoins:
            minCoins = numCoins
    return minCoins



def recMC2(coinValueList, charge, knownResults):
    minCoins = 999999
    if charge in coinValueList:
        knownResults[charge] =1
        return 1
    elif knownResults[charge] > 0:
        return knownResults[charge]
    for i in [c for c in coinValueList if c <= charge]:
        numCoins = 1+recMC(coinValueList,charge-i)
        if numCoins < minCoins:
            minCoins = numCoins
            knownResults[charge] = minCoins
    return minCoins

#recMC([1,5,10,25], 63)

def dpcharge(coinValueList, charge):
    minlist = [charge]*(charge+1)
    coinused = [0]*(charge+1)
    print(minlist)
    for cent in range(charge+1):
        print("cent:",cent)
        mincount = cent
        newcoin = 1
        for i in [c for c in coinValueList if c <= cent]:
            if minlist[cent-i] +1 <mincount:
                mincount= minlist[cent-i] +1
                newcoin = i
        minlist[cent] = mincount
        coinused[cent] = newcoin
    print("minlist:",minlist)
    print("coinused:", coinused)
    return minlist[charge]

print(dpcharge([1,5,10,25], 11))

