class TimeMap:

    def __init__(self):
        self.hash=defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.hash[key].append((timestamp,value))

    def get(self, key: str, timestamp: int) -> str:
        res=""
        values=self.hash.get(key,[])
        values.sort()
        l,r=0,len(values)-1
        while l<=r:
            m=(l+r)//2
            if values[m][0]<=timestamp:
                res=values[m][1]
                l+=1
            else:
                r-=1
        return res
    
