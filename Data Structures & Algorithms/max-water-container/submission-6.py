class Solution:
    def maxArea(self, a: List[int]) -> int:

        ans = 0
        p1 = 0
        p2 = len(a)-1
        while p1<p2:
            if a[p1] <= a[p2]:
                ans = max(ans, a[p1]*(p2-p1))
                p1+=1
            else:
                ans = max(ans, a[p2]*(p2-p1))
                p2-=1
        return ans


                

        

            

        
        