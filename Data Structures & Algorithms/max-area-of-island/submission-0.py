from collections import deque
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def valid(x, y):
            n = len(grid)
            m = len(grid[0])
            return x>=0 and y>=0 and x<n and y<m
        n = len(grid)
        m = len(grid[0])
        vis = [[False for i in range(m)] for j in range(n)]

        q = deque()
        ans = 0

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1 and vis[i][j] is False:
                    cur_ans = 0
                    q.append([i,j])
                    vis[i][j] = True

                    while len(q) > 0:
                        x, y = q.popleft()
                        cur_ans += 1
                        next_points = [[x-1, y], [x+1,y], [x, y+1], [x, y-1]]
                        for nx, ny in next_points:
                            if valid(nx, ny) and grid[nx][ny] == 1 and vis[nx][ny] is False:
                                vis[nx][ny] = True
                                q.append([nx,ny])
                    ans = max(ans, cur_ans)
        return ans
                        

        