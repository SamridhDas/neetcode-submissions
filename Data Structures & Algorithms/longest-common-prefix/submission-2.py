class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        curr=0
        res=""
        while True:
            if curr>=len(strs[0]):
                return res
            
            
            letter=strs[0][curr]
            for s in strs:
                
                if curr>=len(s) or  s[curr]!=letter:
                    return res
            res+=letter
            curr+=1
        #return str(res)
            

