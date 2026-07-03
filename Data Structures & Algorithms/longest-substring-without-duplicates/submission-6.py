class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window=set()
        l=0
        res=-float('infinity')
        for r in range(len(s)):
            while s[r] in window:
                res=max(len(window),res)
                window.remove(s[l])
                l+=1
            window.add(s[r])
        res=max(res,len(window))
        return res
