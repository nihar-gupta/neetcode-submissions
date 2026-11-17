from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def valid(x, y):
            n = len(grid)
            m = len(grid[0])
            return x>=0 and y>=0 and x<n and y<m
            
        n = len(grid)
        m = len(grid[0])
        vis = [[False for i in range(m)] for j in range(n)]

        c = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == "1" and vis[i][j] is False:
                    c += 1
                    q = deque()
                    q.append([i,j])
                    vis[i][j] = True
                    while len(q) > 0:
                        x, y = q.popleft()
                        next_loc = [[x-1,y], [x+1,y], [x, y-1], [x, y+1]]
                        for nx, ny in next_loc:
                            if valid(nx, ny) and grid[nx][ny] == "1" and vis[nx][ny] is False:
                                vis[nx][ny] = True
                                q.append([nx, ny])
        return c