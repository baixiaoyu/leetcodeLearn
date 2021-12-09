
#coding=utf-8
from collections import Counter, OrderedDict

str = "abcbcaccbbad"
li = ["a","b","c","a","b","b"]
d = {"1":3, "3":2, "17":2}

print ("Counter(s):", Counter(str))
print ("Counter(li):", Counter(li))
print ("Counter(d):", Counter(d))


d1 = Counter(str)
print ("d1.most_common(2):",d1.most_common(2))

print ("sorted(d1.elements()):", sorted(d1.elements()))
print ('''("".join(d1.elements())):''',"".join(d1.elements()))



dic2 = OrderedDict()
dic2['a'] = '123'
dic2['b'] = 'jjj'
dic2['c'] = 'abc'
dic2['d'] = '999'
for k, v in dic2.iteritems():
    print('有序字典：%s:%s' %(k,v))




from collections import namedtuple

p = namedtuple("person", "name,age,sex")
print (type(p))

zhanglin = p("zhanglin",30,"male")
print(zhanglin)
print(zhanglin.name,zhanglin.age)