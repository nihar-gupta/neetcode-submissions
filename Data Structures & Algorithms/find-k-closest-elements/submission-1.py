class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:

        n = len(arr)

        i = 0
        s = 0
        while i<k:
            s = s + abs(x-arr[i])
            i+=1
        
        ans = s
        rt = arr[:i]
        j = 0

        while i<n:
            s = s+abs(x-arr[i])
            s = s-abs(x-arr[j])
            
            if s<ans:
                ans = s
                rt = arr[j+1: i+1]
            j+=1
            i+=1
        return rt


        