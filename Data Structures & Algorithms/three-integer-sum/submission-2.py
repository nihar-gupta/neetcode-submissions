class Solution:
    def threeSum(self, a: List[int]) -> List[List[int]]:
        ss = set()
        rt = []
        n = len(a)
        for i in range(n):
            sss = set()
            for j in range(i+1,n):
                tar = -(a[i] + a[j])
                if tar in sss: 
                    pppppp = [a[i], a[j], tar]
                    pppppp.sort()
                    ss.add(tuple(pppppp))
                sss.add(a[j])

        rt = list(ss)
        return rt

        