class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def MergeSort(arr,l,r):
            if l>=r:
                return 
            m=(l+r)//2
            MergeSort(arr,l,m)
            MergeSort(arr,m+1,r)
            Merge(arr,l,m,r)
            


        def Merge(arr,l,m,r):
            left,right=arr[l:m+1],arr[m+1:r+1]
            i=l
            j,k=0,0
            while j<len(left) and k<len(right):
                if left[j]<=right[k]:
                    arr[i]=left[j]
                    j+=1
                else:
                    arr[i]=right[k]
                    k+=1
                i+=1
            while j<len(left):
                arr[i]=left[j]
                i+=1
                j+=1
            while k<len(right):
                arr[i]=right[k]
                i+=1
                k+=1
        MergeSort(nums,0,len(nums)-1)  
        return nums