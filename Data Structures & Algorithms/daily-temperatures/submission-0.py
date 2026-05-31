class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res=[0]*len(temperatures)
      
        for i,temp in enumerate(temperatures):
          count=0
          left=i+1
          
          while(left<len(temperatures)):
            count+=1
            if temperatures[left]>temp:
                res[i]=count
                break
                
            left+=1
            
          

        return res



            

        