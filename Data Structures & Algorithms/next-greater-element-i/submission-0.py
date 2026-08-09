class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        d = dict()
        st = []
        n = len(nums2)
        p = []
        for i in range(n-1, -1, -1):
            d[nums2[i]] = i 

            while len(st)>0 and st[-1] <= nums2[i]:
                st.pop()
            
            if len(st) == 0 :
                p.append(-1)
            else:
                p.append(st[-1])
            
            st.append(nums2[i])
        
        p.reverse()

        rt = []
        for i in nums1:
            rt.append( p[d[i]] )
        return rt
        

        