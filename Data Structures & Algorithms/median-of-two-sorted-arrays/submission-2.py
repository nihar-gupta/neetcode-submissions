class Solution:
    def findMedianSortedArrays(self, a: List[int], b: List[int]) -> float:
        if len(a) > len(b):
            # doing BS on shorter array takes less time
            a,b = b,a
            

        n = len(a)
        m = len(b)

        half = (n+m)//2

        # so now to divide the merged array into two halfs with half as a length

        low = 0
        high = len(a)

        while low<=high:
            mid = (low+high)//2

            # mid no of elements from A
            # half - mid, no of elements from B
            mid2 = half-mid # mid2 no of elements from B

            # l1 = left_most_element_from_A in left half 
            # l2 = left_most_element_from_B in left half 
            # r1 = right_most_element_from_A in right half 
            # r2 = right_most_element_from_B in right half 
            l1 = float('-inf')
            l2 = float('-inf')
            r1 = float('inf')
            r2 = float('inf')

            if mid-1>=0:
                l1 = a[mid - 1]  

            if mid2-1>=0:
                l2 = b[mid2 - 1]
            
            if mid < n:
                r1 = a[mid]

            if mid2 < m:
                r2 = b[mid2]

            # check if partition is correct or not
            # to do this l1 <= r2 and l2 <= r1

            if l1 <= r2 and l2 <= r1:
                # valid 
                # now median depends on n+m is even or odd
                if (n+m)%2 == 0 :
                    # even means we need to consider two ele avg 
                    return (max(l1,l2) + min(r1,r2))/2
                else:
                    # odd means median is in the right half of the array 
                    # because (n+m)//2 in odd will be a lesser number 
                    return min(r1,r2)
            
            elif l1 > r2:
                # meaning we have more elements in left half from array A 
                # so we need to take less elements 
                # meaning mid should be reduced 
                high = mid-1
            else:
                low = mid+1
        









        