class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        d = {}
        for i in board:
            for j in i:
                if j==".":
                    continue
                else:
                    d[j] = d.get(j, 0) + 1
            for k in list(d.values()):
                if k>1:
                    return False
            d = {}
        d = {}
        for i in range(len(board[0])):
            for j in board:
                if j[i] == ".":
                    continue
                else:
                    d[j[i]] = d.get(j[i], 0) + 1
            for k in list(d.values()):
                if k>1:
                    return False
            d = {}
        d = {}
        i = 0
        j = 0
        for row in range(0,9,3):
            for col in range(0,9,3):
                d = {}

                for i in range(row, row+3):
                    for j in range(col, col+3):
                        if board[i][j] == ".":
                            continue
                        else:
                            d[board[i][j]] = d.get(board[i][j], 0) + 1
                for k in d.values():
                    if k>1:
                        return False
        return True