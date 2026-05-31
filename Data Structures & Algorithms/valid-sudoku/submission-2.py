class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #check all rows
        rowchecker={}
        for i in board:
            for j in i:
                if j==".":
                    continue
                rowchecker[j]=1+rowchecker.get(j,0)
                if rowchecker[j]>1:
                    return False
            rowchecker.clear()
        

        #check all columns
        columnchecker={}
        for j in range (9):
            for i in range (9):
                if board[i][j]==".":
                    continue
                columnchecker[board[i][j]]=1+columnchecker.get(board[i][j],0)
                if columnchecker[board[i][j]]>1:
                    return False
            columnchecker.clear()
        
        #3x3 checker
        for box_row in range (0,9,3):
            for box_col in range (0,9,3):
                boxchecker={}
                for i in range(3):
                    for j in range (3):
                        val=board[box_row+i][box_col+j]
                        if val==".":
                            continue
                        if val in boxchecker:
                            return False
                        boxchecker[val]=1
        return True


                


        