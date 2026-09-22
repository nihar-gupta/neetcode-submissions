class Solution:
    def getRow(self, n: int) -> List[int]:
        if n==0: return [1]
        if n==1: return [1,1]

        k = [[1], [1,1]]
        for i in range(2, n+1):
            p = []
            for j in range(i+1):
                if j==0 or j==i:
                    p.append(1)
                else:
                    p.append(k[-1][j-1]+k[-1][j])
            k.append(p)
        return k[-1]
        