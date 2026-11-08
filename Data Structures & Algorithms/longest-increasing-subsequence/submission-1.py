class Solution:
    def lengthOfLIS(self, a: List[int]) -> int:
        n = len(a)
        lis = [1 for i in range(n)]
        maxi = 1
        for i in range(1, n):
            ans = 0
            for j in range(i):
                if a[j] < a[i]:
                    ans = max(ans, lis[j])
            lis[i] = ans+1
            maxi = max(maxi, lis[i])
        return maxi


        