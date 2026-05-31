class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
     i=0
     j=0
     m=len(nums1)
     n=len(nums2)
     temp=[]
     for k in range(m+n):
        if i>=m or j>=n:
            break
        if nums1[i]>nums2[j]:
            temp.append(nums2[j])
            j+=1
        else:
            temp.append(nums1[i])
            i+=1

     while(i<m):
            temp.append(nums1[i])
            i+=1
     while(j<n):
            temp.append(nums2[j])
            j+=1
     
     if(m+n)%2!=0:
        return temp[(m+n)//2]
     else:
        return (temp[(m+n)//2]+temp[((m+n)//2)-1])/2
    
        


    

        
    
        