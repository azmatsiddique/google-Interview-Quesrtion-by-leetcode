#
# @lc app=leetcode id=289 lang=python3
#
# [289] Game of Life
#

# @lc code=start
class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        ind = []
        n_row = len(board)
        n_col = len(board[0])
        direction=[[1,0], [-1,0], [0,1], [0,-1], [1,1], [1,-1], [-1,-1], [-1, 1] ]
        for i in range(n_row):
            for j in range(n_col):
                cnt = 0
                for x,y in direction:
                    i0, j0 = i+x, j+y
                    if i0<0 or i0>=n_row or j0<0 or j0>=n_col:
                        continue
                    if board[i0][j0]:
                        cnt += 1
                if board[i][j]:
                    if cnt < 2 or cnt > 3:
                        ind.append([i, j])
                else:
                    if cnt == 3:
                        ind.append([i, j])
        for x,y in ind:
            board[x][y] = 1-board[x][y]
        return

        
# @lc code=end

