class Solution:
    def minSubArrayLen(self, target: int, a: List[int]) -> int:

        s = 0

        n = len(a)
        ans = float('inf')
        found = False

        i = 0
        j = 0
        while i<n:
            s += a[i]
            if s<target:
                i+=1
            else:
                ans = min(ans, i-j+1)
                found = True

                while s>=target and j<=i:
                    ans = min(ans, i-j+1)
                    s=s-a[j]
                    j+=1
                i+=1
        if not found: return 0
        return ans




        