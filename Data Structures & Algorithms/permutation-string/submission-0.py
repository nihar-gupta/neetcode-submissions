class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        def check(a,b):
            for i,j in a.items():
                if i not in b or b[i] != j: return False
            return True
        
        a = dict()
        for i in s1: a[i] = a.get(i, 0) + 1

        b = dict()
        i = 0
        n = len(s1)
        while i<n-1:
            b[s2[i]] = b.get(s2[i], 0)+1
            i+=1
        
        n = len(s2)
        j = 0
        while i<n:
            b[s2[i]] = b.get(s2[i], 0)+1
            if check(a, b): return True

            b[s2[j]] -= 1
            i+=1
            j+=1
        return False

        