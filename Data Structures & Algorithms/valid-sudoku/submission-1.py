class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            row_seen  = set() 
            for j in range(9):
                if i % 3 == 0 and j % 3 == 0:
                    box_seen = set()
                    for sr in range(i,i+3):
                        for sc in range (j,j+3):
                            if board[sr][sc] != '.':
                                if board[sr][sc] in box_seen:
                                    return False
                                else:
                                    box_seen.add(board[sr][sc])
                if board[i][j] != '.':
                    if board[i][j] in row_seen:
                        return False
                    else:
                        row_seen.add(board[i][j])
        for i in range(9):
            column_seen = set()
            for j in range(9):
                if board[j][i] != '.':
                    if board[j][i] in column_seen:
                        return False
                    else:
                        column_seen.add(board[j][i])
        return True
                