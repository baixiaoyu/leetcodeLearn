from wasabi import wrap


def encrypt(m):
    s = 'abcdefghijklmnopqrstuvwxyz'
    n = ''
    for i in m:
        j = (s.find(i) +4)%26
        n = n +s[j]
    return n

print(encrypt("a"))

def toStr(n,base):
    convertString ="0123456789ABCDEF"

    if n < base:
        return convertString[n]
    else:
        return toStr(n//base, base) + convertString[n%base]

print(toStr(768,16))

s="3[a]2[bc]"
print(s[4])
print(s[6:8])

print("yy"*3)

def decodeString( s):
    start = s.rfind("[")
    if start <= 0:
        return s
    end = s.find("]", start)
    print("start", start)
    print("end", end)
    temp = s[start + 1:end]
    ss = s[:start ]
    print("ss",ss)
    c = len(ss)
    num=""
    counter = 0
    while c > 0:
        print("c",ss[c-1])
        if ss[c-1].isdigit():

            num = num + ss[c-1]

            counter = counter+1
        else:
            break
        c = c - 1
    num = int(num[::-1])
    #num = int(s[start - 1])
    print("num", num)
    print("temp", temp)

    temp = temp * num
    temp = temp + s[end + 1:]
    print("before s1,temp",temp)
    s1 = s[:start - counter] + temp
    print("s1",s1)
    return decodeString(s1)

s="3[a]2[bc]"
print(decodeString(s))
#
# s = "abc"
# print(s[-1])

title = "FLUSH TABLES WITH READ LOCK is waiting for a global read lock or the global read_only system variable is being set."
title = wrap(title, wrap_max=200,indent=0)
print(title)