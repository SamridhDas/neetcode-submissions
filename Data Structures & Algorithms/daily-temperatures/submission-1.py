class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res=[0]*len(temperatures)
        stack=[] #store temp,index
      
        for i,temp in enumerate(temperatures):
            while stack and stack[-1][0]<temp:
               Stemp,Sindex= stack.pop()
               res[Sindex]=i-Sindex
            stack.append((temp,i))

        return res

        
            
          

        



            

        