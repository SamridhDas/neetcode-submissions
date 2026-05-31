class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowcheck={}
        for i in range(9):
            for j in range(9):
                if board[i][j]==".":
                    continue
                rowcheck[board[i][j]]=1+rowcheck.get(board[i][j],0)
                if rowcheck[board[i][j]]>1:
                    return False
            rowcheck.clear()


       
        

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
        for row in range(0,9,3):
            for col in range(0,9,3):
                boxcheck={}
                for i in range(3):
                    for j in range(3):
                        
                        val=board[row+i][col+j]
                        if val==".":
                            continue
                        if val in boxcheck:
                            return False
                        boxcheck[val]=1
                boxcheck.clear()
        return True




                


        