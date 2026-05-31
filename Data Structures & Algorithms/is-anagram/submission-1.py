class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        words={}
        wordt={}
        for i in range(len(s)):
            words[s[i]]=1+words.get(s[i],0)
            wordt[t[i]]=1+wordt.get(t[i],0)

        if words==wordt:
            return True
        else:
            return False