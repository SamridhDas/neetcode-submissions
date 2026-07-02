class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        hashmap=defaultdict(list)
        for word in strs:
            freq=[0]*26
            for c in word:
                freq[ord(c)-ord('a')]+=1
            
            hashmap[tuple(freq)].append(word)
            
        res=[]
        for key in hashmap:
            res.append(hashmap[key])
        return res