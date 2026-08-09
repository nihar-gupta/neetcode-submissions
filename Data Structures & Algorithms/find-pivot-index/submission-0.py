class Solution:
    def pivotIndex(self, a: List[int]) -> int:
        n = len(a)
        ps = []
        s = 0
        for i in a:
            s = s + i
            ps.append(s)
        
        for i in range(n):
            left = ps[i] - a[i]
            right = s - left - a[i]
            if left == right: return i
        return -1
        
        