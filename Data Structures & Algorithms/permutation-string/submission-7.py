class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False
        word1=defaultdict(int)
        word2=defaultdict(int)
        for i in range(len(s1)):
            word1[s1[i]]+=1
            word2[s2[i]]+=1
        l=0
        for r in range(len(s1),len(s2)):
            if word1==word2:
                return True
            word2[s2[r]]+=1
            word2[s2[l]]-=1
            if word2[s2[l]]==0:
                del word2[s2[l]]
            l+=1
        return word1==word2
    
        