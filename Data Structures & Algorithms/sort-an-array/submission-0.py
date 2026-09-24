class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def ms(a, low, high):
            if low>=high: return 
            mid = (low+high)//2
            ms(a, low, mid)
            ms(a, mid+1, high)
            merge(a, low, high)
        
        def merge(a, low, high):
            mid = (low + high)//2
            p = []
            i = low
            j = mid+1
            while i<=mid and j<=high:
                if a[i] < a[j]:
                    p.append(a[i])
                    i+=1
                else:
                    p.append(a[j])
                    j+=1
            while i<=mid:
                p.append(a[i])
                i+=1
            while j<=high:
                p.append(a[j])
                j+=1
            for i in range(low, high+1):
                a[i] = p[i-low]
        ms(nums, 0, len(nums)-1)
        return nums

