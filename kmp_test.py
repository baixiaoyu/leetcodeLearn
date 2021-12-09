#!/usr/bin/env python
# coding: utf-8
class Solution:
    def prefix_table2(self,pattern,m):
        prefix = [0] * m
        j =  1
        prefix[0] = -1    #i也是下标，按下标好理解
        while j<m:
            i = prefix[j-1]
            while(i>=0 and pattern[len+1] != pattern[j]):
                i = prefix[i]
            if pattern[i+1] == pattern[j]:
                prefix[j] = i+1
            else:
                prefix[j] = -1
            j = j +1
        print(prefix)
        return prefix

    def kmp2(self,str,pattern):
        n = len(str)
        m = len(pattern)
        s,p = 0,0
        prefix = self.prefix_table2(pattern,m)
        while(s < n and p<m):
            if str[s] == pattern[p] :
                s = s+1
                p=p+1
            elif p>0:
                p = prefix[p-1] +1
            else:
                s = s +1
        if p==m:
            print("found")
            print(s-m)
        else:
            print("no found")



    def prefix_table(self,pattern,n):

        prefix = [0]*n
        len = 0
        i =1
        while i < n:
            print("i",i)
            if pattern[i]==pattern[len]:
                len = len+1
                prefix[i] = len
                i = i + 1
            else:#这个分支比较难理解
                if(len>0):
                    len = prefix[len-1]
                else:
                    prefix[i]=len
                    i=i+1


        print("prefix",prefix)
        return prefix

    def move_table(self,alist):
        n = len(alist)
        i = n-1

        while i >0:
            alist[i]=alist[i-1]
            i = i -1
        alist[0] = -1
        return alist

    def kmp(self,text,pattern):
        m = len(text)
        n = len(pattern)
        i ,j =0,0
        prefix_table = self.prefix_table(pattern, n)
        prefix_table = self.move_table(prefix_table)
        print(prefix_table)
        print(m)

        while i < m :
            print("i:",i)
            print("j:",j)
            if j == n-1 and pattern[j] == text[i]:
                print("found ",i-j)
                j = prefix_table[j] #注意这个，匹配上了，继续，就当没匹配一样，继续遍历

            if text[i] == pattern[j] :
                i = i+1
                j = j+1
            else:
                j=prefix_table[j]
                if j == -1:
                    i = i+1
                    j = 0
        print("end")

s = Solution()
text = 'acabaabaabcacaabaabcac'
pattern =   'abaabcac'
#s.kmp(text,pattern)
s.kmp2(text,pattern)
# pattern = "ababa"
# n = len(pattern)
# prefix = prefix_table(pattern,n)
# prefix_table = move_table(prefix)
# print(prefix_table)


str1 = "this is string example....wow!!!";
str2 = "exam";

print str1.index(str2);

