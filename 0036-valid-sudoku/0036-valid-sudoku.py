
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        rowMap=[set() for _ in range(9)]
        colMap=[set() for _ in range(9)]
        boxMap=[set() for _ in range(9)]

        for i in range(9):
            for j in range(9):
                currEle = board[i][j]
                if (currEle == "."): 
                    continue
                if(currEle in rowMap[i] or currEle in colMap[j] or currEle in boxMap[(i//3)*3 + j//3]):
                    return False
                
                rowMap[i].add(currEle)
                colMap[j].add(currEle)
                boxMap[(i//3)*3 + j//3].add(currEle)
        return True



