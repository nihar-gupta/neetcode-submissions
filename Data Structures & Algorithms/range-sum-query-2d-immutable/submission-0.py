class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.a = matrix
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        minR = min(row1, row2)
        maxR = max(row1, row2)
        minC = min(col1, col2)
        maxC = max(col1, col2)

        ans = 0
        for i in range(minR, maxR+1):
            for j in range(minC, maxC+1):
                ans += self.a[i][j]
        
        return ans
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)