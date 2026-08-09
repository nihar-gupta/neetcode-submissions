class Solution:
    def generate(self, n: int) -> List[List[int]]:
        if n == 0: return [[]]
        if n == 1: return [[1]]
        if n == 2: return [[1],[1,1]]

        rt = [[1],[1,1]]

        for i in range(2, n):
            rt.append([])
            for j in range(i+1):
                if j==0 or j==i:
                    rt[-1].append(1)
                else:
                    rt[-1].append(rt[-2][j-1]+rt[-2][j])
        
        return rt

    