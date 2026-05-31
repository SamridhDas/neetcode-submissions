class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        res=[]
        
        for a in asteroids:
            destroy=0
            while res and res[-1]>0 and a<0:
                if abs(res[-1])<abs(a):
                    res.pop()
                    
                elif abs(res[-1])==abs(a):
                    a=0
                    res.pop()
                else:
                    a=0
                    

               
            if a:
                res.append(a)
        return res
                        
                


