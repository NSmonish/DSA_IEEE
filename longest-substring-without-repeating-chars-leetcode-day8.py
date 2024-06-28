class Solution(object):
    def lengthOfLongestSubstring(self, s):
        l=0
        r=1
        final = 0
        for _ in s:
            while len(s[l:r]) != len(set(s[l:r])):
                l += 1
            final = max(len(s[l:r]), final)
            r+=1
        return final
