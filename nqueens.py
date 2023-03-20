class Solution:
    def solveNQueens(self, n: int) -> list[list[str]]:
        col = set()
        postD = set() #r+c
        negD = set()  #r-c
        res = []
        board = [['.']*n for i in range(n)]
        print("Initializing the board ",board)
       

        def backtracking(r):
            if r == n: #this is the condition when you have a complete board 
                copy_board =  ["".join(row) for row in board]
                print("copying board..",copy_board)
                res.append(copy_board)
                print("final board",res)
                return res

            for c in range(n):
                if c in col or (r+c) in postD or (r-c)in negD:
                    continue
                col.add(c)
                postD.add(r+c)
                negD.add(r-c)
                board[r][c] = "Q"

                print(f"board before backtracking {c}",board)
                backtracking(r+1)

                col.remove(c)
                postD.remove(r+c)
                negD.remove(r-c)
                board[r][c] = "."

                print("board after backtracking",board)
        backtracking(0)
        return res

n = 4
sol = Solution()
fres = sol.solveNQueens(n)
print(fres)