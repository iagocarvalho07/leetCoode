"""
28. Find the Index of the First Occurrence in a String
Easy
Topics
Companies
Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

 

Example 1:

Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.
Example 2:

Input: haystack = "leetcode", needle = "leeto"
Output: -1
Explanation: "leeto" did not occur in "leetcode", so we return -1.

"""

"""
este video pode ajudar : 
https://www.youtube.com/watch?v=0iDiUuHZE_g



Solução alternativa: muito mais enxuta que a minha por sinal 
class Solution(object):
    def strStr(self, haystack, needle):
        x = len(needle)
        for i in range(0,len(haystack)):
            if haystack[i:i+x] == needle: 
                return i
        return -1

"""

class Solution(object):
    def strStr(self, haystack, needle):
        lps = [0] * len(needle)
        pre = 0
        for i in range(1, len(needle)):
            while pre > 0 and needle[i] != needle[pre]:
                pre = lps[pre-1]
            if needle[pre] == needle[i]:
                pre += 1
                lps[i] = pre

        n = 0 
        for h in range(len(haystack)):
            while n > 0 and needle[n] != haystack[h]:
                n = lps[n-1]
            if needle[n] == haystack[h]:
                n += 1
            if n == len(needle):
                return h - n + 1

        return -1
