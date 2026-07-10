class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prices=[float('infinity')]*n
        prices[src]=0

        for i in range(k+1):
            temp=prices.copy()
            for s,d,p in flights:
                prices[d]=min(prices[d],temp[s]+p)
        if prices[dst]==float('infinity'):
            return -1
        else:
            return prices[dst]
            
