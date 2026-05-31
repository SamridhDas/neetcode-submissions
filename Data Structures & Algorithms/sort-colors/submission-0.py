class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def mergesort(arr,l,r):
            if l==r:
                return arr
            m=(l+r)//2
            mergesort(arr,l,m)
            mergesort(arr,m+1,r)
            merge(arr,l,m,r)
        def merge(arr,l,m,r):
            left,right=arr[l:m+1],arr[m+1:r+1]
            i,j,k=l,0,0
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
                j+=1
                i+=1
            while k<len(right):
                arr[i]=right[k]
                i+=1
                k+=1
        mergesort(nums,0,len(nums)-1)

            