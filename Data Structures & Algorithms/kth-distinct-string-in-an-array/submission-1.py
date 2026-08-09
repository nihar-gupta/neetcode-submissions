class Solution:
    def kthDistinct(self, a: List[str], k: int) -> str:
        n = len(a)
        if k>n: return ""
        d = dict()
        for i in a: d[i] = d.get(i, 0)+1

        for i,j in d.items():
            if j==1: 
                k -= 1
                if k==0: return i
        return ""

        # for i in a:
        #     if d[i] == 1:
        #         k -= 1
        #         if k==0: return i
        # return ""
        