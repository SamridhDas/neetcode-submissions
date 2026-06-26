class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trusty={}
        trusted={}

        for a,b in trust:
            trusty[a]=1+trusty.get(a,0)
            trusted[b]=1+trusted.get(b,0)
        for i in range(1,n+1):
            if trusty.get(i,0)==0 and trusted.get(i,0)==n-1:
                return i
        return -1