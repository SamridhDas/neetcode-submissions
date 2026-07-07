class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top=0
        bottom=len(matrix)-1
        while top<=bottom:
            m=(top+bottom)//2
            if matrix[m][0]==target:
                return True
            if matrix[m][0]>target:
                bottom-=1
            else:
                top+=1
        row=(top+bottom)//2
        l,r=0,len(matrix[0])-1
        while l<=r:
            m=(l+r)//2
            if matrix[row][m]==target:
                return True
            elif matrix[row][m]<target:
                l+=1
            else:
                r-=1
        return False
