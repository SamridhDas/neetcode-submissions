class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False
        count1={i:0 for i in range(26)}
        count2={i:0 for i in range(26)}

        for i in range (len(s1)):
            count1[ord(s1[i])-ord('a')]=1+count1.get(ord(s1[i])-ord('a'),0)
            count2[ord(s2[i])-ord('a')]=1+count2.get(ord(s2[i])-ord('a'),0)
        
        l=0
        for i in range(len(s1),len(s2)):
            if count1==count2:
                return True
            count2[ord(s2[i])-ord('a')]=1+count2.get(ord(s2[i])-ord('a'),0)
            count2[ord(s2[l])-ord('a')]=count2[ord(s2[l])-ord('a')]-1
            l+=1

        return count1==count2
