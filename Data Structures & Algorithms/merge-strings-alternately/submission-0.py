class Solution:
    def mergeAlternately(self, a: str, b: str) -> str:

        i = 0
        j = 0
        n = len(a)
        m = len(b)

        rt = ""
        while i<n and j<m:
            rt = rt + a[i] + b[j]
            i+=1
            j+=1
        
        if i<n:
            rt = rt + a[i:]

        if j<m:
            rt = rt + b[j:]
        return rt
        