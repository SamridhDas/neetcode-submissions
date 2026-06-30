class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if target=="0000":
            return 0
        visit=set(deadends)
        if "0000" in visit:
            return -1
        q=deque(["0000"])
        ans=0

        while q:
            ans+=1
            
            for i in range(len(q)):
                code=q.popleft()
                for j in range(4):
                    for k in [1,-1]:
                        digit=str((int(code[j])+k+10)%10)
                        next_code=code[:j]+digit+code[j+1:]
                        if next_code in visit:
                            continue
                        if next_code==target:
                            return ans
                        q.append(next_code)
                        visit.add(next_code)
        return -1