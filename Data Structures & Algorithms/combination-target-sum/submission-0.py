class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        def solve(a, i, t, c):
            if t==0:
                rt.append(c[:])
                return
            if i == len(a):
                return 
            
            solve(a,i+1,t, c)
            if t-a[i]>=0:
                c.append(a[i])
                solve(a, i, t-a[i], c)
                c.pop()
        rt = []
        solve(nums, 0, target, [])
        return rt


        