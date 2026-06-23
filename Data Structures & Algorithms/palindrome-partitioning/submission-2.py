class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res=[]
        def ispali(s,l,r):
            while l<r:
                if s[l]!=s[r]:
                    return False
                l+=1
                r-=1
            return True

        def dfs(path,start):
            if start==len(s):
                res.append(path[:])
                return

            for i in range(start,len(s)):
                if ispali(s,start,i):
                    path.append(s[start:i+1])
                    dfs(path,i+1)
                    path.pop()
        dfs([],0)
        return res

        


