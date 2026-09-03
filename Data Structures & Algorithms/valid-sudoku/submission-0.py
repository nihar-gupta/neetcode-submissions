class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def valid1(board):
            n = len(board)
            m = len(board[0])
            for i in range(n):
                vv = [0 for j in range(m+1)]
                for j in range(m):
                    if board[i][j] != ".":
                        if vv[int(board[i][j])] != 0 : return False
                        vv[int(board[i][j])] = 1
            return True
        
        def valid2(board):
            n = len(board)
            m = len(board[0])
            for j in range(m):
                vv = [0 for i in range(n+1)]
                for i in range(n):
                    if board[i][j] != ".":
                        if vv[int(board[i][j])] != 0 : return False
                        vv[int(board[i][j])] = 1
            return True

        def valid3(board):
            ppp = [[0,0], [0,3], [0,6], [3,0], [3,3], [3,6], [6,0], [6,3], [6,6]]

            for pp in ppp:
                ci = pp[0]
                cj = pp[1]
                vv = [0 for i in range(10)]
                for i in range(ci, ci+3):
                    for j in range(cj, cj+3):
                        if board[i][j] != ".":
                            if vv[int(board[i][j])] != 0 : return False
                            vv[int(board[i][j])] = 1
            return True

                        

        


                


        k = valid1(board)
        if k==False: return False
        k = valid2(board)
        if k==False: return False
        k = valid3(board)
        if k==False: return False
        return True
        